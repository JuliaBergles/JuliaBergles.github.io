# juliabergles.de — Kontext & Plan

> Was diese Website ist, wo sie hin soll, was gerade in Arbeit ist.
> Bei jeder Session zuerst hier reinschauen.
> Letzte Aktualisierung: 2026-09-25 (Vercel-Design-Iterationen + Rolling-Entry zurück)

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
| Zweck | Persönliche Marke, Blog, Bücher, App-Info, Peer-Support, **Kurs-Sales-Landing** | Kurs **Anmeldung + Kursbereich (Dashboard)** |
| Repo | `github.com/JuliaBergles/JuliaBergles.github.io` | `github.com/JuliaBergles/terra-luna-masterclass` |
| Lokal | `~/Library/Mobile Documents/com~apple~CloudDocs/juliabergles Website/` | `~/Projects/terra-luna-masterclass/` |
| Stack | Statische HTML + `assets/site-v3.css` | Next.js 16 + Tailwind v4 + Supabase (Auth+DB) + Vercel |
| Deploy | `git push` → GitHub Pages | `git push` → Vercel auto-deploy |

Verlinkung: `histamin-masterclass.html` (Dateiname bleibt aus URL-Stabilitätsgründen) ist die Editorial-Landing für den **Histamin Seelenbauch Kurs** (15 Sektionen, Preise, FAQ, Warteliste). CTAs zeigen aktuell auf `mailto:julia@bergles.net` (Betreff pro Paket) und WhatsApp. Der Nav-Link „Kurs ★" führt zur juliabergles.de-Landing; separater CTA-Button rechts zeigt weiter direkt auf Vercel.

---

## Aktueller Design-Stand (juliabergles.de)

**Design-System v3 — Editorial (Cormorant + Manrope):**

- Fonts: **Cormorant Garamond** (Headlines, weight 400) + **Manrope** (Body/UI)
- Zentrales Stylesheet: `assets/site-v3.css`
- v4 wurde probiert, dann per Rollback wieder auf v3 zurück. `assets/site-v4.css` liegt noch da, wird aber nicht mehr gebunden.

**Farbwelt aktuell:**
- Basis: Cream `#fffcf9`, Beige `#f4ede4`, Dark `#2a2a2a`, Mute `#8a8a8a`
- Warm: Copper `#c48b6c`, Copper-Dark `#a87556`
- Kühl: Blau `#8790c1` / Blau-Dark `#6f78a8`, Mint `#e2fffe`
- Kleid-Blau (aus Julias PDF-Bild): `#2a4a68` dunkel, `#bec2d9` gedeckt
- Kein Bordeaux/Grün mehr (Zyklus-Leitfaden hat der Bordeaux-BG abgelegt → beige)

**Buttons:**
- **`.btn-kleidblau`** — Kleid-Blau BG `#2a4a68` + weiße Schrift (primärer CTA auf Startseite)
- **`.btn-copper`** — jetzt Warmbeige `#e1ded5` mit dunkler Schrift
- **`.btn-outline`** — transparent mit dark Border

**Marquee (Ticker unter Nav):** Kleid-Hellblau `#bec2d9` mit dunkelblauer Schrift

---

## Nav (aktuell auf allen aktiven Seiten)

```
Über mich  |  Themen ▾  |  Rezepte ▾  |  Kurs ★ ▾  |  App  |  Bücher ▾  |  Mehr ▾    [Kurs ★]
```

- **Themen ▾**: Histamin · MCAS · Reizdarm · PMS & Zyklus · Angststörung · Selbsttest · Blog
- **Rezepte ▾**: Übersicht + 6 Kategorien
- **Kurs ★ ▾**: Zum Kurs · Anmeldung
- **App**: direkt zu `app.html` (TerraLuna App-Landing)
- **Bücher ▾** (früher E-Books): Übersicht · **E-Books** (Histaminarm Reisen, Seelenbauchbuch) · **Softcover Bücher** (Seelenbauchbuch) — Dropdown mit Unter-Kategorien via `.dropdown-header` CSS
- **Mehr ▾**: Live Calls · 1:1 Gespräch · Empfehlungen · Kunst
- **CTA rechts**: „Kurs ★" führt aktuell zu Vercel

---

## Startseite (index.html) — Sektionsfolge

1. Nav
2. Marquee (jetzt „★ NEU · Histamin Seelenbauch Kurs · 12 Wochen")
3. **Call-CTA-Banner** oben: Kleid-Hellblau, „Neu · Mein Histamin Seelenbauch Kurs ist da." → Vercel-Link
4. Hero (Full-Bleed Bild von Julia im blauen Kleid Piran, kein Filter)
5. **„Kennst du das?"** Pain-Sektion
6. Themen-Sektion mit Pfingstrosen-Deko + 6 Copper-Karten
7. Full-Bleed IMG_4680
8. Blog-Sektion
9. **Kurs-Herzstück** — Verweis auf Vercel-Landing bzw. `histamin-masterclass.html`
10. Bücher & Community
11. Empfehlungen
12. App
13. Gespräch/Peer-Support
14. Footer

---

## Bücher (`ebooks.html`)

Seite heißt jetzt **„Bücher"** (nicht mehr „E-Books"). Bestellung weiterhin per Mail-Vorkasse. Aktueller Katalog:

| Nº | Titel | Preis | Status |
|---|---|---|---|
| 01 | Die Probe (Reisen mit Histamin) | 7,99 € | verfügbar, echtes Cover |
| 02 | **Das Seelenbauchbuch — Der Weg zurück zu deinem Seelenbauch** (144 S., Magazin-Stil, Seelenrezepte, Reflexionsfragen) | **24,99 € Softcover-Magazin · 9,99 € E-Book** | verfügbar, **aktuell 12 Stück auf Lager**, Cover + 12-Seiten-Preview + Quell-Bilder in `images/seelenbauchbuch/` |
| 03 | Zyklus-Leitfaden | **Freebie · kostenlos** (vorher 1,99 €) | verfügbar, warmer beige Look |
| 04 | Freebie „Histamin & Ängste der Familie erklären" | kostenlos | in Arbeit |
| 05 | So wird man seine Ängste los | 14,99 € | in Arbeit |
| 06 | Was Depressionen mit einem machen | 14,99 € | in Arbeit |
| 07 | Live Calls (Format) | 32 €/Call | verfügbar |

**Iss dich stabil** wurde am 24.09. auf Julias Wunsch vorerst entfernt („kannst du erstmal rausnehmen"). Kann später zurück.

**Seelenbauchbuch-Versand (neue Regelung):**
- Innerhalb Deutschlands **3,60 €** (statt vorher 6,99 € DHL)
- **Ab 30 € Bestellwert kostenlos**
- App-Kunden bekommen Versand kostenlos gegen Screenshot aus der App (egal welches Abo)

**Content-Regel:** die zwei Verkaufs-Bücher (Seelenbauchbuch + Iss dich stabil, falls wieder aktiv) zeigen nur eine **Inhaltsliste**, keinen Verkaufstext.

**Nav-Dropdown „Bücher"** verlinkt Übersicht + E-Books (Histaminarm Reisen, Seelenbauchbuch) + Softcover Bücher (Seelenbauchbuch als gedrucktes Magazin).

---

## Histamin Seelenbauch Kurs

**Wichtig:** Der Kurs wurde am 23.09.–24.09. komplett umstrukturiert. Aktueller Stand:

- **Name:** „Histamin Seelenbauch Kurs" (Dateiname `histamin-masterclass.html` bleibt aus URL-Stabilitätsgründen — auf der Website taucht das Wort „Masterclass" nirgends mehr auf)
- **Dauer:** 12 Wochen (3 Monate), davon **10 Wochenmodule + 2 Wochen Pause** (davon Weihnachten 24.12. – 01.01.2027)
- **App:** 6 Monate kostenlos in allen Paketen (Early-Bird: 12 Monate)
- **Seelenbauchbuch:** als gedrucktes Softcover-Magazin (Warenwert 24,99 €) in **allen drei Paketen**
- **E-Books im Kurs:** nur **E-Book Histaminarm Reisen** — nicht mehr „Alle E-Books"
- **WhatsApp:** früher „WhatsApp-Community + Sonntags-Impuls" → **WhatsApp-Kontakt 24/7** (in allen Paketen)
- **Einkaufen** umbenannt zu **Einkaufs-Talk** (Julia zeigt Vorratskammer statt gemeinsam einzukaufen)
- **Preis-Karten** neu im Editorial-Look — Cream + blau-getönte Umrandung, Nº + Kategorie-Label getrennt, Preis mit Trennlinien, Serif-italic Fits-Zeile
- **Hero-Tagline:** „In 3 Monaten zu einem entspannteren Bauch."

### Paket-Namen (24.09. spät umgetauft von Klein/Mittel/VIP)

**Herbstkohorte (feste Kohorte 01.10.–01.01.):**
- **Nº 01 · Basic Kurs** — 325 € (statt 399 €) · 3 × 115 € · 6 × 58 € — Selbstlern-Dashboard
- **Nº 02 · Gruppenkurs** — 699 € · 3 × 245 € · 6 × 123 € — Kleingruppe max. 6
- **Nº 03 · Seelenbauch Kurs** — 825 € (statt 899 €) · 3 × 285 € · 6 × 143 € — max. 4 Plätze, mit 1:1

**Rolling Entry (Einstieg egal wann, seit 25.09. wieder aktiv):**
- **Self Study** — 399 € · 3 × 139 € · 6 × 70 € — reine Selbstlern-Variante
- **Seelenbauch 1:1** — 780 € · 3 × 275 € · 6 × 138 € — max. 4 Plätze parallel, mit 1:1

Auf der **juliabergles.de/histamin-masterclass.html Landing** werden aktuell nur die 3 Herbstkohorten-Pakete gezeigt. Rolling-Entry taucht nur im Vercel-Anmeldeformular auf (2. Fieldset).

### Landing auf juliabergles.de/histamin-masterclass.html

Editorial-Landing mit 16 nummerierten Sektionen (Nº 01–16). Hero-H1 bleibt „Histamin verstehen. Deinen Körper verstehen. Wieder mehr Vertrauen entwickeln." — der Kurs-Name „Histamin Seelenbauch Kurs" steht im Eyebrow, die Tagline drunter.

Sektionen: 01 Problem · 02 Was du lernst · 03 Persönlicher Bereich · 04 **10 Wochenmodule** im Überblick · 05 Das bekommst du · 06 Bewegung · 07 Ernährung · 08 Zu wenig essen · 09 Mehr Vielfalt · 10 Meine Geschichte · 11 Warum es dir wert ist · **12 Alle Termine (neu, 24.09.)** · 13 Deine Optionen (Preise + Early-Bird-Callout) · 14 Terra Luna · 15 FAQ · 16 Abschluss.

CTAs: `mailto:julia@bergles.net` mit Betreff pro Paket + WhatsApp `+49 1511 8515394` für Warteliste.

### Herbstspecial 2026 — feste Kohorte

**Zeitraum:** 01.10.2026 – 01.01.2027 (12 Kalenderwochen: 10 aktive Wochenmodule + 2 Pause-Wochen)
**Weihnachtspause:** 24.12.2026 – 01.01.2027 (bewusste Pause, keine Live-Termine, keine WhatsApp-Betreuung)

**Feste Kohorten-Termine** (auf der Landing als eigene Nº-12-Sektion mit Editorial-Tabelle; alle werden aufgezeichnet, Aufzeichnung dient als Ersatz bei Abwesenheit):

| Datum | Uhrzeit | Termin | Für |
|---|---|---|---|
| So 04.10.2026 | 10:00 | Start-Call · 30–45 Min | Kohorte (alle Pakete) |
| Sa 24.10.2026 | 18:30 | Einkaufs-Talk · Vorratskammer + Einkauf | Gruppenkurs + Seelenbauch Kurs |
| Sa 14.11.2026 | 18:30 | Austausch-Call | Gruppenkurs + Seelenbauch Kurs |
| Sa 28.11.2026 | 16:30 | Live-Kochen | Gruppenkurs + Seelenbauch Kurs |
| Sa 19.12.2026 | 18:30 | Abschluss-Call · 30–45 Min | Kohorte (alle Pakete) |

**Seelenbauch-Kurs 1:1-Calls:** 2 Stück, flexibel nach Absprache, **auch kurzfristig verlegbar** (weicher als Standard 24h-Storno).

### 10 Wochenmodule (Inhalt der „Nº 04"-Sektion)

1. Histamin verstehen · 2. Deine individuelle Situation · 3. Darm & Ernährung · 4. Lebensmittel integrieren · 5. Zyklus & Histamin · 6. Stress & Nervensystem · 7. Bewegung & Regeneration · 8. Dein persönlicher Fahrplan · **9. Angst vor Essen & innere Signale (neu)** · **10. Alltag, Familie & Reisen (neu)**

Module 9 und 10 sind Platzhalter mit sinnvollen Themen. Julia kann Titel/Beschreibung noch anpassen.

### Preise / Pakete (Detail)

| Paket | Preis | Rate | Early-Bird (erste 5) | Kern-Inhalt |
|---|---|---|---|---|
| **Nº 01 · Basic Kurs** | **325 €** (statt 399 €) | 3 × 115 € | **275 €** | 10 Wochenmodule als Selbstlern-Dashboard, **Seelenbauchbuch als gedrucktes Softcover (24,99 €)**, E-Book Histaminarm Reisen, App 6 Mo, WhatsApp-Kontakt 24/7, Start- + Abschluss-Call (je 30–45 Min) |
| **Nº 02 · Gruppenkurs** | **699 €** | 3 × 245 € | **649 €** | Basic-Basis + alle 5 Kohorten-/Gruppen-Termine (Start/Einkaufs-Talk/Austausch/Live-Kochen/Abschluss) + Notizbuch/Überraschungspaket per Post. Max. 6 Teilnehmerinnen. |
| **Nº 03 · Seelenbauch Kurs** | **825 €** (statt 899 €) | 3 × 285 € | **775 €** | Gruppenkurs-Basis + **2 persönliche 1:1-Calls mit Julia** (flexibel, auch kurzfristig verlegbar) + persönlicher Sonntags-Wochenplan mit Einkaufsliste + Ernährungsplan. Max. 4 Plätze. |

**Early-Bird ★:** Erste 5 Buchungen bekommen **Terra Luna App 12 Monate (statt 6) + 50 € Rabatt** auf den Herbstspecial-Preis. Callout-Box mit expliziten Preisen (275 / 649 / 775 €) direkt über den Preis-Karten. Legal in AGB § 5c.8.

**Streichpreise:** Basic „statt 399 €" ist rechtlich sauber (399 € stand im alten AGB). Seelenbauch Kurs „statt 899 €" ist Marketing-Anker — 899 € war nie realer Preis. Rechtlich angreifbar unter § 11 PreisAngV.

### AGB (24.09. komplett überarbeitet)

- **§ 1** — Kurs-Beschreibung mit 3 Paket-Namen (Basic Kurs, Gruppenkurs, Seelenbauch Kurs)
- **§ 5a** — Allgemeine Bestimmungen für alle drei Pakete (Buchung, Ratenzahlung, digitale Zugriffsdauer, WhatsApp-Kontakt 24/7, Sonntags-Impuls, Nutzungslizenz, Widerrufsrecht, Haftungsausschluss, Wechsel zwischen Paketen). Rolling Entry und alte 399/780 €-Preise entfernt.
- **§ 5c** — Herbstspecial 2026 mit festen Kohorten-Terminen (§ 5c.3 mit Aufzeichnungs-Regel + Weihnachtspause), Seelenbauchbuch als Softcover in Gruppenkurs + Seelenbauch Kurs (§ 5c.5), Ratenzahlung
- **§ 5c.8** — Early-Bird-Paragraph (erste 5 Buchungen, App 12 Monate + 50 € Rabatt, nach Zahlungseingang, nicht kombinierbar, nicht auszahlbar)

**Achtung:** AGB nicht von Anwalt geprüft — bei Gelegenheit prüfen lassen (besonders Widerrufsklauseln und Aufzeichnungs-Regel + „24/7"-Support-Wording vs. tatsächliche Erreichbarkeit).

### Vercel-Site (Landing + Anmeldung + Kursbereich)

Unter `terra-luna-masterclass.vercel.app`:
- `/` — Landing mit Pfingstrosen-Hintergrund, transparente weiße Karten (Basic → Seelenbauch Kurs = 45% → 92% Opazität), Rosé-Buttons, aufklappbare Termine pro Karte
- `/anmeldung` — Anmeldeformular mit 2 Sektionen (siehe unten)
- `/masterclass` — Kursbereich mit Modul-Dashboard (Julia arbeitet parallel dran)

**Design-Änderungen 25.09. (Vercel-Landing Herbstspecial-Sektion):**
- Vollflächiges Pfingstrosen-Hintergrundbild `IMG_7461.jpg` (kein Cream-Overlay)
- Weißer Text im Hero mit Text-Shadow (H2, Absätze, „HERBSTSPECIAL 2026")
- Karten transparent-weiß mit Backdrop-Blur, Opazitäts-Gradient Basic → Seelenbauch
- Karten in Glacial Indifference (Sans), nicht mehr Cormorant Serif
- Karten-Breite: **10 cm** (max-w-[1200px] für 3 Karten)
- Warteliste-Buttons + Early-Bird-Callout im **Rosé-Verlauf** (`--color-rose` + `--color-rosegold`)
- Termine pro Karte aufklappbar (`<details>` mit Rosé-Button „Termine ansehen ↓"), enthält Datum + Titel + Kurzbeschreibung + Dauer
- Keine separate Termine-Sektion mehr (steht alles in den Kartendetails)

**Anmeldeformular (25.09. neu strukturiert):**

Zwei Fieldsets zur Auswahl:

1. **Herbstkohorte · ab 01.10. bis 01.01.**
   - Basic Kurs — 325 €
   - Gruppenkurs · max. 6 — 699 €
   - Seelenbauch Kurs · max. 4 — 825 €

2. **Einstieg egal wann · Rolling Entry** (Standard-Programm ist zurück)
   - Self Study — 399 €
   - Seelenbauch 1:1 — 780 €

Jede Option zeigt nur **Name + Preis** — keine langen Inhaltsbeschreibungen mehr (war unübersichtlich).

**Zahlungsart** dynamisch für das gewählte Paket in 3 Optionen:
- Einmalzahlung
- Ratenzahlung 3 Monate (`raten3`)
- Ratenzahlung 6 Monate (`raten6`) — neu 25.09., Raten fair mit ~5% Uplift

Post-Adresse-Feld erscheint nur wenn Paket physischen Versand hat (alle außer Self Study).
Wunsch-Startdatum-Feld nur bei Rolling-Entry-Paketen.

**Zentrale Preis-Config:** `src/lib/variants.ts` — enthält `raten` (3M) + `raten6` (6M) + `raten6Gesamt` je Variante. Bei Preisänderungen immer beide Sites synchron halten (juliabergles.de/histamin-masterclass.html + agb.html + Vercel `variants.ts` + `page.tsx`).

---

## Peer-Support-Telefonate

- Kostenloses 15-Min Kennenlerngespräch (Calendly `julia-bergles/kennenlerngesprach`)
- 1-Stunden-Peer-Support-Gespräch: 39 € (Calendly `julia-bergles/gesprach-mit-julia`), inkl. PDF-Zusammenfassung
- Positionierung: **„Erfahrungsaustausch" / „Peer-Support"** — NIEMALS „Beratung" oder „Coaching" (Heilpraktiker-Gesetz)
- Disclaimer: „Ich teile meine eigene Erfahrung. Keine medizinische Beratung, kein Ersatz für Arzt/Therapeut."

---

## TerraLuna App

- Preise: 4,99 €/Monat oder 39,99 €/Jahr
- **3 Tage kostenlose Testphase**
- In allen Kurs-Paketen 6 Monate kostenlos, mit Early-Bird 12 Monate

---

## Blog (`blog/`)

11 Artikel-Ordner (jeweils mit `index.html`) — Themen: Darmverschluss, Warum wenig essen, Sport, Blähbauch, Auf Körper hören, Enttäuscht von Ärzten, Frische Diagnose, Gym-Transformation, Weg aus Depressionen, Angst vor Essen, Orthorexie/Corona. Alle enden mit CTA zur App oder zum Kurs.

---

## Ordner-Struktur (nach Cleanup 23.09.)

Root: nur HTML-Seiten, `CLAUDE.md`, `CONTEXT.md`, `CONTEXT-CONTENT.md`, `CNAME` + Asset-/Content-Ordner.

- **`docs/`** — alle Arbeits-MDs (Kalender, Konzepte, Design-Notizen, PLAN.md, Masterclass-Prompt, Kochbuch-Roadmap etc.)
- **`assets/`**, **`css/`**, **`images/`** — Website-Assets
- **`images/seelenbauchbuch/`** — Cover + 12-Seiten-Preview (JPGs) für die Website
- **`images/seelenbauchbuch/_quellen/`** — PNG-Quellbilder (cover-final.png + page-1.png bis page-12.png) für spätere Neuerstellung
- **`blog/`**, **`rezepte/`** — Content-Ordner
- **`ebook-*/`** — pro E-Book ein Ordner mit Bildern + arbeitsmappe.md

---

## Bilder

**Julias Portraits (Kleid-blaues Foto in Piran):**
- `ebook-reisen/bilder/Header-Startseite.jpg` — Signature-Bild
- `ebook-reisen/bilder/IMG_4680.jpg` — Piazza-Portrait
- `images/neu-2026-08/IMG_3639.jpg` — Portrait Barock-Tür (lila Top)

**Cover-Bilder:**
- Die Probe: `ebook-reisen/bilder/Titelbild.PNG` ✓
- Seelenbauchbuch: `images/seelenbauchbuch/cover.png` (neues Cover vom 24.09., ersetzt das alte 1.jpg) + 12-Seiten-Preview
- Zyklus-Leitfaden: **Placeholder** — Julia liefert Cover-Bild bei Gelegenheit
- Freebook „Familie" / „Ängste" / „Depressionen": Placeholder

---

## Rechtstexte

Alle auf Stand September 2026:
- **`agb.html`** — 24.09. komplett auf 3-Paket-Struktur ausgerichtet, § 5a Allgemeine Bestimmungen + § 5c Herbstspecial + § 5c.8 Early-Bird
- **`datenschutz.html`** — WhatsApp-Sonntags-Check-in, Videokonferenz, Calendly
- **`widerruf.html`** — 14-Tage-Regel Kurs + Peer-Support-Storno + Muster-Widerrufsformular
- **`impressum.html`** — Standard

---

## Was NIE gemacht wird

- Heilversprechen
- Ärzte namentlich negativ nennen
- KI-glattgebügelte Sprache in Julias Texten (nur Rechtschreibung/Grammatik/Kommas korrigieren — Formulierung bleibt Julia)
- Perfekt-balancierte Dreier-Listen
- Werbe-Adjektive stapeln
- Force-Push auf `main`
- Bindestriche (em-dashes) systematisch — Julia mag sie nicht

---

## Was gerade offen ist

### Content
- [ ] **Cover-Bild für Zyklus-Leitfaden** (aktuell Placeholder) — Julia liefert
- [ ] **Zyklus-Leitfaden Inhalt** — Julia hat ein Zip im Ordner `E-Book Zyklus und Histamin/` gedroppt (nicht committet). Wenn Julia will, entpacken und einbauen.
- [ ] Konkrete Snacks im **Überraschungspaket** in AGB § 5c.5 benennen (optional)
- [ ] **Kurs-Screenshots** für Landing (histamin-masterclass.html) — Julia macht 3–5 Screenshots vom Dashboard etc. und legt sie in `images/masterclass/`
- [ ] Uhrzeiten für Austausch-Call 14.11. und Abschluss-Call 19.12. sind fix (jeweils 18:30) — Uhrzeit für Start-Call 04.10. ist 10 Uhr

### Vercel (in `~/Projects/terra-luna-masterclass`)
- [ ] Anmeldeformular auf 3 aktuelle Pakete (Klein/Mittel/VIP) umstellen — Self-Study/1:1 sind Legacy
- [ ] Preise aktualisieren (325/699/825 + Early-Bird)
- [ ] Kursbereich mit Cards + Live-Calls + Notizen
- [ ] Digistore24-Integration für automatisierte Zahlung
- [ ] Julia hat parallel Änderungen an `dashboard-client.tsx`, `weeks.ts`, `week-cards.tsx` — unstaged (nicht anfassen ohne Nachfrage)

### juliabergles.de
- [ ] `assets/site-v4.css` löschen oder als Alt-Style dokumentieren
- [ ] **Kurs-Landing-CTAs** aktuell alle auf `mailto:` — evtl. auf Vercel-Anmeldeformular umbiegen (das kann jetzt alle 5 Pakete)
- [ ] **Streichpreis „statt 899" bei VIP** rechtlich sauber machen oder streichen (§ 11 PreisAngV)
- [ ] AGB rechtlich von Anwalt prüfen lassen (Widerrufs- und Aufzeichnungsklauseln)
- [ ] AGB muss um Self Study (399 €) und Seelenbauch 1:1 (780 €) ergänzt werden — Rolling-Entry ist wieder aktiv
- [ ] Uhrzeit für Start-Call vs. andere Termine harmonisieren? Start 10 Uhr fällt aus dem 18:30-Schema — vielleicht auch 18:30 nachziehen? (Julia entscheidet)

---

## Feedback-Regeln aus laufenden Sessions

- **Julia's Prosa gehört Julia.** Nur Rechtschreibung glätten, nicht umformulieren.
- **Bindestriche (em-dashes) werden systematisch entfernt** — Julia lässt sie durchgehend rausnehmen.
- **Deploy = git push, direkt** — keine Preview-Umgebung, Julia testet live am Handy.
- **Commit-Messages auf Deutsch, kurz.**
- **Direkt handeln, nicht endlos fragen.** Bei Unklarheit EINE knappe Frage im Fließtext.
- **Kein Anfassen ohne zu lesen.** Erst verstehen was existiert, dann ändern.
- **Julia gibt Termine/Zeiten oft schrittweise** — nachfragen nur wenn etwas komplett fehlt, sonst sinnvoll defaulten und Julia korrigiert bei Bedarf.
