# juliabergles.de — Kontext & Plan

> Was diese Website ist, wo sie hin soll, was gerade in Arbeit ist.
> Bei jeder Session zuerst hier reinschauen.
> Letzte Aktualisierung: 2026-08-16

---

## Was ist das hier

Julia Bergles' Personal-Brand-Website unter **www.juliabergles.de**.

- Deploy: **GitHub Pages** (Repo: `github.com/JuliaBergles/JuliaBergles.github.io`)
- Ordner-Pfad: `~/Library/Mobile Documents/com~apple~CloudDocs/juliabergles Website/`
- CNAME → `juliabergles.de`
- Julia testet **live am Handy** — kein lokaler Preview-Zwischenschritt

**Julia in Kürze** (20, Wehringen bei Augsburg):
- Instagram: @julia_bergles
- Geschichte: Corona-Infektion → Geschmack weg → Orthorexie → Darmverschluss mit 19 → 2 Jahre nur 5 Lebensmittel → heute mehr, aber immer noch reduziert
- Diagnosen: **Histaminintoleranz (HIT)** beim Arzt + Cerascreen bestätigt, **Allergien** (Kartoffel, Apfel, Mandeln, Haselnüsse, Karotte Sommer, Latex, Nickel, Erdnüsse, Soja leicht), **PMS**, **Pollenallergie**
- Vermutet: **MCAS** (wird demnächst getestet)
- Auch dabei: Orthorexie, Angststörung, verzerrte Selbstwahrnehmung
- Heute im Griff durch: regelmäßig essen, wenig Ballaststoffe, kein HIIT, angstfrei essen, 10 Min nach dem Essen laufen, gekeimte Lebensmittel

---

## Aktueller Design-/Feature-Stand

**Fertig gebaut und live:**
- Startseite editorial, zentriertes „Julia"-Logo, Menü-basiert (Über mich | Blog | App | Gespräch | Empfehlungen | Kontakt)
- Info-Seiten `histaminintoleranz.html`, `mcas.html`, `reizdarm.html`
- `ueber-mich.html` mit Sektion **„Meine Tests + Diagnosen"** (5 Toggles: Diagnostiziert / Vermutet / Meine Allergien / Wie ich reagiere / Auch das gehört dazu — Malaga-Buttons zum Aufklappen mit Plus-Icon)
- `gespraech.html` — Peer-Support 25 €/30 Min via Calendly (`calendly.com/julia-bergles/30min`)
- `empfehlungen.html` — **5 Produkte** in großen Karten mit „Das kaufe ich"-Box + Rabattcode + Gold-Button:
  1. **aho.bio** (Code `Smacado10`) — Sprossenmehl, gekeimte Haferflocken, gekeimter Reis, Belugalinsen
  2. **Histaminikus** — alle Gewürze
  3. **HistaFOOD** — Basilikum-Zucchini-Aufstrich, Beeren-Riegel, Proteinpulver, Gemüsebrühe
  4. **Balance Riegel** (histaminarme Variante, mit Fructose-Warnung)
  5. **Yamatogast** (kein Affiliate, Kampro-Arzneimittel aus 8 Heilpflanzen, mit Warnung „meine eigene Erfahrung")
- `blog/index.html` + 11 Artikel-Ordner (siehe unten)
- **Selbsttest wieder aktiv:** `selbsttest.html` läuft komplett client-seitig (keine Speicherung, kein Tracking) — Symptom-Quiz mit Handlungsempfehlung
- **Startseite: Sektion „Einführung in die App"** zwischen Feature-Cards und App-Showcase — zwei Karten (So funktioniert / Für wen ist die App) + WhatsApp-Community-CTA (https://chat.whatsapp.com/Bld3QLjowCKBpW6dksoRVK). Feature-Card #5 auf Startseite ist Anker-Link `#einfuehrung`.
- **Instagram-Insights-Seite** `instagram-insights.html` (Reichweite/Zielgruppe/Interaktionen 6.7.–4.8.2026)
- **Floating Instagram-Button** unten rechts auf allen aktiven Seiten (Malaga + Gold-Rand)
- **Health-Disclaimer** im Footer aller Unterseiten („Ich bin keine Ärztin")
- Zeitstrahl auf `ueber-mich`: Malaga-Gradient-Karten, Gold-Border, Pill-shaped Marker, Gold-Fade-Linie
- Page-Hero mit BG-Image + Overlay auf jeder Unterseite; H1 weiß, weight 700, doppelter Text-Shadow
- **Shared CSS:** `assets/site.css` für alle neuen Seiten
- **Neue Nav (7 Items, 2 Dropdowns):** Über mich · Diagnosen ▾ (Histaminintoleranz / MCAS / Reizdarm) · Selbsttest · Blog · Rezepte · Shop ▾ (E-Books / Kunst / TerraLuna App) · Empfehlungen + Gespräch-CTA. Auf **allen 28 aktiven Seiten** (12 Haupt + 11 Blog + blog-index + Impressum + Datenschutz + AGB + Widerruf). Mobile: Sub-Punkte eingerückt unter „Diagnosen"/„Shop"-Labels. Rechts-Seiten (Impressum/Datenschutz/AGB/Widerruf) haben Nav-CSS inline (nicht via `css/onpoint.css`) — bei Nav-Änderungen dort separat nachziehen.

**Bilder gesetzt (inline, aus `blog-bilder/`):**
- Startseiten-Hero, Über mich (`Liebe.jpeg`), App (TerraLuna-Logo), HIT (Sonnenblumen-Portrait), MCAS, Reizdarm, Empfehlungen („Was auf meinem Teller landet"), Gespräch
- Selbsttest: **kein Foto**, nur Malaga-Gradient

---

## TerraLuna App (früher „Vollmond")

- **App heißt TerraLuna** — überall so benannt, auch AGB (nicht mehr EatMoreArt-Referenzen)
- **Preise:** 4,99 €/Monat oder 39,99 €/Jahr (vorher 7,99 / 59,99)
- **Preis-Sektion „Ein klarer Plan":** 2-Spalten-Layout — iPhone-Home-Screen (`images/app-v1.2/01-heute.png`) links, Preis-Karte rechts, auf Mobile gestapelt. CTA lautet **„Jetzt 3 Tage kostenlos testen oder kostenfreie Version nutzen"**
- `app.html` ist auf neues Design (Fonts + Overlay) gebracht — doppelte Stylesheet-Links im body raus, einer im head

---

## Blog-Artikel — Master-Liste (11 Stück)

Julia schreibt alle Texte selbst. Claude darf umschreiben, aber muss nach Julia klingen (siehe CLAUDE.md).

Ordner in `blog/`:
1. `darmverschluss/` — Wie kam es zu meinem Darmverschluss
2. `warum-wenig-essen/` — Warum ich nur wenig esse
3. `sport-histamin-mcas/` — Sport und Histamin/MCAS (warum kein HIIT)
4. `blaehbauch-in-griff/` — Blähbauch (fast) losgeworden (6-Punkte-Ansatz)
5. `auf-koerper-hoeren/` — Wie ich auf meinen Körper hören gelernt habe
6. `enttaeuscht-von-aerzten/` — Warum ich von Ärzten enttäuscht bin
7. `frische-diagnose/` — Was ich jedem empfehlen würde, der die Diagnose gerade bekommen hat
8. `gym-transformation/` — Wie Gym mir geholfen hat (mit Vorher-Bildern + 6 Monate Transformation)
9. `weg-aus-depressionen/` — Mein Weg raus aus den Depressionen
10. `angst-vor-essen/` — Angst vor dem Essen — wie ich sie losgeworden bin
11. `orthorexie-corona/` — Orthorexie — wie alles nach der Corona-Infektion anfing

Alle Artikel enden mit CTA zur TerraLuna-App.
URL-Format: `juliabergles.de/blog/[slug]/`

---

## Info-Seiten (kein Blog)

Kürzere, „lexikalische" Seiten — was die Diagnose ist, keine persönliche Geschichte:
- `histaminintoleranz.html` — inkl. Sektion **„Wie ich bei Histamin reagiere"** (Bauchkrämpfe, Durchfall, Schwindel, Übelkeit, Brainfog; 3–4 h akut + 1–2 Tage Nachwirkung; Histaminfass-Konzept; Stress als starker Trigger; „bei Histamin bin ich wirklich unglaublich sensibel")
- `mcas.html`
- `reizdarm.html`

Verlinkt von Startseite + relevanten Blog-Artikeln.

---

## Peer-Support-Telefonate

- **25 €/30 Minuten** via Calendly: `calendly.com/julia-bergles/30min`
- Positionierung: **„Erfahrungsaustausch" / „Peer-Support"** — NIEMALS „Beratung" oder „Coaching" (Heilpraktiker-Gesetz)
- Disclaimer: „Ich teile meine eigene Erfahrung. Keine medizinische Beratung, kein Ersatz für Arzt/Therapeut."

---

## Design-System — v3 FINAL (ab 2026-08-17)

**Stil:** Editorial / Vogue-Zeitschrift. Direkt am E-Book-Cover „Die Probe" orientiert. Warm-kühl kombiniert. Große Serif-Displays, viel Weißraum, ALL-CAPS Eyebrow-Labels, Nº-Kapitelmarker, rechteckige Buttons, dünne Trennlinien.

**Zentrales Stylesheet:** `assets/site-v3.css` (fertig 2026-08-17).
**Erste Referenz-Seite:** `ebook-reisen.html` (Landing für E-Book „Die Probe").

**Fonts:**
- Headlines: **Cormorant Garamond** (Google Fonts) — Serif, elegant, 400/500 weight, große Sizes
- Body/UI: **Manrope** (Google Fonts) — geometric Sans, ~95% Glacial-Indifference-Look
- *Optional-Upgrade:* Echte Glacial Indifference als WOFF2 in `assets/fonts/`, dann im `--sans` Token vor Manrope setzen (Julia besorgt die Dateien, ich schalte sie frei)

**Farben:**
- Warm: Cream `#fffcf9`, Beige `#f4ede4`, Copper `#C48B6C`, Copper-dark `#a87556`
- Kühl: Blau `#8790c1`, Blau-dark `#6f78a8`, Mint `#e2fffe`
- Neutral: Dark `#2a2a2a`, Dark-soft `#4a4a4a`, Mute `#8a8a8a`
- Regel: Copper für Aktion (CTA, Buttons). Blau für Editorial-Ruhe (Zitate, E-Book, gefährdete Themen). Warm bleibt Basis.

**Ehemalige Regeln — überholt:**
- Raleway 900 + Object Sans → durch Cormorant Garamond + Manrope ersetzt
- „Kein Blau" → aufgehoben: Blau ist offizieller Zweitakzent
- OnPoint-Kit + agentur.juliabergles.de als Design-Referenz → durch eigenes E-Book-Cover als Referenz ersetzt

**Spacing:**
- Section-Padding: `clamp(80px, 12vw, 160px)` vertikal
- Container: `max-width 1280px`, `max-width-narrow 780px`
- Padding X: `clamp(24px, 5vw, 60px)`

**Bilder:** großflächig, editorial (full-bleed, split, oder als Sektions-Break), persönliche Fotografie. Bevorzugt: Julias eigene Bilder aus `images/neu-2026-08/` und `ebook-reisen/bilder/`.

**Neue Bilder (2026-08-14):** 15 Julia-HEICs in `images/neu-2026-08/*.jpg` (2400 px, JPEG 85). Aufteilung:
- **Portraits (Website):** IMG_3635, 3636, 3639, 3545 → Über mich, Hero, App
- **Reise-Motive (E-Book):** IMG_3612, 3631, 3632, 3689, 3697, 3738, 3776, 3835, 3836, 3719-2, 3724-2 → Ljubljana + Bougainvillea + Mittelmeer-Nacht

**E-Book „Die Probe" — Julia hat bereits gestaltet:**
- Cover „Titelbild.PNG" in `ebook-reisen/bilder/` (Nächtliche Straße, blaues Kleid, „DIE PROBE" — Farbwelt Babyblau + Cream + Serif → wurde zur Website-Design-Referenz)
- Vorwort 1-3.JPG, Kapitel vorschau.jpg, Rabattcodes.jpg als PDF-Seiten-Screenshots

**Redesign-Historie:**
- v2 (5f63dd1, 2026-08-10 revertet): Raleway/Archivo/Cream+Choice-Screen — zu experimentell
- v3-Anfang (2026-08-14): geplant als agentur.juliabergles.de-Look — verworfen
- v3-final (2026-08-17): Editorial nach E-Book-Cover — laufend

---

## Datenschutz / Rechtliches

- **Selbsttest-Sektion in Datenschutz:** Sektion 6 „Symptom-Check / Selbsttest" — läuft komplett client-seitig, keine Speicherung, keine Übertragung, kein Tracking
- **Impressum, Datenschutz, AGB, Widerruf** — alle da und aktuell
- AGB-EatMoreArt-Referenzen → auf TerraLuna umgestellt

---

## Videografie — komplett raus (2026-08-10)

Videografie war kurz drin (Nav, Feature-Card #5, eigene Seite `videografie.html`) — Julia wollte das wieder raus. **Alle Links entfernt**, `videografie.html` **gelöscht**. Feature-Card #5 auf Startseite ist jetzt „Einführung in die App".

---

## WYH — raus (nicht verlinken, nicht löschen)

Wear Your Healing ist aus Nav und Footer **komplett raus**. Dateien liegen weiter auf Platte für ggf. Reaktivierung:
- `eatmoreart.html` (Shop)
- `bestellen.html`, `bestell-uebersicht.html`, `danke.html` (Bestellprozess)
- `funnel.html`
- `freebook.html`, `ebooks.html`
- `dashboard.html`, `deine-speisekammer.html`, `onboarding.html`, `social-media.html`
- `masterclass/` gesamt
- `freebooks/` gesamt
- `contentplan/`, `posts/`, `templates/`, `tools/`

**Nicht** in Nav/Footer aufnehmen. Wenn Julia je zurück will → explizit ansprechen.

---

## Deploy

- **Deploy = git push auf `main`** — GitHub Pages baut in ~1 Min
- **Direkt pushen**, keine Zwischenschritte
- Commit-Messages: **Deutsch, kurz und beschreibend** (siehe git log für Stil)

---

## Was gerade offen ist

**In Arbeit — Redesign v3 FINAL (2026-08-17):**
- [x] Design-System final: Cormorant Garamond + Manrope + Cream/Copper/Blau/Mint/Dark
- [x] `assets/site-v3.css` aufgebaut
- [x] `ebook-reisen.html` als erste Vogue-Editorial-Referenz-Seite
- [x] CLAUDE.md + CONTEXT.md Design-Sektion nachgezogen
- [ ] Startseite (`index.html`) auf v3 umstellen
- [ ] Über mich (`ueber-mich.html`) auf v3 umstellen
- [ ] App (`app.html`) auf v3 umstellen
- [ ] HIT / MCAS / Reizdarm Info-Seiten auf v3
- [ ] Blog (`blog/index.html` + Artikel) auf v3
- [ ] Empfehlungen (`empfehlungen.html`) auf v3
- [ ] Gespräch (`gespraech.html`) auf v3
- [ ] Rezept-Bereich neu bauen (Übersicht + Rezept-Template)
- [ ] Blog-Kategorien-System (Histamin, MCAS, Ernährung, Darm, Zyklus, Alltag, Erfahrungen, App, Rezepte)
- [ ] Landing-Pages für weitere E-Books (`ebook-aengste.html`, `ebook-familie.html`, `ebook-depressionen.html`)

**Bestehendes weiter offen:**
- [ ] **Julia-Texte einbauen** — überall wo 📝 Platzhalter stehen (Vorwort „Die Probe", Blog-Artikel-Body). Julia schreibt selbst, Claude paste ein.
- [ ] Elopage-Link für „Die Probe" einbauen sobald E-Book gelauncht
- [ ] E-Book „Die Probe" Zweitverwendung: K1 „Meine Geschichte" als Blog-Artikel unter `blog/erste-reise-nach-darmverschluss/`
- [ ] Bilder in `blog-bilder/` den einzelnen Blog-Artikeln zuordnen
- [ ] MCAS-Testergebnis abwarten und Diagnosen-Sektion updaten (aktuell „vermutet")
- [ ] 10 Reise-Bilder aus `images/neu-2026-08/` auch in `ebook-reisen/bilder/` kopieren (wenn Julia OK gibt)

**Regel für v3:** Bestehende Texte + Content grundsätzlich behalten, nur visuell/strukturell neu. Keine persönlichen Inhalte selbstständig kürzen oder streichen.

---

## Feedback-Regeln aus laufenden Sessions

- **Julia's Prosa gehört Julia.** Wenn prosa-artiger Content fehlt → Platzhalter setzen, nicht in ihrer Stimme schreiben.
- **Ehrlich sein, dass es Placeholder ist.** Kein Versuch, sanft in ihre Voice zu formulieren.
- **Bei Bug-Fixes tief graben** (siehe Selbsttest-Button-Fix: `page-hero::before/::after` haben Klicks abgefangen — pointer-events + z-index waren die Ursache, nicht der Button selbst)
- **Bilder brauchen kräftige Overlays** (50–85 % Malaga), sonst leidet Text-Lesbarkeit
