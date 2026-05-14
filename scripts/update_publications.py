#!/usr/bin/env python3
"""
Fetch publications from ORCID and Google Scholar, merge with existing
hand-curated entries, and write/update _publications/*.md files.

ORCID ID  : 0000-0002-0872-4295
Scholar ID : HGfrQiUAAAAJ
"""

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

import requests

ORCID_ID = "0000-0002-0872-4295"
SCHOLAR_ID = "HGfrQiUAAAAJ"
PUBLICATIONS_DIR = Path("_publications")

ORCID_API = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
ORCID_WORK_API = f"https://pub.orcid.org/v3.0/{ORCID_ID}/work"

HEADERS_ORCID = {"Accept": "application/json"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_]+", "-", text)
    return text[:60].strip("-")


def yaml_escape(text: str) -> str:
    return text.replace('"', '\\"').replace("\n", " ").strip()


def existing_dois() -> dict:
    """Return mapping doi -> filepath for already-tracked publications."""
    doi_map = {}
    for f in PUBLICATIONS_DIR.glob("*.md"):
        content = f.read_text()
        m = re.search(r'^doi\s*:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE | re.IGNORECASE)
        if m:
            doi_map[m.group(1).strip().lower()] = f
    return doi_map


# ---------------------------------------------------------------------------
# ORCID
# ---------------------------------------------------------------------------

def fetch_orcid_works() -> list[dict]:
    """Fetch all work summaries from ORCID public API."""
    resp = requests.get(ORCID_API, headers=HEADERS_ORCID, timeout=20)
    resp.raise_for_status()
    data = resp.json()
    groups = data.get("group", [])
    works = []
    for group in groups:
        summaries = group.get("work-summary", [])
        if not summaries:
            continue
        s = summaries[0]  # take most recent version
        put_code = s.get("put-code")
        title_obj = s.get("title", {}) or {}
        title = (title_obj.get("title", {}) or {}).get("value", "")
        year_obj = (s.get("publication-date") or {}).get("year") or {}
        year = year_obj.get("value", "")
        journal_obj = (s.get("journal-title") or {})
        journal = journal_obj.get("value", "") if isinstance(journal_obj, dict) else ""
        # Extract DOI from external-ids
        doi = ""
        ext_ids = ((s.get("external-ids") or {}).get("external-id")) or []
        for eid in ext_ids:
            if eid.get("external-id-type", "").lower() == "doi":
                doi = eid.get("external-id-value", "")
                break
        works.append({
            "put_code": put_code,
            "title": title,
            "year": year,
            "journal": journal,
            "doi": doi,
        })
        time.sleep(0.1)
    return works


def fetch_orcid_work_detail(put_code: int) -> dict:
    """Fetch full work record for contributors/abstract."""
    resp = requests.get(f"{ORCID_WORK_API}/{put_code}", headers=HEADERS_ORCID, timeout=20)
    if resp.status_code != 200:
        return {}
    data = resp.json()
    contributors = []
    contrib_obj = (data.get("contributors") or {}).get("contributor") or []
    for c in contrib_obj:
        name = (c.get("credit-name") or {}).get("value", "")
        if name:
            contributors.append(name)
    abstract = ""
    short_desc = data.get("short-description") or ""
    if short_desc:
        abstract = short_desc
    return {"authors": contributors, "abstract": abstract}


# ---------------------------------------------------------------------------
# Google Scholar  (via scholarly)
# ---------------------------------------------------------------------------

def fetch_scholar_works() -> list[dict]:
    """Try to fetch from Google Scholar via scholarly. Fail gracefully."""
    try:
        from scholarly import scholarly as sc
        author = sc.search_author_id(SCHOLAR_ID)
        sc.fill(author, sections=["publications"])
        works = []
        for pub in author.get("publications", []):
            bib = pub.get("bib", {})
            title = bib.get("title", "")
            year = str(bib.get("pub_year", ""))
            journal = bib.get("journal", bib.get("booktitle", ""))
            doi = bib.get("doi", "")
            abstract = bib.get("abstract", "")
            authors_raw = bib.get("author", "")
            authors = [a.strip() for a in authors_raw.split(" and ")] if authors_raw else []
            works.append({
                "title": title,
                "year": year,
                "journal": journal,
                "doi": doi.lower(),
                "abstract": abstract,
                "authors": authors,
            })
        return works
    except Exception as e:
        print(f"[Scholar] Skipped ({e})", file=sys.stderr)
        return []


# ---------------------------------------------------------------------------
# Write Jekyll file
# ---------------------------------------------------------------------------

def write_publication(pub: dict, existing_path: Path | None = None) -> Path:
    year = str(pub.get("year", "2024"))
    title = pub.get("title", "Untitled")
    journal = pub.get("journal", "")
    doi = pub.get("doi", "")
    abstract = pub.get("abstract", "")
    authors = pub.get("authors", [])

    slug = slugify(title)
    date_str = f"{year}-01-01"
    filename = f"{date_str}-{slug}.md"
    out_path = existing_path or (PUBLICATIONS_DIR / filename)

    # Don't overwrite if file has hand-curated content (marked with # curated)
    if out_path.exists():
        content = out_path.read_text()
        if "# curated" in content:
            print(f"  [skip] hand-curated: {out_path.name}")
            return out_path

    paper_url = f"https://doi.org/{doi}" if doi else ""
    citation = ""
    if authors:
        first = authors[0] if authors else ""
        et_al = " et al." if len(authors) > 1 else ""
        citation = f"{first}{et_al} ({year}). {title}. {journal}."

    excerpt = abstract[:200] + "..." if len(abstract) > 200 else abstract
    if not excerpt:
        excerpt = f"{title}. {journal} ({year})."

    content = f"""---
title: "{yaml_escape(title)}"
collection: publications
category: manuscripts
permalink: /publication/{year}-{slugify(title)}
excerpt: '{yaml_escape(excerpt)}'
date: {date_str}
venue: '{yaml_escape(journal)}'
{"paperurl: '" + paper_url + "'" if paper_url else ""}
{"doi: '" + doi + "'" if doi else ""}
citation: '{yaml_escape(citation)}'
---

{abstract if abstract else ""}
"""
    out_path.write_text(content)
    print(f"  [write] {out_path.name}")
    return out_path


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    PUBLICATIONS_DIR.mkdir(exist_ok=True)
    tracked_dois = existing_dois()
    print(f"Existing tracked publications: {len(tracked_dois)}")

    # --- ORCID ---
    print("\nFetching ORCID works …")
    orcid_works = fetch_orcid_works()
    print(f"  Found {len(orcid_works)} works on ORCID")

    new_count = 0
    for work in orcid_works:
        doi = work.get("doi", "").lower()
        if doi and doi in tracked_dois:
            print(f"  [exists] {doi[:50]}")
            continue
        # Fetch detail for authors/abstract
        put_code = work.get("put_code")
        detail = fetch_orcid_work_detail(put_code) if put_code else {}
        work.update(detail)
        write_publication(work)
        if doi:
            tracked_dois[doi] = None
        new_count += 1
        time.sleep(0.3)

    print(f"\nORCID: {new_count} new publications written")

    # --- Scholar ---
    print("\nFetching Google Scholar works …")
    scholar_works = fetch_scholar_works()
    print(f"  Found {len(scholar_works)} works on Scholar")

    new_s = 0
    for work in scholar_works:
        doi = work.get("doi", "").lower()
        if doi and doi in tracked_dois:
            continue
        title_slug = slugify(work.get("title", ""))
        # Check if any existing file matches by title slug
        already = any(title_slug in str(p) for p in PUBLICATIONS_DIR.glob("*.md"))
        if already:
            continue
        write_publication(work)
        if doi:
            tracked_dois[doi] = None
        new_s += 1

    print(f"Scholar: {new_s} new publications written")
    print("\nDone.")


if __name__ == "__main__":
    main()
