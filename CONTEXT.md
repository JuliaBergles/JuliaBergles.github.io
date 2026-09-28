# juliabergles.de — Kontext & Plan

> Was diese Website ist, wo sie hin soll, was gerade in Arbeit ist.
> Bei jeder Session zuerst hier reinschauen.
> Letzte Aktualisierung: 2026-09-28 mittags (Redesign + Verkaufs-Fokus). **Kernwechsel:**
> - Headlines von Cormorant fein → **Manrope Bold 700-800** (dick, moderner). Italic-Akzente in Headlines bleiben Cormorant für Editorial-Kontrast, aber `p em` + `chapter-num` + `.lead` sind jetzt Sans-Bold statt schnörkelig-Serif-Italic.
> - **Copper (braun) → Malaga (Weinrot `#8B2E3E`)** als Akzent-Farbe global.
> - **Blau als BG überall raus** — Kleid-Blau, Mint, `section-blue`, `section-mint`, `.editorial-card.blue-soft`, Marquee, Call-CTA-Banner, Themen-Kacheln → alle auf **Beige/Dark** umgestellt.
> - **Instagram-Post-Stil** für Themen-Sektion (Startseite) + Kategorien-Grid (Rezepte-Seite): großes Bild als Full-Bleed-BG, weiße transparente Karten mit Backdrop-Blur.
> - **Startseite Verkaufs-Sektion „Was ich dir anbieten kann"** direkt nach Pain-Sektion: Julias Story-Headline „Vom Darmverschluss und 5 Lebensmitteln zurück zu mir. Endlich bin ich wieder ich." + 3 Angebot-Karten (Seelenbauchbuch, Seelenbauch Kurs featured, TerraLuna App).
> - **Bücher-Übersicht neu:** 3-Card-Grid (alle gleich hoch), Seelenbauchbuch als Fokus mit Malaga-Border, Zyklus-Leitfaden als **kostenloser WhatsApp-Freebie Lead-Magnet** (Button öffnet `wa.me/4915118515394` mit vorformatierter Nachricht).
> - **App-Seite:** 8 Feature-Sektionen (je Grid-2 mit Screenshot) → kompaktes 4-Spalten-Feature-Grid mit Phone-Mockups.
> - **Live Calls aus Nav auf 87 Seiten entfernt** (Datei bleibt, kann reaktiviert werden). Fokus jetzt: Buch + Kurs + App.
> - **Nav-Links „Zum Kurs" + „Anmeldung"** zeigen auf `terra-luna-masterclass.vercel.app` statt lokal.
> - **8 neue Rezepte** eingebaut + 7 Rezept-Fotos + Einfrier-Disclaimer.
> - Neue Portrait-Bilder: Über-mich Hero (`hey-ich-bin-julia.jpg` Nachtstraße + 2. Bild `hey-julia-2.jpg` Brille/Jeansjacke), Startseite Blähbauch-Blog-Kachel + Empfehlungen-Sektion mit Kroatien-Brillen-Bildern (Nahaufnahme + Straßenbild). Piran-Hero-Bild richtig gedreht.

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

**Design-System v3.5 — Editorial modern (Manrope Bold + Malaga-Akzent, ab 28.09.):**

- **Fonts:** Headlines auf **Manrope 700-800** (Sans Bold, dick statt fein). Italic-Akzente `<em class="italic">` in Headlines bleiben **Cormorant Garamond Italic** für editorial Kontrast. In Fließtexten (`p em`, `.lead em`, `.chapter-num`) auch Sans-Bold statt Cormorant. Body 18px + Lead 22-28px für Leserlichkeit.
- Zentrales Stylesheet: `assets/site-v3.css`
- Julia hatte Glacial Indifference gewünscht — nicht als OTF verfügbar (GitHub-Repo tot). Manrope Bold als ~95%-Alternative.

**Farbwelt aktuell (Malaga-Wechsel 28.09.):**
- Basis: Cream `#fffcf9`, Beige `#f4ede4`, Dark `#2a2a2a`, Mute `#8a8a8a`
- **Akzent (neu): Malaga `#8B2E3E` / Malaga-Dark `#6D2732`** — ersetzt das alte Copper-Braun. `--copper` und `--malaga` zeigen jetzt auf denselben Wert (Weinrot/Bordeaux).
- Kein Blau mehr als BG. Blau-Tokens `--blue`, `--mint` sind noch definiert, aber alle Sektions-Klassen (`section-blue`, `section-mint`, `.editorial-card.blue-soft`) sind auf Beige umgestellt.
- Kleid-Blau `#2a4a68` / `#bec2d9` überall raus, ersetzt durch Dark und Beige.

**Buttons:**
- **`.btn-kleidblau`** — jetzt **Dark Grey** (`--dark` `#2a2a2a`) statt Kleid-Blau. Primärer CTA-Button.
- **`.btn-copper`** — Warmbeige `#e1ded5` mit dunkler Schrift.
- **`.btn-outline`** — transparent mit dark Border.
- **Weißer transparenter Button** (Instagram-Style): auf dunklen Section-BGs, mit Backdrop-Blur.

**Marquee:** Beige `--beige` mit Dark-Schrift (statt Kleid-Hellblau).

---

## Nav (vereinheitlicht auf allen 88 Seiten seit 28.09.)

```
Über mich  |  Themen ▾  |  Rezepte ▾  |  Kurs ★ ▾  |  App  |  Bücher ▾  |  Mehr ▾    [Seelenbauch Kurs]
```

- **Themen ▾**: Histamin · MCAS · Reizdarm · PMS & Zyklus · Angststörung · Selbsttest · Blog
- **Rezepte ▾**: Übersicht · Frühstück · Snacks · Vorspeisen · Salate · Warme Mahlzeiten · Mealprep · Süßes · Gebäck · Hüttenkäse
- **Kurs ★ ▾**: Zum Kurs · Anmeldung — beide führen jetzt auf **Vercel** (`terra-luna-masterclass.vercel.app` / `/anmeldung`), nicht mehr auf lokale `histamin-masterclass.html` / `masterclass-anmeldung.html`
- **App**: direkt zu `app.html` (TerraLuna App-Landing)
- **Bücher ▾**: Übersicht · **E-Books** (Histaminarm Reisen, Seelenbauchbuch) · **Softcover Bücher** (Seelenbauchbuch)
- **Mehr ▾**: 1:1 Gespräch · Empfehlungen · Kunst (**Live Calls raus seit 28.09.**, Datei bleibt)
- **CTA rechts:** „Seelenbauch Kurs" → Vercel

**Nav-Vereinheitlichung (28.09.):** Die Rezept-Unterseiten hatten eine alte „Diagnosen + Masterclass"-Nav. Jetzt haben alle 88 HTML-Files die identische Master-Nav aus `index.html` (mit korrektem Pfad-Prefix je Tiefe). Auf allen Seiten identisch — kein Nav-Wechsel beim Klick zu anderer Sektion mehr. „Masterclass" im sichtbaren Text global durch „Seelenbauch Kurs" ersetzt (URLs bleiben).

---

## Startseite (index.html) — Sektionsfolge (Stand 28.09.)

1. Nav (CTA rechts: „Seelenbauch Kurs" → Vercel)
2. Marquee (Beige BG, „★ NEU · Histamin Seelenbauch Kurs · 12 Wochen")
3. **Call-CTA-Banner** oben: Beige BG (statt Kleid-Hellblau), Sans-Bold-Schrift, „Neu · Mein Histamin Seelenbauch Kurs ist da." → Dark-Button → Vercel
4. Hero (Full-Bleed Piran-Portrait `images/portraits/julia-piran-hero.jpg` gedreht) — CTAs „Erst mal stöbern" + „Meine Geschichte"
5. **„Kennst du das?"** Pain-Sektion (letzte Card jetzt Beige + Sans Bold statt Blau/Cormorant italic)
6. **★ Verkaufs-Sektion „Was ich dir anbieten kann"** (NEU 28.09.) — Julias Story-Headline: „Vom Darmverschluss und 5 Lebensmitteln zurück zu mir. Endlich bin ich wieder ich." + 3 Angebot-Karten: Nº 01 Seelenbauchbuch, **Nº 02 Seelenbauch Kurs (featured, Dark BG)**, Nº 03 TerraLuna App
7. **Themen-Sektion Instagram-Post-Stil** (redesign 27.09.) — Straßenbild `images/portraits/julia-strasse-kroatien.jpg` als Full-Bleed-BG, dunkler Overlay, 6 Themen-Blocks in weiß mit Backdrop-Blur. Histamin als Hero-Block über 4 Spalten. Weißer Button „Zum Symptom-Selbsttest →"
8. Full-Bleed IMG_4680
9. **Kurs-Herzstück** — Portrait + Headline „Histamin Seelenbauch" + 3 Paket-Tiles (Basic/Gruppenkurs/Seelenbauch Kurs)
10. **Nº 04 · 10 Wochenmodule** — kompakte Mini-Karten
11. **Nº 05 · 5 Kohorten-Termine**
12. **Featured Blog-Card** „Was mir bei Histamin und Essensangst geholfen hat"
13. Blog-Sektion (3 Kacheln) — Nº 03 Blähbauch mit neuem Brille-Portrait
14. Bücher & Community
15. **Empfehlungen** — neues Foto `julia-strasse-kroatien.jpg`
16. App
17. Gespräch/Peer-Support
18. Footer

---

## Bücher (`ebooks.html`) — 3-Card-Übersicht neu 28.09.

Seite heißt „Bücher". Neue Übersicht am Seitenanfang: **3-Card-Grid, alle gleich hoch**, mittlere Card mit Malaga-Border als Fokus. Bestellung weiterhin per Mail-Vorkasse oder WhatsApp.

| Nº | Titel | Preis | CTA/Status |
|---|---|---|---|
| **01** | Die Probe (Reisen mit Histamin) | 7,99 € | Zum E-Book → `ebook-reisen.html` |
| **02** ★ FOKUS | **Das Seelenbauchbuch — Der Weg zurück zu deinem Seelenbauch** (144 S., Magazin-Stil, Seelenrezepte, Reflexionsfragen) | **24,99 € Softcover · 9,99 € E-Book** | Mehr & bestellen → `#seelenbauchbuch` (Detail-Sektion mit 12-Seiten-Preview). **12 Stück auf Lager.** |
| **03** | Zyklus-Leitfaden | **Kostenlos** | **WhatsApp-Freebie** (Lead-Magnet!) → Button öffnet `wa.me/4915118515394?text=Hallo%20Julia%2C%20ich%20h%C3%A4tte%20gerne%20deinen%20kostenlosen%20Zyklus-Leitfaden.` Julia bekommt die Nummer, sendet Leitfaden zu. |

**In Arbeit (weiter unten auf ebooks.html):** Freebie „Histamin & Ängste der Familie erklären", „So wird man seine Ängste los" (14,99 €), „Was Depressionen mit einem machen" (14,99 €).

**Iss dich stabil** wurde am 24.09. auf Julias Wunsch entfernt. Kann später zurück.

**Live Calls** (32 €/Call) am 28.09. aus Nav + Angeboten entfernt. `live-calls.html` bleibt im Repo, aus Nav rausgenommen. Kann reaktiviert werden.

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

**Startseite-Buttons (index.html, 25.09.):**
- Beide blauen `.btn-kleidblau`-Buttons auf der Startseite sagen jetzt einheitlich **„Seelenbauch Kurs"** (zwei Wörter, ohne „Zur", ohne Pfeil) — vorher waren es „Zur Histamin Seelenbauch Kurs" und „Seelenbauchkurs →" (inkonsistent). Ein Button führt zu Vercel, der andere zur histamin-masterclass.html-Landing.

### Landing auf juliabergles.de/histamin-masterclass.html

Editorial-Landing mit 16 nummerierten Sektionen (Nº 01–16). Hero-H1 bleibt „Histamin verstehen. Deinen Körper verstehen. Wieder mehr Vertrauen entwickeln." — der Kurs-Name „Histamin Seelenbauch Kurs" steht im Eyebrow, die Tagline drunter.

**Wow-Effekt-Politur 27.09.:**
- **Hero mit großem Kroatien-Portrait rechts** — `images/kurs-neu/IMG_9364.jpg` (Julia am Meer), mit sanfter Float-Animation. Vorher nur Text.
- **Zwei Full-Bleed-Bild-Breaks zwischen Sektionen** — `IMG_9009.jpg` (Jeansjacke) + `IMG_8977.jpg` (Portrait) als Trenner-Bilder ohne Overlay, geben der Landing Atem.
- **Nº 10 · Meine Geschichte** neu strukturiert — Portrait `IMG_8944 2.jpg` (blaues Top) direkt daneben, blauer Eyebrow, mehr persönlich.
- **Blog-Teaser** nach Meine-Geschichte-Sektion: kleiner Verweis auf den neuen Blog-Artikel „Was mir bei Histamin und Essensangst geholfen hat" mit Copper-Underline-Link.

Sektionen: 01 Problem · 02 Was du lernst · 03 Persönlicher Bereich · 04 **10 Wochenmodule** im Überblick · 05 Das bekommst du · 06 Bewegung · 07 Ernährung · 08 Zu wenig essen · 09 Mehr Vielfalt · 10 **Meine Geschichte (mit Portrait + Blog-Teaser)** · 11 Warum es dir wert ist · 12 Alle Termine · 13 Deine Optionen (Preise + Early-Bird-Callout) · 14 Terra Luna · 15 FAQ · 16 Abschluss.

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

**Kursbereich `/masterclass/*` — Julia's Politur 25.09. morgens:**
Julia hat den geschützten Kursbereich (Dashboard, Wochen, Rezepte, Empfehlungen, Wochenplan, Editor) auf einheitliches Design gebracht:
- Schrift: **Glacial Indifference** (font-sans) überall, kein Cormorant Serif mehr im Kurs-Bereich — passt zum E-Book-Stil
- Keine kursive Schrift mehr
- H1–H4 automatisch fett
- Fließtexte 14/16px, Überschriften bleiben groß
- Modul 2 (Ernährung im Alltag) ausführlicher, Modul 1 Card 5 mit fetten Headern und ▸-Punkten untereinander
- Neues `renderInhalt()`: Zeilen mit ▸ als sichtbare Listen, **bold** Markdown → `<strong>`
- Rosa Hintergrund für Wochenmodule
- Reflexions-Card verweist explizit auf Notizbuch (Handschrift, keine Tastatur)
- Kunsttherapie-/Kreativ-Impuls-Element im Notizbuch mit WhatsApp-Brücke

**Vercel Build-History 25.09.:**
- Commit `c5fbf08` (Anmeldung-Refactor) hat unbeabsichtigt `src/lib/email.ts` gebrochen (falsche Perl-Regex bei `data.zahlungsart === "raten"` → `data.(zahlungsart === "raten3" || zahlungsart === "raten6")` — kein valides JS)
- Julia hat das mit Commit `00ef83e Fix Build-Error email.ts` selbst gefixt (Klammern richtig gesetzt)
- Lehre: bei Perl-Regex mit Punkt vor Variablennamen aufpassen — `data.` wird mitverschluckt

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

**12 Artikel-Ordner** (jeweils mit `index.html`) — Themen: Darmverschluss, Warum wenig essen, Sport, Blähbauch, Auf Körper hören, Enttäuscht von Ärzten, Frische Diagnose, Gym-Transformation, Weg aus Depressionen, Angst vor Essen, Orthorexie/Corona, **neu 27.09.: „Was mir bei Histamin und Essensangst geholfen hat"** (`blog/was-mir-geholfen-hat/`, 10 Sektionen, Julias Text 1:1, ausführlich). Alle enden mit CTA zur App oder zum Kurs.

**Blog-Übersicht (`blog/index.html`)**: Oben Featured-Kachel für den neuen Artikel mit Badge „Neu · Ausführlich" (Beige-BG, Copper-Border-Left). Verlinkt auch prominent von Startseite (Featured Card oberhalb der 3 Standard-Kacheln) und Kurs-Landing (Teaser „Zum Weiterlesen" nach Meine-Geschichte-Sektion).

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

**Julias Portraits (organisiert in `images/portraits/` seit 28.09.):**
- `images/portraits/julia-piran-hero.jpg` — Piran-Kleid-Portrait, gedreht (Startseite Hero)
- `images/portraits/julia-sonnenuntergang.jpg` — IMG_9442 Kroatien Sonnenuntergang mit dunkler Brille (früher Über-mich Hero, jetzt ersetzt)
- `images/portraits/julia-brille-nahaufnahme.jpg` — IMG_9621 Nahaufnahme mit Brille festhalten (Startseite Blähbauch-Blog-Kachel)
- `images/portraits/julia-strasse-kroatien.jpg` — IMG_9715 kniend auf Kroatien-Straße, hellblauer Halter + Brille (Startseite Themen-Sektion BG + Empfehlungen-Sektion)
- `images/hey-ich-bin-julia.jpg` — Nachtstraße Piran, blaues Kleid, kniend (Über-mich Hero seit 28.09.)
- `images/hey-julia-2.jpg` — Zwinker mit Brille + Jeansjacke + hellblauem Rollkragen (Über-mich 2. Bild seit 28.09.)

**Kurs-Landing (`images/kurs-neu/`, seit 27.09.):**
- `IMG_9364.jpg` — Kroatien am Meer (Kurs-Landing Hero-Portrait rechts, mit Float-Animation)
- `IMG_9009.jpg` — Jeansjacke (Full-Bleed-Break)
- `IMG_8977.jpg` — Portrait (Full-Bleed-Break)
- `IMG_8944 2.jpg` — blaues Top (Meine-Geschichte-Sektion, Nº 10)
- Vorrats-Bilder: `IMG_8974 2.jpg` · `IMG_9079.jpg` · `IMG_9085.jpg`
- HEIC-Originale entfernt

**Weitere neue Portraits (in `images/Neue Bilder/`, noch nicht integriert):**
- IMG_9648 — Meer + Sonnenuntergang mit Brille (Editorial, könnte auf Kurs-Landing)
- IMG_9707 — verschwommen kniend auf Straße
- IMG_9720 — Rückansicht gehend (gedreht, muss rotiert werden)
- IMG_8865 / 8869 / 8872 / 8973 / 8975 / 8978 — Innenraum-Selfie-Serie mit Brille + hellblauem Top
- IMG_9081 / 9083 — Bad-Spiegelselfie Jeansjacke

**Cover-Bilder:**
- Die Probe: `ebook-reisen/bilder/Titelbild.PNG` ✓
- Seelenbauchbuch: `images/seelenbauchbuch/cover.png` (neues Cover vom 24.09., ersetzt das alte 1.jpg) + 12-Seiten-Preview
- Zyklus-Leitfaden: **Placeholder** — Julia liefert Cover-Bild bei Gelegenheit
- Freebook „Familie" / „Ängste" / „Depressionen": Placeholder

---

## Rechtstexte

Alle auf Stand September 2026:
- **`agb.html`** — 25.09. nachmittags rechtlich abgeklopft: § 5a.4 WhatsApp klar definiert (24/7 erreichbar, Antwortzeit werktags 24 Std.), § 5a.5 neu (Storno 1:1 + Gruppen-Termine), § 5c Herbstspecial mit korrigierter Paket-Inhaltsliste (Seelenbauchbuch als Softcover in **allen 3** Paketen, nur E-Book Reisen als PDF), § 5c.3 Ausfall-Deadline von „25.09.2026" auf „7 Tage vor Kursstart" umgestellt, § 5c.8 Early-Bird, **neuer § 5d Rolling Entry** (Self Study 399 € + Seelenbauch 1:1 780 € mit 3M/6M Raten), Peer-Support-Preis in § 2.3 + § 8 auf 39 €/60 Min aktualisiert, Grammatik „Die Kurs" → „Der Kurs" durchgängig gefixt, „statt 899 €" beim Seelenbauch Kurs raus (§ 11 PreisAngV).
- **`widerruf.html`** — 25.09. auf 5-Paket-Struktur ausgerichtet (Herbstspecial + Rolling Entry), 1:1-Termine allgemein statt „Startgespräch/Abschlussgespräch", Peer-Support-Preis 39 €/60 Min synchronisiert. Fix: hatte auf nicht existentes „AGB § 5a.5" verwiesen — Ziel-Paragraph existiert jetzt.
- **`histamin-masterclass.html`** — Landing: „statt 899 €" beim Seelenbauch Kurs entfernt (Rest der Streichpreise sind rechtssaubere Herbstspecial-vs-Early-Bird bzw. Basic-vs-Rolling-Entry-Vergleiche).
- **`datenschutz.html`** — WhatsApp-Sonntags-Check-in, Videokonferenz, Calendly
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
- [ ] **Zyklus-Leitfaden Inhalt** — Zip + PDF liegen jetzt in `E-Book Zyklus und Histamin/` (versehentlich mit `git add -A` am 27.09. Abend committet, sind damit auf GitHub Pages public). Wenn Julia den Inhalt lieber privat hätte: per `git rm` + neuem Commit rausnehmen. Ansonsten entpacken und einbauen.
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
- [x] ~~Nav vereinheitlicht auf 88 Seiten~~ 28.09. — Master-Nav aus index.html, keine Nav-Wechsel mehr zwischen Seiten
- [x] ~~„Zum Kurs" + „Anmeldung" auf Vercel umgebogen~~ 28.09.
- [x] ~~Live Calls aus Nav raus~~ 28.09. — Datei bleibt, kann reaktiviert werden
- [x] ~~Startseite Verkaufs-Sektion „Was ich dir anbieten kann"~~ 28.09. — 3 Angebot-Karten (Buch/Kurs/App) mit Julias Story-Headline
- [x] ~~Bücher-Übersicht 3-Card-Grid + Zyklus-Leitfaden als WhatsApp-Freebie~~ 28.09.
- [x] ~~App-Seite kompakter (Feature-Grid statt 8 Sektionen)~~ 28.09.
- [x] ~~Startseite Themen-Sektion Instagram-Style~~ 28.09.
- [x] ~~Rezepte-Seite Kategorien Instagram-Style~~ 28.09.
- [x] ~~Headlines auf Manrope Bold (statt Cormorant fein)~~ 28.09.
- [x] ~~Copper → Malaga (Weinrot) als Akzent-Farbe~~ 28.09.
- [x] ~~Blau als BG global raus~~ 28.09.
- [x] ~~Neue Portrait-Bilder integriert~~ 28.09. — Über-mich, Startseite (Blähbauch-Kachel + Empfehlungen), Piran-Hero gedreht
- [x] ~~Bücher-Karten alle gleich hoch~~ 28.09.
- [x] ~~8 neue Rezepte + 7 Rezept-Fotos + Einfrier-Disclaimer~~ 27.–28.09.
- [ ] **Weitere Portrait-Bilder** (IMG_9648, 9707, 9720, Innenraum-Serie) noch nicht integriert — Julia entscheidet wo
- [ ] **Cover-Bild für Zyklus-Leitfaden** (aktuell Text-Placeholder in Buch-Card)
- [ ] **Zyklus-Leitfaden Inhalt** — Zip + PDF liegen jetzt in `E-Book Zyklus und Histamin/` (versehentlich mit `git add -A` committet, auf GitHub Pages public). Julia entscheidet: privat oder einbauen.
- [ ] **Kurs-Screenshots** für `histamin-masterclass.html` — Julia macht 3–5 Screenshots vom Dashboard
- [ ] **`histamin-masterclass.html` Kurs-Landing** — aktuell nicht mehr aus Nav verlinkt (Kurs geht direkt zu Vercel). Löschen oder ausbauen? Julia offen.
- [ ] AGB rechtlich von Anwalt prüfen lassen
- [ ] Uhrzeit für Start-Call vs. andere Termine harmonisieren

---

## Feedback-Regeln aus laufenden Sessions

- **Julia's Prosa gehört Julia.** Nur Rechtschreibung glätten, nicht umformulieren.
- **Bindestriche (em-dashes) werden systematisch entfernt** — Julia lässt sie durchgehend rausnehmen.
- **Deploy = git push, direkt** — keine Preview-Umgebung, Julia testet live am Handy.
- **Commit-Messages auf Deutsch, kurz.**
- **Direkt handeln, nicht endlos fragen.** Bei Unklarheit EINE knappe Frage im Fließtext.
- **Kein Anfassen ohne zu lesen.** Erst verstehen was existiert, dann ändern.
- **Julia gibt Termine/Zeiten oft schrittweise** — nachfragen nur wenn etwas komplett fehlt, sonst sinnvoll defaulten und Julia korrigiert bei Bedarf.
- **Website-Content-Strategie:** genug Wert für Vertrauen, aber nicht zu viel gratis. Der komplette Weg / die persönliche Begleitung / die Struktur bleibt im **Seelenbauchbuch + Seelencoaching (Kurs)**. Kostenlose Inhalte sind das Vertrauens-Vorspiel, nicht der Ersatz. Leere Rezept-Kategorien (Mealprep, Hüttenkäse, Alternativen) können bewusst als „das findest du im Kurs/Buch"-Positionierung dienen.
