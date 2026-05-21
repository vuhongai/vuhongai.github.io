---
name: "Hong Ai Vu · Academic Portfolio"
version: "2.0.0"
theme: cursor-adapted
description: >
  Cursor-adapted warm studio portfolio for a research scientist in gene therapy & AI.
  Single light-mode only. Precise sophistication through EB Garamond headings,
  Lato UI/body text, Cormorant Garamond hero-only, and an Onyx Orange accent palette.

colors:
  canvas-parchment: "#f7f7f4"  # page background — warm studio white
  pebble-gray:      "#e6e5e0"  # card/elevated surfaces — Pebble Gray
  highlight-beige:  "#cdcdc9"  # borders, dividers — Highlight Beige
  inkwell:          "#262510"  # primary text — near-black warm
  muted-stone:      "#7a7974"  # secondary text, captions, labels — Muted Stone
  onyx-orange:      "#f54e00"  # interactive accent — Onyx Orange
  goldenrod:        "#c08532"  # warm secondary accent
  forest-green:     "#34785c"  # success / HuggingFace links
  footer-bg:        "#1a1a16"  # near-black cool — footer background
  danger:           "#ee5f5b"

typography:
  hero:
    family: "'Cormorant Garamond', Georgia, serif"
    weights: [600]
    styles: [normal, italic]
    usage: "Hero name (.hero-name) ONLY"
  heading:
    family: "'EB Garamond', Georgia, serif"
    weights: [400, 500]
    styles: [normal, italic]
    letter-spacing: "-0.01em"
    google-fonts-url: "https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap"
  body:
    family: "'Lato', -apple-system, BlinkMacSystemFont, sans-serif"
    weights: [400, 600]
    size-base: "15px"
    line-height: 1.65
    letter-spacing: "0.01em"
    google-fonts-url: "https://fonts.googleapis.com/css2?family=Lato:wght@400;600&display=swap"
  monospace:
    family: "Monaco, Consolas, 'Lucida Console', monospace"
  scale:
    size-1: "2.441em"   # ~39px — hero names, display
    size-2: "1.953em"   # ~31px
    size-3: "1.563em"   # ~25px — h1
    size-4: "1.25em"    # ~20px — h2
    size-5: "1em"       # ~16px — h3, body
    size-6: "0.75em"    # ~12px — small, labels, badges
    size-7: "0.6875em"  # ~11px
    size-8: "0.625em"   # ~10px

spacing:
  border-radius: "4px"
  border-radius-card: "6px"
  box-shadow: "0 1px 3px rgba(0, 0, 0, 0.08)"
  box-shadow-card-hover: "0 8px 24px rgba(28, 22, 16, 0.08)"
  masthead-height: "68px"
  section-gap: "3rem"
  card-padding: "1.3rem 1.2rem"

breakpoints:
  small: "600px"
  medium: "768px"
  medium-wide: "900px"
  large: "925px"
  x-large: "1280px"

animation:
  global-transition: "all 0.2s ease-in-out"
  aos-duration: "700ms"
  aos-easing: "ease-out-cubic"
  aos-offset: "60px"
  countup-duration: "2s"
  typed-type-speed: 38   # ms per char
  typed-back-speed: 18
  typed-back-delay: 2800

components:
  focus-card:
    background: "var(--global-code-background-color)"   # #FAF7F2
    border: "1px solid var(--global-border-color)"
    border-radius: "6px"
    padding: "1.3rem 1.2rem"
    hover-transform: "translateY(-2px)"
    hover-border-color: "var(--global-base-color)"      # cognac
    icon-font-size: "1.4rem"
    title-font: "Inter"
    title-size: "0.7rem"
    title-weight: 700
    title-transform: "uppercase"
    title-spacing: "0.1em"
    body-size: "0.84rem"
    body-line-height: 1.6
  pub-item:
    border-left: "2px solid var(--global-border-color)"
    padding: "1rem 1.2rem 1rem 1.1rem"
    background: "var(--global-code-background-color)"
    font-size: "0.88rem"
    line-height: 1.65
    hover-border-color: "var(--global-base-color)"
    highlight-border-color: "var(--global-base-color)"
  pub-badge:
    font: "Inter"
    size: "0.65rem"
    weight: 600
    transform: "uppercase"
    spacing: "0.08em"
    color: "var(--global-base-color)"
    border: "1px solid var(--global-base-color)"
    border-radius: "2px"
    padding: "0.15em 0.55em"
  software-item:
    padding: "0.9rem 1.1rem"
    border: "1px solid var(--global-border-color)"
    border-radius: "5px"
    background: "var(--global-code-background-color)"
    font-size: "0.87rem"
    title-font: "Cormorant Garamond"
    title-size: "1rem"
    title-weight: 600
  stat-number:
    font: "Cormorant Garamond"
    size: "2.8rem"
    weight: 600
    color: "var(--global-base-color)"
    letter-spacing: "-0.02em"
  stat-label:
    font: "Inter"
    size: "0.68rem"
    weight: 600
    transform: "uppercase"
    spacing: "0.12em"
    opacity: 0.5
  section-heading-h2:
    font: "Inter"
    size: "0.72rem"
    weight: 700
    transform: "uppercase"
    spacing: "0.18em"
    color: "var(--global-base-color)"
    border-bottom: "1px solid var(--global-border-color)"
    margin-top: "3rem"
  hero-name:
    font: "Cormorant Garamond"
    size: "2.8rem"
    weight: 600
    letter-spacing: "-0.01em"
    line-height: 1.1
  hero-tagline:
    font: "Inter"
    size: "0.82rem"
    weight: 500
    spacing: "0.12em"
    transform: "uppercase"
    color: "var(--global-base-color)"
  hero-affiliation:
    font: "Cormorant Garamond"
    size: "0.88rem"
    style: italic
    opacity: 0.6
  masthead:
    background: "var(--global-bg-color)"
    border-bottom: "1px solid var(--global-border-color)"
    height: "68px"
    nav-font: "Inter"
    nav-size: "0.8rem"
    nav-weight: 500
    nav-transform: "uppercase"
    nav-spacing: "0.1em"
  table:
    font-size: "0.86rem"
    th-font: "Inter"
    th-size: "0.68rem"
    th-weight: 600
    th-transform: "uppercase"
    th-spacing: "0.1em"
    th-color: "var(--global-base-color)"
    th-border: "2px solid var(--global-base-color)"
    td-border: "1px solid var(--global-border-color)"
    row-hover-bg: "var(--global-code-background-color)"
---

# DESIGN.md — Hong Ai Vu Academic Portfolio

> This file is the single source of truth for the site's visual identity.
> Coding agents should read it before making any style, layout, or component change.

---

## Philosophy

The design is rooted in **classical academic elegance** — the kind found in a well-typeset monograph, not a startup landing page. Every decision reinforces three qualities:

1. **Warmth** — ivory backgrounds and cognac accents feel welcoming, not clinical.
2. **Authority** — serif headings (Cormorant Garamond) signal scholarly weight without stuffiness.
3. **Clarity** — Inter as the body typeface keeps reading fast and modern.

There is **no dark mode**. The site forces `data-theme="light"` on load. Do not introduce dark-mode variants.

---

## Color System

### Palette rationale

The palette is adapted from Cursor's warm studio design language — Canvas Parchment backgrounds, Pebble Gray elevated surfaces, and Onyx Orange as the single interactive accent. The palette is intentionally cooler and more precise than the previous cognac system.

| Token | Value | Use |
|---|---|---|
| `canvas-parchment` | `#f7f7f4` | Page background — warm studio white |
| `pebble-gray` | `#e6e5e0` | Card/elevated surfaces — Pebble Gray |
| `highlight-beige` | `#cdcdc9` | Borders, dividers — Highlight Beige |
| `inkwell` | `#262510` | Primary text — near-black warm |
| `muted-stone` | `#7a7974` | Secondary text, captions, labels — Muted Stone |
| `onyx-orange` | `#f54e00` | Interactive accent — Onyx Orange (links, hover, badges) |
| `goldenrod` | `#c08532` | Warm secondary accent |
| `forest-green` | `#34785c` | Success / HuggingFace links |
| `footer-bg` | `#1a1a16` | Footer — near-black cool |
| `danger` | `#ee5f5b` | Error states |

### Contrast note

The `onyx-orange` (#f54e00) on `canvas-parchment` (#f7f7f4) is a very high-contrast combination and should be used only for interactive affordances (links, hover states, badge outlines), never for paragraph-length text. Primary reading copy always uses `inkwell` (#262510) which provides strong contrast on parchment backgrounds.

---

## Typography

### Type pairing

| Role | Family | Weight | Notes |
|---|---|---|---|
| Display / H1 | Cormorant Garamond | 600 | Hero name, large headings |
| Headings H2–H6 | See below | — | H2 is overridden to Inter uppercase |
| Section label (H2 override) | Inter | 700 | 0.72rem, uppercase, 0.18em spacing |
| Body | Inter | 400 | 15.5px base, 1.7 line-height |
| Navigation | Inter | 500 | 0.8rem, uppercase, 0.1em spacing |
| Badges / labels | Inter | 600 | 0.65–0.72rem, uppercase |
| Captions / blockquotes | Cormorant Garamond | 400 italic | |
| Code | Monaco, Consolas, Lucida Console | — | |

### Critical rule

H2 inside `.page__content` is intentionally styled as a **small-caps label** (Inter 700, 0.72rem, uppercase), not as a traditional heading. This creates clear section breaks without competing with the prose. Do not change this without updating all section headings across the site simultaneously.

---

## Spacing & Layout

- **Border radius (default):** `4px` — used on code blocks, images, small UI elements.
- **Border radius (cards):** `6px` — focus cards, software items.
- **Max content width:** `1280px` ($x-large breakpoint).
- **Masthead height:** `68px` — body top-padding must match.
- **Section gap:** `3rem` top margin before each H2.

### Grid breakpoints

| Name | Value | Behavior |
|---|---|---|
| `small` | 600px | 2-col focus grid, responsive stats |
| `medium` | 768px | Sidebar appears |
| `large` | 925px | Main layout container max |
| `x-large` | 1280px | Masthead inner-wrap max |

---

## Components

### Focus cards (`.focus-card`)

Four-column grid on desktop, 2-col at `small`, 1-col at `400px`. Cards use the light background (`#FAF7F2`), a 1px warm border, and lift `translateY(-2px)` with cognac border on hover. Icon emoji at `1.4rem`, title in Inter uppercase `0.7rem`, body at `0.84rem`. **Do not add drop shadows at rest** — only on hover.

### Publication items (`.pub-item`)

Left-bordered cards. Default border is `#DDD3C4`; highlighted items (`.pub-highlight`) and hover state use the cognac primary. Background is `#FAF7F2`. Badges use Inter uppercase at `0.65rem` with a 1px cognac border and `2px` border-radius. Keep padding at `1rem 1.2rem 1rem 1.1rem` — the asymmetric left padding aligns copy with the border's visual weight.

### Stats row (`.stats-row`)

Flex row with `2.5rem` gap. Numbers in Cormorant Garamond 600 at `2.8rem`, cognac color. Labels in Inter 600 uppercase `0.68rem` at 50% opacity. Separated from surrounding content by `1px` warm borders top and bottom. CountUp.js animates numbers on scroll-into-view — always set both `data-countup` (end value) and a fallback text content for no-JS.

### Section headings (H2)

Inside `.page__content`, H2 is overridden: Inter 700, `0.72rem`, uppercase, `0.18em` letter-spacing, cognac color, `1px` warm border-bottom, `3rem` top margin, `1.2rem` bottom margin. This is intentional — it creates a label-style divider, not a typographic heading.

---

## Animations

| System | Config | Trigger |
|---|---|---|
| AOS (Animate On Scroll) | 700ms, ease-out-cubic, once, 60px offset | `data-aos="fade-up"` on section wrappers |
| CountUp.js | 2s duration, no grouping, useEasing true | IntersectionObserver at 35% threshold on `.stats-row` |
| Typed.js | typeSpeed 38, backSpeed 18, backDelay 2800ms, loop, HTML content | `#typed-tagline` span in hero |

When adding new sections to `about.md`, always add `data-aos="fade-up"` to the outer wrapper div. Do not add AOS to elements inside an already-animated parent — it creates stacked delays.

---

## What to avoid

- **Dark backgrounds inside content** — the theme is light-only; dark surfaces feel foreign.
- **Saturated accent colors** — the cognac palette is deliberately desaturated. Do not introduce blues, greens, or bright reds.
- **Sans-serif display text** — large hero text must stay in Cormorant Garamond.
- **Box shadows at rest** — reserve shadows for hover/active states only.
- **Inline `color:` styles that hardcode hex** — always use CSS custom properties (`var(--global-base-color)`, etc.) so the theme file remains the single source of truth.
- **Removing the `data-theme="light"` lock** — do not delete the `localStorage.setItem("theme", "light")` script in `_includes/head/custom.html`.

---

## File map

| File | Purpose |
|---|---|
| `_sass/theme/_elegant_light.scss` | All color tokens as SCSS variables + CSS custom properties |
| `_sass/_themes.scss` | Typography scale, breakpoint variables, brand colors |
| `_sass/_custom.scss` | Component styles (hero, cards, stats, pubs, software, tables) |
| `_sass/layout/_masthead.scss` | Fixed top nav bar |
| `_sass/layout/_base.scss` | Base HTML element styles |
| `_includes/head/custom.html` | Google Fonts links, AOS CSS CDN, favicon, theme lock |
| `_includes/scripts.html` | AOS + CountUp.js + Typed.js CDN and initialization |
| `_pages/about.md` | Homepage — hero, focus cards, stats, publications, awards, software |
| `_config.yml` | `site_theme: elegant` — controls which SCSS theme file is loaded |
