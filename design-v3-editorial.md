# Design v3 — Editorial / Vogue

> Aktuelles Live-Design (ab 2026-08-17). Orientiert am E-Book-Cover „Die Probe".
> **Stylesheet:** `assets/site-v3.css` — jede Seite bindet `<link rel="stylesheet" href="assets/site-v3.css">` ein.

---

## Stimmung in einem Satz

Vogue-Zeitschrift trifft persönliches Journal. Kühle Ruhe, warme Akzente, große Bilder, viel Weißraum.

## Fonts

```html
<!-- Google Fonts -->
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500&family=Manrope:wght@300;400;500;600;700;800&display=swap">
```

- **Headlines:** Cormorant Garamond (Serif), weight 400/500, groß bis riesig (bis 132 px Display)
- **Body/UI:** Manrope (Sans, geometric), 17 px, weight 400/500
- **Betonung:** `<em class="italic">` (Cormorant italic) für elegante Betonung, `<strong>` für Fett
- **Chapter-Marker:** `Nº 01`, `Nº 02` — Cormorant italic, klein, oberhalb H3
- **Eyebrow-Labels:** Manrope 11 px, weight 700, ALL CAPS, Letter-Spacing 0.22em

## Farben

```css
--cream:       #fffcf9;   /* Warm BG */
--beige:       #f4ede4;   /* Warm BG variant */
--copper:      #c48b6c;   /* CTA, Buttons */
--copper-dark: #a87556;

--blue:        #8790c1;   /* Kühl accent */
--blue-dark:   #6f78a8;
--mint:        #e2fffe;   /* Kühl BG variant */

--pink:        #e8b4c1;   /* Blush - nur sehr sparsam */
--pink-soft:   #f9e0e6;

--dark:        #2a2a2a;
--dark-soft:   #4a4a4a;
--mute:        #8a8a8a;
```

**Regeln:**
- **Warm ist Basis** (Cream, Copper).
- **Blau als Zweitakzent** — für Editorial-Ruhe, Zitate, gefährdete Themen. Dezent dosiert (`.blue-soft` mit Mint-BG + blauem Text ist die bevorzugte Variante — nicht vollflächig `.blue`).
- **Rosa nur sehr sparsam** (Julia findet vollflächiges Rosa zu krass).
- **Copper für CTA/Buttons** — führt das Auge.
- **Kein Grün. Kein reines Schwarz `#000`.**

## Editorial-Elemente

- **Buttons:** rechteckig (kein `border-radius`), ALL CAPS, Letter-Spacing 0.18em, Padding 18/36. Standard = `.btn.btn-copper`.
- **Cards:** `.editorial-card` = Cream + dünne Border. Varianten: `.blue-soft` (dezent), `.blue` (voll), `.beige`, `.mint`, `.dark`.
- **Pull-Quote:** Cormorant italic, groß, blauer Rand links (`.pullquote`)
- **Trenn-Ornamente:** `<div class="ornament">§</div>` oder `<hr class="divider">`
- **Full-Bleed Bilder:** `<img class="full-image">` als Break zwischen Sektionen (70 vh)
- **Grid-2 / Grid-3 / Grid-hero:** Split-Layouts (2- und 3-Spalten, auf Mobile stacken)

## Nav

```html
<nav class="nav-v3" id="navV3">
  <div class="container">
    <a href="index.html" class="logo">Julia<span class="amp"> ·</span> Bergles</a>
    <ul class="nav-main">
      <li><a href="ueber-mich.html">Über mich</a></li>
      <li class="has-dropdown">
        <span class="nav-link">Diagnosen <span class="caret">▾</span></span>
        <ul class="dropdown">
          <li><a href="histaminintoleranz.html">Histamin</a></li>
          <li><a href="mcas.html">MCAS</a></li>
          <li><a href="reizdarm.html">Reizdarm</a></li>
        </ul>
      </li>
      <li><a href="selbsttest.html">Selbsttest</a></li>
      <li><a href="blog/">Blog</a></li>
      <li><a href="rezepte.html">Rezepte</a></li>
      <li class="has-dropdown">
        <span class="nav-link">Shop <span class="caret">▾</span></span>
        <ul class="dropdown">
          <li><a href="ebook-reisen.html">E-Books</a></li>
          <li><a href="bilder.html">Kunst</a></li>
          <li><a href="app.html">TerraLuna App</a></li>
        </ul>
      </li>
      <li><a href="empfehlungen.html">Empfehlungen</a></li>
    </ul>
    <a href="gespraech.html" class="nav-cta">Gespräch</a>
    <button class="burger" onclick="document.getElementById('navV3').classList.toggle('open')" aria-label="Menü">☰</button>
  </div>
</nav>
```

## Sektions-Klassen

- `.section` + eine Farbklasse: `.section-cream`, `.section-beige`, `.section-mint`, `.section-blue`, `.section-dark`, `.section-pink` (sparsam)
- Padding vertikal: `clamp(80px, 12vw, 160px)`
- Container: `.container` (max 1280 px) oder `.container-narrow` (max 780 px)

## Live-Referenz-Seiten

- Startseite: `index.html`
- E-Book-Landing: `ebook-reisen.html`

## Wenn Julia wieder auf v3 wechseln will

Auf jeder Seite:
1. `<link rel="stylesheet" href="assets/site-v3.css">` (statt v2/altes)
2. Google-Font-Link im Head
3. Nav-Block ersetzen (siehe oben)
4. Inline-Styles vom alten Design entfernen wo möglich
