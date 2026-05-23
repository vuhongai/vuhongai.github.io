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

The design adapts Cursor's warm studio precision to an academic portfolio context. Every decision reinforces three qualities:

1. **Precision** — Pebble Gray elevated cards with layered shadow system signal craft without decoration.
2. **Authority** — EB Garamond headings and Cormorant Garamond hero text preserve scholarly weight.
3. **Clarity** — Lato as the UI/body typeface replaces Inter for a slightly warmer, more humanist feel.

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
| Hero name only | Cormorant Garamond | 600 | `.hero-name` ONLY — no other use |
| Content headings H3, author name, archive titles | EB Garamond | 400/500 | `-0.01em` letter-spacing |
| Section label (H2 override) | Lato | 700 | 0.68rem, uppercase, 0.18em spacing, Muted Stone color |
| Body | Lato | 400 | 15px base, 1.65 line-height |
| Navigation | Lato | 600 | 0.73rem, uppercase, 0.1em spacing |
| Badges / labels | Lato | 600 | 0.61–0.68rem, uppercase |
| Stats numbers | Cormorant Garamond | 600 | 2.6rem, Inkwell color (not orange) |
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

Four-column grid on desktop, 2-col at `small`, 1-col at `400px`. Cards use Pebble Gray background (`#e6e5e0`), no border, `border-radius: 4px`, and `shadow-subtle` at rest. On hover: `translateY(-2px)` + `shadow-xl`. Icon emoji at `1.3rem`, title in Lato uppercase `0.68rem`, body at `0.83rem` Muted Stone. **Cards elevate via shadow, not border changes.**

### Publication items (`.pub-item`)

Pebble Gray cards with `shadow-subtle` at rest, `shadow-xl` on hover. `.pub-highlight` items get a `2px solid onyx-orange` left border. Badges use Lato uppercase at `0.61rem` with a 1px onyx-orange border and `2px` border-radius and orange text.

### Stats row (`.stats-row`)

Flex row with `2.5rem` gap. Numbers in Cormorant Garamond 600 at `2.6rem`, **Inkwell color** (not orange). Labels in Lato 600 uppercase `0.63rem`, Muted Stone. Separated from surrounding content by `1px` Highlight Beige borders top and bottom. CountUp.js animates numbers on scroll-into-view — always set both `data-countup` (end value) and a fallback text content for no-JS.

### Section headings (H2)

Inside `.page__content`, H2 is overridden: Lato 700, `0.68rem`, uppercase, `0.18em` letter-spacing, **Muted Stone color** (not orange), `1px` Highlight Beige border-bottom, `3.5rem` top margin, `1.4rem` bottom margin. This creates a label-style divider, not a typographic heading.

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
- **Using orange for non-interactive text** — Onyx Orange is reserved for interactive affordances (links, hover, badges, `.pub-highlight` border). Stats numbers and section labels use Inkwell and Muted Stone respectively.
- **Sans-serif display text** — hero name must stay in Cormorant Garamond. Content headings use EB Garamond.
- **Hardcoding cognac (#7C5C3E) or old ivory (#F5F0E8)** — the palette has migrated to Cursor tokens. Always use CSS custom properties (`var(--color-inkwell)`, `var(--color-pebble-gray)`, etc.).
- **Inline `color:` styles that hardcode hex** — always use CSS custom properties so the theme file remains the single source of truth.
- **Removing the `data-theme="light"` lock** — do not delete the `localStorage.setItem("theme", "light")` script in `_includes/head/custom.html`.
- **Loading extra Cormorant Garamond weights** — only weight 600 normal and weight 400 italic are loaded. Do not add other weights.

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
