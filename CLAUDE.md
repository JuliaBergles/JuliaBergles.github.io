# CLAUDE.md — Regeln für juliabergles.de

> Regeln für Claude, wenn wir an juliabergles.de arbeiten.
> Zuerst `CONTEXT.md` lesen (was das Projekt ist, was gerade in Arbeit ist).

---

## Kern-Regeln

### 1. Texte gehören Julia

Julia schreibt alle Website- und Blog-Texte **selbst**.
Claude darf:
- ✅ Rechtschreibung, Grammatik, Kommas, Tippfehler korrigieren
- ✅ Formulierungen glätten — **aber nur wenn's danach noch nach Julia klingt**

Claude darf NICHT:
- ❌ Inhaltlich ergänzen (Fakten, Beispiele, Behauptungen) ohne Nachfrage
- ❌ Absätze umsortieren, Argumentation umbauen
- ❌ In KI-typische Sprache übersetzen („In der Tat", „Es ist wichtig zu beachten", „Wusstest du, dass...")
- ❌ Perfekt-balancierte Dreier-Listen bauen („gesund, glücklich und ausgeglichen")
- ❌ Werbe-Adjektive stapeln („liebevoll", „achtsam", „mit Herz")

**Wie Julia klingt** (aus echten Nachrichten):
- Direkt, kurz, umgangssprachlich („mag ich", „klapp alles", „so ne Sache")
- Zeigt Unsicherheit offen („glaub ich", „oder was meinst du?")
- Ich-Form, Emotionen erlaubt („ich hatte Angst", „ich war enttäuscht")
- Sätze dürfen kurz und abgehackt sein, dürfen auch mal mäandern
- Keine perfekte Rhetorik anstreben

Im Zweifel weniger anfassen als mehr.

### 2. Direkt handeln, nicht endlos fragen

Julia hasst lange Fragenkataloge.
- ✅ Machen, was klar ist
- ✅ EINE knappe Frage im Fließtext, wenn wirklich nötig
- ❌ 4-Punkte-Checklisten mit Klärungsfragen

### 3. Deploy = git push, direkt

- Änderungen sofort committen + auf `main` pushen — GitHub Pages baut in ~1 Min
- Julia testet **live am Handy**, nicht lokal
- Keine Preview-Umgebung, keine Zwischenschritte
- Commit-Messages auf Deutsch, kurz („Blog-Artikel Blähbauch fertig", „Nav größer + fetter")

---

## Design-System — v3 (ab 2026-08-17)

**Stil:** Editorial / Vogue-Zeitschrift. Warm-kühl kombiniert (Copper + Blau). Ruhig, elegant, viel Weißraum.
**Zentrales Stylesheet:** `assets/site-v3.css` — alle neuen Seiten binden dieses ein. Alte `assets/site.css` läuft parallel bis alle Seiten umgezogen sind.

### Fonts

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300;1,400;1,500&family=Manrope:wght@300;400;500;600;700;800&display=swap">
```

- **Headlines:** `'Cormorant Garamond', serif` — 400/500 weight, große Display-Sizes (bis 132px)
- **Body / UI:** `'Manrope', sans-serif` — 400/500/700
- **Betonung im Fließtext:** `<em class="italic">` (Cormorant italic) oder `<strong>` (bold)
- **Alternativ Body:** *Glacial Indifference* (Original aus dem E-Book) — WOFF2 in `assets/fonts/` legen, `@font-face`-Block in `site-v3.css` reaktivieren, im `--sans`-Token vor `'Manrope'` setzen. Solange Julia die Dateien nicht liefert, ist Manrope die ~95%-Alternative.

### Farben (v3 final)

```css
--cream:       #fffcf9;   /* Warm BG */
--beige:       #f4ede4;   /* Warm BG variant */
--copper:      #c48b6c;   /* Warm accent — CTAs, Buttons */
--copper-dark: #a87556;

--blue:        #8790c1;   /* Kühl accent — Zitate, Cards, ruhige Sektionen */
--blue-dark:   #6f78a8;
--mint:        #e2fffe;   /* Kühl BG variant — Leseproben, Ruhe-Momente */

--dark:        #2a2a2a;
--dark-soft:   #4a4a4a;
--mute:        #8a8a8a;
```

**Warm bleibt Basis, Blau ist Zweitakzent.** Copper für Aktion (CTA, Buttons), Blau für Editorial-Ruhe (Zitate, E-Book-Sektionen, gefährdete Themen wie Depressionen). Kein Grün, kein Schwarz.

### Editorial-Elemente

- **Chapter-Numerierung:** `Nº 01`, `Nº 02` — im Serif-Italic, klein, oberhalb der Überschrift
- **Eyebrow-Labels:** ALL CAPS, 11px, Letter-Spacing 0.22em — vor jeder Section-Überschrift
- **Pull-Quotes:** Cormorant italic, groß, blauer Rand links
- **Trenn-Ornamente:** `§` oder `—` zentriert, dünne Linien
- **Buttons:** rechteckig (kein Border-Radius), ALL CAPS, Letter-Spacing weit

### Nav

- Sticky, halbtransparent (`rgba(255,252,249,0.92)` + backdrop-blur)
- Logo: Cormorant serif, „Julia · Bergles" mit Copper-Trenner
- Links: Manrope 12px, ALL CAPS, Letter-Spacing 0.18em
- Mobile: Hamburger (noch nicht v3-umgesetzt)

### Spacing

- Sektionen: `padding: clamp(80px, 12vw, 160px) 0`
- Container: `max-width: 1280px`, `max-width-narrow: 780px`
- Weißraum ist heilig — Editorial-Look lebt davon

---

## Content-Regeln

### Ton

- Persönlich, ehrlich, verletzlich wenn passend
- Nie belehrend, nie „Coach-Sprech"
- Betroffene-Perspektive, nicht Experten-Perspektive
- Duz-Ansprache immer

### Medizinische Disclaimer (nicht verhandelbar)

- **Kein Heilversprechen** — nie „heilt", „macht gesund", „löst das Problem"
- Erlaubt: „hat mir geholfen", „bei mir wurde besser", „meine Erfahrung"
- Auf jeder Info-Seite (HIT / MCAS / Reizdarm): Kurzer Disclaimer am Ende: *„Das ist meine Erfahrung, keine medizinische Beratung. Bitte sprich mit einem Arzt/Therapeut."*
- Bei Peer-Support-Telefonaten: klar „Erfahrungsaustausch", nicht „Beratung" (Heilpraktiker-Gesetz)

### Affiliate

- **aho.bio** — Code `Smacado10`, Link `aho.bio/smacado10`
- Andere Codes siehe TerraLuna-App-Kontext, falls relevant
- Immer als **„Partnerempfehlung"** kennzeichnen
- Ehrlich bleiben — Partnerprodukte bekommen auch Warnungen, wenn was nicht passt

---

## Ordner-Struktur

```
juliabergles Website/
├── .git/                    # Git-Repo → github.com/JuliaBergles/JuliaBergles.github.io
├── CNAME                    # juliabergles.de
├── CONTEXT.md               # Was das Projekt ist, aktueller Plan
├── CLAUDE.md                # Diese Datei — Regeln
├── index.html               # Startseite
├── app.html                 # TerraLuna App-Landing
├── impressum.html, datenschutz.html, agb.html, widerruf.html
├── ueber-mich.html          # (optional, wenn Julia will)
├── selbsttest.html          # Bleibt
├── empfehlungen.html        # aho.bio + tägliche Lebensmittel
├── histaminintoleranz.html  # NEU — Info-Seite
├── mcas.html                # NEU — Info-Seite
├── reizdarm.html            # NEU — Info-Seite
├── blog/                    # NEU
│   ├── index.html           # Blog-Übersicht
│   └── [artikel-slug]/
│       └── index.html
├── blog-bilder/             # Julias Rohbilder (unsortiert)
├── images/                  # Website-Bilder (bestehend)
├── eatmoreart.html          # WYH — bleibt liegen, NICHT verlinken
├── bestellen.html           # WYH — bleibt liegen, NICHT verlinken
├── bestell-uebersicht.html  # WYH
├── danke.html               # WYH
├── funnel.html              # WYH
└── ...                      # rest wie gehabt
```

**Neue Blog-Ordner-Regel:** ein Ordner pro Artikel (`blog/blaehbauch-in-griff/index.html`) — dann können pro Artikel Bilder direkt danebenliegen und URL ist `juliabergles.de/blog/blaehbauch-in-griff/`.

---

## Dinge, die wir NIE machen

- ❌ WYH-Dateien löschen — nur aus Nav/Links raus
- ❌ Heilversprechen
- ❌ Ärzte namentlich negativ nennen (Ärger-Content darf, aber ohne Namen)
- ❌ KI-glattgebügelte Sprache in Julias Texten
- ❌ Neue Farben einführen (bordeaux/copper bleibt)
- ❌ Grün oder Blau anywhere (Ausnahme: Ampel-Icons falls medizinisch nötig)
- ❌ Force-Push auf `main`
- ❌ Ohne Nachfrage inhaltlich in Julias Texte eingreifen

---

## Wenn du diese Datei liest…

…dann arbeitest du gerade an juliabergles.de. Zuerst CONTEXT.md lesen (aktueller Plan, was in Arbeit). Dann loslegen — schnell, direkt, weniger fragen, mehr machen.
