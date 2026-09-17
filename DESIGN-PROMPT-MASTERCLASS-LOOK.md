# Design-Prompt: juliabergles.de an den Masterclass-Look angleichen

Zum Copy-Paste in Claude Code, wenn du im Ordner `juliabergles Website` bist.

---

## Kontext für den Assistenten

Ich möchte, dass alle Seiten von juliabergles.de exakt dem Design-System folgen, das ich in der Histamin Masterclass (terra-luna-masterclass.vercel.app) verwende. Das ist mein Referenz-Look. Bitte gleiche das gesamte Design an, ohne bestehende Inhalte zu verändern. Behalte alle Texte, Bilder und Links – tausche nur Look, Layout, Struktur und interaktive Bausteine aus.

Die neue Design-Sprache heißt intern **Herbstwald v4** und folgt diesen Regeln:

---

## 1) Farbwelt (fest)

```css
--warm-cream:     #faf4eb;   /* Basis-Hintergrund */
--warm-charcoal:  #3d322a;   /* Fließtext */
--cocoa:          #5a4a3f;   /* Sekundärer Text */
--copper:         #C48B6C;   /* Primär-Akzent, Labels, Buttons Sekundär */
--copper-dark:    #a4735a;   /* Copper hover */
--malaga:         #6d2e3a;   /* Buttons Primär, Überschriften, Tiefe */
--malaga-deep:    #4d1e28;   /* Malaga hover */
--warm-gold:      #c9a96e;   /* Premium-Akzent */
--soft-peach:     #f5e4d0;   /* Sanfte Sektions-Fläche */
--soft-linen:     #f0e9dc;   /* Alternative Section-Fläche (beige) */
--mint:           #d7ecdc;   /* Alternative Section-Fläche */
--flieder:        #e6dcf0;   /* Alternative Section-Fläche */
--warm-gray:      #8a7a6f;   /* Muted / kleine Info */
```

**Regeln:**
- Kein Grün, kein Blau (außer Männer-Modus in der App – hier irrelevant)
- Rot nur als `#e37f7f` (Verträglichkeits-Symbol „meiden"), nie sonst
- Alle Shadows in Copper-Ton, niemals Schwarz

---

## 2) Typografie

```css
--font-display: 'Madelyn', 'Playfair Display', Georgia, serif;   /* Sehr groß, italic */
--font-heading: 'Source Serif 4', Georgia, serif;                /* Überschriften */
--font-body:    'Glacial Indifference', system-ui, sans-serif;   /* Fließtext, UI */
```

**Regeln:**
- Überschriften in Source Serif 4, **Farbe malaga**, Weight 600
- Italic (`em`, `.italic`) für emotionale Einzelwörter innerhalb von Headings: *Kurz zu mir*, *Deine Optionen*, *Kennst du das?*
- Body in Glacial Indifference, 17px, Line-Height 1.6
- Display-Font Madelyn nur für den Hero
- Sizes: h1 clamp(28px, 4.5vw, 44px), h2 clamp(24px, 3.5vw, 34px), display clamp(48px, 7vw, 96px)

---

## 3) Layout-System

### Sektionen (Signatur des Designs)

Jede Seite ist in klare Sektionen unterteilt mit **alternierenden Hintergründen**:

```
Cream (warm-cream)  →  Peach (soft-peach)  →  Mint  →  Beige (soft-linen)  →  Cream ...
```

Pro Sektion:
- Padding oben/unten: `clamp(80px, 12vw, 160px)`
- Padding links/rechts: `clamp(24px, 5vw, 60px)`
- Container-Breite: max 1280px (normal) oder 780px (schmal für Text/FAQ)

### Aufbau innerhalb einer Sektion

```
1. Eyebrow (kleiner Label-Text, oben)
2. Überschrift mit italic-Wort (z.B. „Der <em>Inhalt</em>.")
3. Optional: Lead-Text (kurze Einleitung)
4. Content (Grid, Karten, Text)
5. CTA-Button am Ende (führt zur nächsten Sektion)
```

---

## 4) Wiederkehrende Komponenten

### Eyebrow (Label über Überschrift)

```html
<span class="eyebrow eyebrow-copper eyebrow-line">Der Inhalt</span>
```

- 11px, `font-weight: 700`, `letter-spacing: 0.22em`, UPPERCASE
- Farbe copper (oder gold, malaga für Varianten)
- Mit `.eyebrow-line` → horizontale Linien vor und nach dem Text (24px, opacity 0.5)

### Buttons

```html
<a class="btn btn-copper">Primär-CTA</a>
<a class="btn btn-outline">Sekundär-CTA</a>
<a class="btn btn-malaga">Alternative Primär</a>
```

- **Alle Buttons rund (border-radius: pill)**
- Padding: 16px 32px
- Font-weight: 500, Font-size: 16px
- Copper hat warmen Shadow (`0 3px 10px rgba(196,139,108,0.3)`)
- Outline hat 2px Border in Copper

### Editorial-Card

```html
<article class="editorial-card">
  <span class="eyebrow eyebrow-copper">Label</span>
  <h3>Titel</h3>
  <p>Inhalt</p>
</article>
```

- `background: white`
- `border-radius: 24px` (unser Signatur-Radius für alle Karten)
- `box-shadow: 0 3px 10px rgba(196, 139, 108, 0.08)` (warm-copper, nie schwarz)
- Padding 32–40px
- Bei Hover: shadow etwas stärker, leichtes translateY(-2px)

Variante `.editorial-card.blue` (jetzt malaga):
- `background: var(--malaga)`, `color: white`
- Eyebrow-Farbe wird zu `var(--soft-peach)`

### Chapter-Num (für Wochen, Nummern, Kapitel)

```html
<span class="chapter-num">Woche 3</span>
```

- Klein, Copper, Uppercase, Letter-Spacing 0.2em
- 11–12px

### Marquee-Ticker (oben unter Nav auf Landing/wichtigen Seiten)

- Horizontaler Ticker in Copper-Hintergrund, weißer Text
- Rotierende Botschaften mit `·` als Trennzeichen
- Animation: 40s linear infinite

---

## 5) Navigation

Sticky Top-Nav mit:
- Logo links (`Julia · Bergles` – Serif, klein)
- Zentrale Anker-Links (Über mich, Angebote, Rezepte, Blog)
- Rechts: sekundärer Link (Login) + primärer CTA-Button („Masterclass")

Auf Landing/Verkaufsseiten zusätzlich **Sprungmarken** innerhalb der Seite (nicht nur zu anderen Seiten), damit man von oben direkt zum Content springen kann.

---

## 6) Bilder

- Immer in `border-radius: 24px` gerundet
- Warmer Shadow drunter: `0 20px 60px rgba(109, 46, 58, 0.15)`
- Für emotionale Fotos (Julia in Piran, Blumen): mit warmem Beige/Peach-Overlay wenn im Hintergrund

---

## 7) Sektions-Enden brauchen Buttons

**Nie eine Sektion ohne CTA am Ende.** Beispiele:
- „Kennst du das?" → „Ich bin dabei →"
- „Wochenthemen" → „Was kostet die Masterclass? →"
- „FAQ" → „Zur Anmeldung →"
- „Kurz zu mir" → „Ist das etwas für mich? →"

So navigiert man mit Klicks durch, nicht mit endlosem Scrollen.

---

## 8) Was du konkret machen sollst

1. **Lies zuerst** die Referenz-Datei `assets/site-v4.css`, dann `histamin-masterclass.html` **von terra-luna-masterclass.vercel.app** (siehst du im Browser, live)
2. Gehe die Liste aller HTML-Dateien im Root-Verzeichnis durch (`ls *.html`)
3. Wende auf **jede** dieser Seiten die neue Design-Sprache an:
   - Ersetze alte Hintergründe durch die neuen Section-Farben
   - Alle Karten auf `border-radius: 24px` und warmen Copper-Shadow
   - Alle Buttons auf pill-shape (Copper/Outline/Malaga)
   - Überschriften mit italic-Wörtern (wo emotional passend)
   - Eyebrow-Labels oben in jeder Sektion
   - Am Sektionsende jeweils einen sinnvollen CTA-Button
   - Sprungmarken in der Nav für seiten-interne Navigation
4. **Nicht ändern:** Texte, Bilder, Reihenfolge der Inhalte
5. **Nicht neu erfinden:** Farben, Radii, Shadows – exakt aus `--warm-cream`, `--copper`, `--malaga` etc.
6. Nach jeder Seite: `git add <file> && git commit && git push`. GitHub Pages deployed automatisch.

---

## 9) Reihenfolge – wo zuerst starten

**Priorität 1** (die verkaufsrelevanten Seiten zuerst):
- `index.html`
- `app.html`
- `ebooks.html`
- `gespraech.html`
- `live-calls.html`
- `histaminintoleranz.html`

**Priorität 2** (informative Seiten):
- `ueber-mich.html`
- `mcas.html`, `reizdarm.html`, `pms.html`, `angststoerung.html`
- `rezepte.html`

**Priorität 3** (Unterseiten und Details):
- Alles in `/rezepte/`, `/blog/`, `/empfehlungen/`

---

## 10) Wichtige Prinzipien (Roter Faden)

1. **Warm, feminin, editorial** – nie clinical, nie flat
2. **Weißraum ist Design** – lieber weniger, dafür großzügiger
3. **Buttons statt Scroll** – Nutzer:innen sollen navigieren können
4. **Eine Marke, ein Guss** – App, Masterclass, Website müssen wie drei Räume desselben Hauses wirken
5. **Kein Grün, kein Blau, kein Schwarz-Shadow** – die Palette ist absichtlich eng
6. **Italic für Emotion** – *Kurz zu mir*, *Deine Optionen*, *Kennst du das?* – nie in Fließtext, nur in Headings
7. **Bilder haben Rundungen** – 24px auf alles was ein Bild ist
8. **Marquee für Signal** – Copper-Ticker signalisiert „hier ist etwas Wichtiges"

---

## 11) Live-Referenz

**Immer die Landing der Masterclass als Vorbild:**
https://terra-luna-masterclass.vercel.app

Dort siehst du:
- Wie die Marquee aussieht
- Wie die Sektionen abwechseln
- Wie die Buttons am Ende jeder Sektion Nutzer weiterführen
- Wie Bilder eingebettet sind
- Wie das FAQ zum Aufklappen aussieht
- Wie der finale CTA-Block wirkt (dunkles Malaga-Rechteck mit Foto im Hintergrund)

**Alles was du dort visuell siehst, ist Ziel-Zustand für juliabergles.de.**
