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

## Design-System

### Fonts (neu, wie agentur.juliabergles.de)

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500;1,600&display=swap">
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=object-sans@300,400,500,600,700&display=swap">
```

- **Headlines:** `'Playfair Display', serif`
- **Body / UI:** `'Object Sans', -apple-system, sans-serif`
- **Body-Größe:** 18–19 px (vorher 15–16 — zu klein)
- **Body-Weight:** 500 (vorher 300 — zu dünn)
- **Headline-Weight:** 500–700 je nach Größe

### Farben (aus altem Design behalten)

```css
--bordeaux: #955251;   /* Primary */
--copper:   #C48B6C;   /* Accent */
--warm-white: #F8F2EE; /* Background */
--warm-grey:  #F0E8E4;
--text-dark:  #3D2B2E;
--text-muted: #8A7B75;
```

**Kein Grün, kein Blau, kein Schwarz.** Warm bleibt warm.

### Nav

- Höhe: mehr Padding (aktuell zu eng)
- Links: **Object Sans, 15–16 px, weight 500**, mehr Padding pro Link
- Immer sticky, glasmorph mit blur
- Auf mobile: klarer Hamburger-Menü-Zustand

### Spacing

- Sektionen: `padding: 120px 24px` (vorher 100px — mehr Luft)
- Weißraum ist wichtig — Julias Content wirkt sonst gedrängt

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
