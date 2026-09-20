# juliabergles.de — Kontext & Plan

> Was diese Website ist, wo sie hin soll, was gerade in Arbeit ist.
> Bei jeder Session zuerst hier reinschauen.
> Letzte Aktualisierung: 2026-09-18

---

## Was ist das hier

Julia Bergles' Personal-Brand-Website unter **www.juliabergles.de**.

- Deploy: **GitHub Pages** (Repo: `github.com/JuliaBergles/JuliaBergles.github.io`)
- Ordner-Pfad: `~/Library/Mobile Documents/com~apple~CloudDocs/juliabergles Website/`
- CNAME → `juliabergles.de`
- Julia testet **live am Handy** — kein lokaler Preview-Zwischenschritt
- Deploy = `git push origin main` (GitHub Pages baut in ~1 Min)

**Julia in Kürze** (20, Wehringen bei Augsburg):
- Instagram: @julia_bergles · WhatsApp: **+49 1511 8515394**
- Corona → Geschmackverlust → Orthorexie → Darmverschluss mit 19 → 2 Jahre nur 5 Lebensmittel → heute mehr
- Diagnosen: **Histaminintoleranz** (Arzt + Cerascreen bestätigt), Allergien (Kartoffel, Apfel, Mandeln, Haselnüsse, Karotte Sommer, Latex, Nickel, Erdnüsse, Soja), **PMS**, Pollenallergie
- Vermutet: **MCAS**
- Heute im Griff: regelmäßig essen, wenig Ballaststoffe, kein HIIT, angstfrei essen, 10 Min nach Essen laufen, gekeimte Lebensmittel

---

## Zwei Marken / Zwei Projekte

Die Website ist Teil eines größeren Öko-Systems. Klarheit welches Repo welches Ziel hat:

| | juliabergles.de | terra-luna-masterclass.vercel.app |
|---|---|---|
| Zweck | Persönliche Marke, Blog, E-Books, App-Info, Peer-Support | **Histamin Masterclass** (Landing + Anmeldung + Kursbereich) |
| Repo | `github.com/JuliaBergles/JuliaBergles.github.io` | `github.com/JuliaBergles/terra-luna-masterclass` |
| Lokal | `~/Library/Mobile Documents/com~apple~CloudDocs/juliabergles Website/` | `~/Projects/terra-luna-masterclass/` |
| Stack | Statische HTML + `assets/site-v3.css` | Next.js 16 + Tailwind v4 + Supabase (Auth+DB) + Vercel |
| Deploy | `git push` → GitHub Pages | `git push` → Vercel auto-deploy |

Verlinkung: `histamin-masterclass.html` auf juliabergles.de ist ein Meta-Refresh-Redirect zu `terra-luna-masterclass.vercel.app` (Julia hat das so eingerichtet). Der Nav-Link „Masterclass ★" führt direkt zur Vercel-URL.

---

## Aktueller Design-Stand (juliabergles.de, Stand 2026-09-18)

**Design-System v3 — Editorial (Cormorant + Manrope):**

- Fonts: **Cormorant Garamond** (Headlines, weight 400) + **Manrope** (Body/UI)
- Zentrales Stylesheet: `assets/site-v3.css`
- v4 wurde probiert (App-Look angeglichen), dann per Rollback wieder auf v3 zurück. `assets/site-v4.css` liegt noch da, wird aber nicht mehr gebunden.

**Farbwelt aktuell:**
- Basis: Cream `#fffcf9`, Beige `#f4ede4`, Dark `#2a2a2a`, Mute `#8a8a8a`
- Warm: Copper `#c48b6c` — hell veränderbar (siehe Buttons)
- Kleid-Blau (aus Julias PDF-Bild): `#2a4a68` dunkel, `#bec2d9` gedeckt (das ehemalige hellblaue #cbdeed wurde durch dieses gedecktere Blau ersetzt), `#eff5fa` fast weiß
- Editorial-Blau (v3 default): `#7768a3` — kommt kaum noch vor
- Mint: `#e2fffe`

**Buttons (nach Julias Iterationen):**
- **`.btn-kleidblau`** — Kleid-Blau BG `#2a4a68` + weiße Schrift (primärer CTA auf Startseite: Hero, Themen, Blog, Empfehlungen, App, Gespräch)
- **`.btn-copper`** — jetzt Warmbeige `#e1ded5` mit dunkler Schrift (NICHT mehr braun/kupfer — Julia wollte alle „braunen" Buttons zu Warmbeige)
- **`.btn-outline`** — transparent mit dark Border
- **Nav-CTA „Masterclass"** oben rechts: Kleid-Blau

**Marquee (Ticker unter Nav):** Kleid-Hellblau `#bec2d9` mit dunkelblauer Schrift (nicht mehr schwarz/malaga)

**Hero:** kein dunkler Overlay-Filter mehr auf dem Bild — pur, mit Text-Shadow für Lesbarkeit

---

## Nav (aktuell auf allen 72 aktiven Seiten)

```
Über mich  |  Themen ▾  |  Rezepte ▾  |  Masterclass ★  |  App  |  E-Books  |  Mehr ▾    [Anmelden / Gespräch]
```

- **Themen ▾**: Histamin · MCAS · Reizdarm · PMS & Zyklus · Angststörung · Selbsttest · Blog
- **Rezepte ▾**: Übersicht + 6 Kategorien
- **Masterclass ★**: direkter Link zu `terra-luna-masterclass.vercel.app` (externes Ziel)
- **App**: direkt zu `app.html` (TerraLuna App-Landing)
- **E-Books**: direkt zu `ebooks.html`
- **Mehr ▾**: Live Calls · 1:1 Gespräch · Empfehlungen · Kunst
- **CTA rechts**: „Anmelden" führt zu `masterclass-anmeldung.html` (Vercel-Redirect zur Anmeldeseite)

Julia hat mehrfach zwischen Nav-Varianten iteriert. Vorherige Versionen mit „Angebote" / „Shop" wurden verworfen.

---

## Startseite (index.html) — Sektionsfolge

1. Nav
2. Marquee
3. **Call-CTA-Banner** oben: Kleid-Hellblau, „Neu · Meine Histamin Masterclass ist da." → Vercel-Link
4. Hero (Full-Bleed Bild von Julia im blauen Kleid Piran, kein Filter)
5. **„Kennst du das?"** Pain-Sektion (5 Karten inkl. „Kein Arzt versteht dich", „Psychisch krank abgestempelt")
6. Themen-Sektion mit Pfingstrosen-Deko + 6 Copper-Karten (Histamin/MCAS/Reizdarm/Blähbauch/Ängste/Depressionen)
7. Full-Bleed IMG_4680 (Julia auf Piazza)
8. Blog-Sektion (3 aktuelle Artikel)
9. **Masterclass-Herzstück** — Verweis auf Vercel-Landing
10. E-Books & Community
11. Empfehlungen
12. App (mit **„3 Tage kostenlos testen" + „Zur App"** Buttons)
13. Gespräch/Peer-Support
14. Footer

---

## E-Books (`ebooks.html`)

Alle E-Books über Mail-Vorkasse (`julia@bergles.net`). Aktueller Katalog:

| Nº | Titel | Preis | Status |
|---|---|---|---|
| 01 | Die Probe (Reisen mit Histamin) | 7,99 € | verfügbar, echtes Cover |
| 02 | **Das Seelenbauchbuch** (138 S. Leitfaden Unverträglichkeiten) | **15,99 €** | verfügbar, **Placeholder-Cover** |
| 03 | **Iss dich stabil** (Ernährungsleitfaden) | 19,99 € | verfügbar, **Placeholder-Cover** |
| 04 | Zyklus-Leitfaden | 1,99 € | verfügbar |
| 05 | Freebie „Histamin & Ängste der Familie erklären" | kostenlos | in Arbeit |
| 06 | So wird man seine Ängste los | 14,99 € | in Arbeit |
| 07 | Was Depressionen mit einem machen | 14,99 € | in Arbeit |
| 08 | Live Calls (Format) | 32 €/Call | verfügbar |

**Kein KI-Text · kein Coach-Sprech**-Formulierungen wurden auf Julias Wunsch entfernt. Ersetzt durch „Von einer Betroffenen. Für Betroffene."

**Content-Regel:** die zwei E-Books Seelenbauchbuch + Iss dich stabil zeigen nur eine **Inhaltsliste**, keinen Verkaufstext (Julia's Ansage: „Leseprobe/Inhalt statt Direkttext").

---

## Histamin Masterclass — auf Vercel (nicht hier)

Volle Landing + Anmeldung + späterer Kursbereich läuft im separaten Repo `terra-luna-masterclass`. Auf juliabergles.de nur:

- **Nav-Link** „Masterclass ★" → Vercel
- **`histamin-masterclass.html`** → Meta-Refresh + JS-Redirect zur Vercel-URL (Julia hat das selbst eingerichtet)
- **`masterclass-anmeldung.html`** → Redirect zu Vercel `/anmeldung`
- **AGB § 5a** (Standard-Masterclass Self-Study 399 € + 1:1 780 €)
- **AGB § 5c** (Herbstspecial 2026: feste Kohorte 01.10.–01.12., 3 Pakete 399/699/825 € + Ratenzahlung + Klein enthält Einstiegs- & Endcall + Notizbuch/Überraschungspaket für Mittel/VIP)
- **Datenschutz** (WhatsApp-Sonntags-Check-in, Videokonferenz-Anbieter für 1:1, Calendly)
- **Widerruf** (Masterclass: 14 Tage, erlischt bei Zugriff auf digitale Inhalte; Peer-Support-Gespräche: 24-h-Storno)

---

## Peer-Support-Telefonate

- 25 €/30 Minuten via Calendly (`calendly.com/julia-bergles/30min`)
- Positionierung: **„Erfahrungsaustausch" / „Peer-Support"** — NIEMALS „Beratung" oder „Coaching" (Heilpraktiker-Gesetz)
- Disclaimer: „Ich teile meine eigene Erfahrung. Keine medizinische Beratung, kein Ersatz für Arzt/Therapeut."

---

## TerraLuna App

- **App heißt TerraLuna** — überall so benannt (nicht mehr Vollmond/EatMoreArt)
- Preise: 4,99 €/Monat oder 39,99 €/Jahr
- **3 Tage kostenlose Testphase** — auf der Startseite jetzt als eigener Button „3 Tage kostenlos testen" prominent (zusätzlich zum „Zur App →")

---

## Blog (`blog/`)

11 Artikel-Ordner (jeweils mit `index.html`):
1. `darmverschluss/`
2. `warum-wenig-essen/`
3. `sport-histamin-mcas/`
4. `blaehbauch-in-griff/`
5. `auf-koerper-hoeren/`
6. `enttaeuscht-von-aerzten/`
7. `frische-diagnose/`
8. `gym-transformation/`
9. `weg-aus-depressionen/`
10. `angst-vor-essen/`
11. `orthorexie-corona/`

Alle Artikel enden mit CTA zur TerraLuna-App oder Masterclass.

---

## Info-Seiten (kein Blog)

Kürzere, „lexikalische" Seiten:
- `histaminintoleranz.html` (mit „Wie ich bei Histamin reagiere"-Sektion)
- `mcas.html`
- `reizdarm.html`
- `pms.html`
- `angststoerung.html`

---

## Bilder

**Julias Portraits (Kleid-blaues Foto in Piran):**
- `ebook-reisen/bilder/Header-Startseite.jpg` — Rückenansicht ganzer Körper blaues Kleid Piazza (Julia's Signature-Bild)
- `ebook-reisen/bilder/IMG_4680.jpg` — Portrait Rückenansicht blaues Kleid Sonnenuntergang
- `images/neu-2026-08/IMG_3639.jpg` — Portrait Julia vor Barock-Tür (lila Top)
- `images/neu-2026-08/IMG_3545.jpg` — Portrait lila Kleid im Park (NICHT für „blaues Kleid" nutzen!)

**Blumen-/Reise-Motive:**
- `images/neu-2026-08/IMG_3835.jpg` — Rosa Oleander bei Nacht mit Palme (Pfingstrosen-Ersatz)
- `images/neu-2026-08/IMG_3738.jpg` — Rosa Bougainvillea an Steinmauer mit Treppe
- `images/pfingstrosen/IMG_7461.jpg` + `IMG_7460.jpg` — echte Pfingstrosen (auf Startseite Themen-Deko)

**Cover-Bilder:**
- Die Probe: `ebook-reisen/bilder/Titelbild.PNG` ✓
- Seelenbauchbuch + Iss dich stabil: **noch Placeholder** — Julia muss echte Cover liefern

---

## Rechtstexte

Alle auf Stand September 2026:
- **`agb.html`** — mit § 5a Histamin Masterclass Standard und § 5c Herbstspecial 2026 (rechtssicher: Ratenzahlung, Ausfallregelung, Starterpaket-Klausel nur für Mittel/VIP, versiegelte Lebensmittel nach § 312g Abs. 2 Nr. 4 BGB)
- **`datenschutz.html`** — mit WhatsApp-Sonntags-Check-in, Videokonferenz-Anbieter (Zoom/Meet/WhatsApp-Video), Calendly, keine Tally/WYH-Reste mehr
- **`widerruf.html`** — mit 14-Tage-Regel für Masterclass + Peer-Support-Gespräche-Storno + Muster-Widerrufsformular
- **`impressum.html`** — Standard

WYH („Wear Your Healing")/Seelenbauch-Coaching-Alttexte wurden aus allen Rechtstexten entfernt.

---

## Was NIE gemacht wird

- Heilversprechen
- Ärzte namentlich negativ nennen
- KI-glattgebügelte Sprache in Julias Texten (nur Rechtschreibung/Grammatik/Kommas korrigieren — Formulierung bleibt Julia)
- Perfekt-balancierte Dreier-Listen („gesund, glücklich und ausgeglichen")
- Werbe-Adjektive stapeln
- Force-Push auf `main`
- Bindestriche (em-dashes) in Julias Texten — sie mag die nicht und lässt sie durchgehend rausnehmen

---

## Was gerade offen ist

### Content
- [ ] **Cover-Bilder** für Seelenbauchbuch + Iss dich stabil (aktuell Placeholder) — Julia liefert
- [ ] Konkrete Snacks im **Überraschungspaket** in AGB § 5c.5 benennen (optional)
- [ ] Julia-Prosa für die 8 Wochen-Detail-Pages (falls diese auf juliabergles.de kommen — sonst nur auf Vercel)

### Vercel-Masterclass (in `~/Projects/terra-luna-masterclass`)
- [ ] Anmeldeformular auf 5 Optionen erweitern (Prompt in `PROMPTS.md` dort)
- [ ] Kursbereich mit Cards + Live-Calls + Notizen (Prompt 3 in `PROMPTS.md` dort, State-Persistenz via Supabase)
- [ ] Wochenthemen visuell schöner (aktuell Warmbeige-Accordion, könnte Bilder pro Woche vertragen)
- [ ] Digistore24-Integration für automatisierte Zahlung (aktuell Julia manuell)

### juliabergles.de
- [ ] `assets/site-v4.css` entweder löschen oder als optionalen Alt-Style dokumentieren
- [ ] Instagram + Schulen (aktuell nur direkt per URL erreichbar, nicht mehr im Nav) — evtl. im Footer prominenter

---

## Feedback-Regeln aus laufenden Sessions

- **Julia's Prosa gehört Julia.** Nur Rechtschreibung glätten, nicht umformulieren.
- **Bindestriche (em-dashes) werden systematisch entfernt** — Julia lässt sie durchgehend rausnehmen, sie mag sie nicht.
- **Deploy = git push, direkt** — keine Preview-Umgebung, Julia testet live am Handy.
- **Commit-Messages auf Deutsch, kurz.**
- **Direkt handeln, nicht endlos fragen.** Bei Unklarheit EINE knappe Frage im Fließtext.
- **Kein Anfassen ohne zu lesen.** Erst verstehen was existiert, dann ändern.
