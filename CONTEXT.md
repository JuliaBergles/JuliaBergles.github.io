# juliabergles.de — Kontext & Plan

> Was diese Website ist, wo sie hin soll, was gerade in Arbeit ist.
> Bei jeder Session zuerst hier reinschauen.
> Letzte Aktualisierung: 2026-09-22

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
| Zweck | Persönliche Marke, Blog, E-Books, App-Info, Peer-Support, **Masterclass-Sales-Landing** | Masterclass **Anmeldung + Kursbereich (Dashboard)** |
| Repo | `github.com/JuliaBergles/JuliaBergles.github.io` | `github.com/JuliaBergles/terra-luna-masterclass` |
| Lokal | `~/Library/Mobile Documents/com~apple~CloudDocs/juliabergles Website/` | `~/Projects/terra-luna-masterclass/` |
| Stack | Statische HTML + `assets/site-v3.css` | Next.js 16 + Tailwind v4 + Supabase (Auth+DB) + Vercel |
| Deploy | `git push` → GitHub Pages | `git push` → Vercel auto-deploy |

Verlinkung: `histamin-masterclass.html` auf juliabergles.de ist seit 2026-09-20 eine **echte Editorial-Landing** (15 Sektionen, Preise, FAQ, Warteliste) — nicht mehr nur Redirect. CTAs zeigen aktuell auf `mailto:julia@bergles.net` (Betreff pro Paket) und WhatsApp — der Vercel-Checkout kann später verlinkt werden. Der Nav-Link „Masterclass ★" führt zur juliabergles.de-Landing; separater CTA-Button rechts zeigt weiter direkt auf Vercel.

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
| 02 | **Das Seelenbauchbuch** (138 S. Leitfaden Unverträglichkeiten) | **24,99 € Softcover-Magazin (A5, zzgl. DHL 6,99 €) · 9,99 € E-Book** | verfügbar, Cover + Magazin-Preview (12 Seiten in `images/seelenbauchbuch/`) |
| 03 | **Iss dich stabil** (Ernährungsleitfaden) | 19,99 € | verfügbar, **Placeholder-Cover** |
| 04 | Zyklus-Leitfaden | 1,99 € | verfügbar |
| 05 | Freebie „Histamin & Ängste der Familie erklären" | kostenlos | in Arbeit |
| 06 | So wird man seine Ängste los | 14,99 € | in Arbeit |
| 07 | Was Depressionen mit einem machen | 14,99 € | in Arbeit |
| 08 | Live Calls (Format) | 32 €/Call | verfügbar |

**Kein KI-Text · kein Coach-Sprech**-Formulierungen wurden auf Julias Wunsch entfernt. Ersetzt durch „Von einer Betroffenen. Für Betroffene."

**Content-Regel:** die zwei E-Books Seelenbauchbuch + Iss dich stabil zeigen nur eine **Inhaltsliste**, keinen Verkaufstext (Julia's Ansage: „Leseprobe/Inhalt statt Direkttext").

---

## Histamin Masterclass — beide Sites synchron

### Landing (Sales) auf juliabergles.de/histamin-masterclass.html

Editorial-Landing mit 15 durchgehend nummerierten Sektionen (Nº 01–15):

1. Hero („Histamin verstehen. Deinen Körper verstehen. Wieder mehr Vertrauen entwickeln.") + Meta-Bar (Start 01.10., Ratenzahlung, 4 VIP-Plätze)
2. Nº 01 · Problem („Vielleicht kennst du das" — 16 Punkte)
3. Nº 02 · Was du lernst (8 Themenkarten mit Emoji + Nummer)
4. Nº 03 · Dein individueller Bereich (5 App-Karten in Mint)
5. Nº 04 · 8 Wochen im Überblick (4×2-Grid, je Woche mit Kurzbeschreibung)
6. Nº 05 · Das bekommst du (16-Punkte-Checkliste)
7. Nº 06 · Bewegung + Pull-Quote „regenerieren statt aushalten"
8. Nº 07 · Ernährung + „stabilisieren→erweitern"-Flow
9. Nº 08 · Zu wenig essen + Karte „weniger essen macht alles schlimmer"
10. Nº 09 · Mehr Vielfalt („von 5 Lebensmitteln auf lange Liste")
11. Nº 10 · Meine Geschichte (Story-Block, 31 kg, Darmverschluss, „heute nahezu beschwerdefrei")
12. Nº 11 · Warum es dir wert ist (Value-Sektion)
13. Nº 12 · Deine Optionen (3 Preiskarten + Warteliste + Seelenbauchbuch-Alternative)
14. Nº 13 · Terra Luna (in Blau)
15. Nº 14 · FAQ (19 Fragen als Accordion)
16. Nº 15 · Abschluss („Bereit für deinen Weg?") + Disclaimer

CTAs: `mailto:julia@bergles.net` mit Betreff pro Paket + WhatsApp `+49 1511 8515394` für Warteliste.

### Preise / Pakete (Herbstspecial 2026, feste Kohorte 01.10.–01.12.)

| Paket | Preis | Rate | Kern-Inhalt |
|---|---|---|---|
| **Klein · Starter-Kurs** | **325 €** (statt 399 €) | 3 × 115 € = 345 € | Wochenmodule im Dashboard oder als gedrucktes Buch zum Ausfüllen, alle E-Books, App 4 Mo, Community, Sonntags-Impuls, Start-/Abschluss-Call mit Julia (je 30–45 Min), WhatsApp-Kontakt für Fragen |
| **Mittel · max. 6** | **699 €** | 3 × 245 € = 735 € | Klein-Basis + 1 Austausch-Call in der Gruppe + 1× Live-Kochen + 1× gemeinsames Einkaufen + Notizbuch/Überraschungspaket per Post |
| **VIP · max. 4** | **825 €** (statt 899 €) | 3 × 285 € = 855 € | Mittel-Basis + 1 Austausch-Call + 1× Live-Kochen + **2 persönliche 1:1-Calls mit Julia** + 2 Kohorten-Calls (Start & Abschluss) + persönlicher Sonntags-Wochenplan mit Einkaufsliste + Ernährungsplan + Notizbuch/Überraschung |

**Streichpreise:** Klein „statt 399" ist rechtlich sauber (der 399 €-Preis stand tatsächlich vor der Reduktion im AGB). VIP „statt 899" ist Marketing-Anker — 899 € war nie realer Preis. Rechtlich angreifbar unter § 11 PreisAngV, wenn jemand es hinterfragt.

### Standard-Angebot (jederzeit, § 5a AGB)

- **Self-Study 399 €** (3 × 139 €) — 8 Wochenmodule, App 8 Wochen, E-Books, Community, Sonntags-Impuls
- **1:1 mit Julia 780 €** (3 × 275 € = 825 € gesamt) — Masterclass Online oder gedrucktes Arbeitsbuch, alle E-Books, App, persönlicher Wochenplan + Einkaufsliste + Rezepte, WhatsApp-Support mit Sprachnachrichten, **1 Kennenlerncall (60 Min) + 1 Abschlusscall (60 Min) + 2 persönliche Austausch-Calls + 1 gemeinsame Live-Koch-Session**. Max. 3 Plätze parallel.

### Was auf juliabergles.de passiert (Rechtstexte)

- **AGB § 5a** — Standard-Masterclass (Self-Study 399 € + 1:1 780 €)
- **AGB § 5c** — Herbstspecial 2026 (3 Pakete, feste Kohorte, Ratenzahlung, Ausfallregelung)
- **AGB § 5c.5** — Physischer Versand: Notizbuch/Überraschungspaket für Mittel/VIP + optionales Arbeitsbuch für Klein (§ 312g Abs. 2 Nr. 1 BGB — individuell gebundenes Werk, Widerruf nach Versand ausgeschlossen)
- **Datenschutz** — WhatsApp-Sonntags-Check-in, Videokonferenz-Anbieter für 1:1, Calendly
- **Widerruf** — Masterclass: 14 Tage, erlischt bei Zugriff auf digitale Inhalte; Peer-Support-Gespräche: 24-h-Storno

### Vercel-Site (Anmeldung + Kursbereich)

Weiterhin unter `terra-luna-masterclass.vercel.app`:
- `/` — kompakte Landing (Marquee, „Zwei Wege"-Sektion, Standard 2-Karten Self-Study/1:1, Herbstspecial 3-Karten Klein/Mittel/VIP)
- `/anmeldung` — Anmeldeformular (aktuell nur Self-Study, muss auf 5 Varianten erweitert werden)
- `/masterclass` — späterer Kursbereich (Dashboard mit Wochenkarten, Live-Calls-Übersicht, Notizen — noch in Arbeit)

**Zentrale Preis-Config:** `src/lib/variants.ts` — alle Preise, Raten, Capacity und Kurz-Infos einer Stelle. Beim Ändern immer beide Sites synchron halten (juliabergles.de/histamin-masterclass.html + juliabergles.de/agb.html + Vercel `variants.ts` + Vercel `page.tsx`).

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
- Seelenbauchbuch: Cover + 12-Seiten-Magazin-Preview vorhanden (`images/seelenbauchbuch/1.jpg`–`12.jpg`) — geliefert 2026-09-23
- Iss dich stabil: **noch Placeholder** — Julia muss echtes Cover liefern

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
- [x] Cover + Preview für Seelenbauchbuch — geliefert 2026-09-23
- [ ] **Cover-Bild** für Iss dich stabil (aktuell Placeholder) — Julia liefert
- [ ] Konkrete Snacks im **Überraschungspaket** in AGB § 5c.5 benennen (optional)
- [ ] Julia-Prosa für die 8 Wochen-Detail-Pages (falls diese auf juliabergles.de kommen — sonst nur auf Vercel)
- [ ] **Masterclass-Screenshots** für die Landing (juliabergles.de/histamin-masterclass.html) — Julia macht 3–5 Screenshots vom Dashboard, einer Woche, Wochenplan/Einkaufsliste, Rezept-Screen und legt sie in `images/masterclass/`. Dann baue ich eine „So sieht der Kurs von innen aus"-Sektion (Editorial-Grid).

### Vercel-Masterclass (in `~/Projects/terra-luna-masterclass`)
- [ ] Anmeldeformular auf 5 Optionen erweitern (Prompt in `PROMPTS.md` dort)
- [ ] Kursbereich mit Cards + Live-Calls + Notizen (Prompt 3 in `PROMPTS.md` dort, State-Persistenz via Supabase)
- [ ] Wochenthemen visuell schöner (aktuell Warmbeige-Accordion, könnte Bilder pro Woche vertragen)
- [ ] Digistore24-Integration für automatisierte Zahlung (aktuell Julia manuell)
- [ ] Julia hat parallel Änderungen an `dashboard-client.tsx`, `weeks.ts`, `week-cards.tsx` — unstaged (nicht anfassen ohne Nachfrage)

### juliabergles.de
- [ ] `assets/site-v4.css` entweder löschen oder als optionalen Alt-Style dokumentieren
- [ ] Instagram + Schulen (aktuell nur direkt per URL erreichbar, nicht mehr im Nav) — evtl. im Footer prominenter
- [ ] **Masterclass-Landing-CTAs:** aktuell alle auf `mailto:` — evtl. auf Vercel-Anmeldeformular umbiegen, sobald das die 5 Varianten kann
- [ ] **Streichpreis „statt 899" bei VIP** rechtlich sauber machen (aktuell nur Marketing-Anker) oder streichen — siehe § 11 PreisAngV

---

## Feedback-Regeln aus laufenden Sessions

- **Julia's Prosa gehört Julia.** Nur Rechtschreibung glätten, nicht umformulieren.
- **Bindestriche (em-dashes) werden systematisch entfernt** — Julia lässt sie durchgehend rausnehmen, sie mag sie nicht.
- **Deploy = git push, direkt** — keine Preview-Umgebung, Julia testet live am Handy.
- **Commit-Messages auf Deutsch, kurz.**
- **Direkt handeln, nicht endlos fragen.** Bei Unklarheit EINE knappe Frage im Fließtext.
- **Kein Anfassen ohne zu lesen.** Erst verstehen was existiert, dann ändern.
