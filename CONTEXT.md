# juliabergles.de — Kontext & Plan

> Was diese Website ist, wo sie hin soll, was gerade in Arbeit ist.
> Bei jeder Session zuerst hier reinschauen.
> Letzte Aktualisierung: 2026-08-14

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

**Bilder gesetzt (inline, aus `blog-bilder/`):**
- Startseiten-Hero, Über mich (`Liebe.jpeg`), App (TerraLuna-Logo), HIT (Sonnenblumen-Portrait), MCAS, Reizdarm, Empfehlungen („Was auf meinem Teller landet"), Gespräch
- Selbsttest: **kein Foto**, nur Malaga-Gradient

---

## TerraLuna App (früher „Vollmond")

- **App heißt TerraLuna** — überall so benannt, auch AGB (nicht mehr EatMoreArt-Referenzen)
- **Preise:** 4,99 €/Monat oder 39,99 €/Jahr (vorher 7,99 / 59,99)
- **Preis-Sektion:** keine Feature-Liste mehr — CTA lautet **„Jetzt 3 Tage kostenlos testen oder kostenfreie Version nutzen"**
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

## Design-System — Redesign v3 (ab 2026-08-14)

**Wichtig:** Design-System wird komplett auf **OnPoint-Kit / agentur.juliabergles.de-Look** umgestellt. Die alten Angaben in CLAUDE.md (Playfair Display + Bordeaux `#955251` + Warm-White `#F8F2EE`) sind **veraltet** — es gilt was hier steht. CLAUDE.md-Design-Sektion muss noch nachgezogen werden.

**Fonts (verbindlich, wie agentur.juliabergles.de):**
- Headlines: **Raleway** weight 900, uppercase, letter-spacing tight
- Body/UI: **Object Sans** weight 400/500, 18–19 px, line-height 1.6

**Farben (verbindlich):**
- Copper `#C48B6C` (Primary/Akzent)
- Dark `#2a2a2a` (Text, dunkle Sektionen)
- Cream `#fffcf9` (Grundton BG)
- **Kein Grün, kein Blau, kein Schwarz-#000, kein Pink**

**Spacing:**
- Section-Padding: 120–160 px vertikal Desktop, 70–90 px mobile
- Container: max-width 1200 px, padding 0 40 px (24 px mobile)

**Bilder:** großzügige Flächen, mediterran-warm, persönliche Fotografie, organische Formen, viel Weißraum

**Referenzen für Aufbau:** Mia Page (Struktur/Atmosphäre) + agentur.juliabergles.de (Farben/Typo) — Details noch offen (Julia liefert Mia-URL).

**Neue Bilder (2026-08-14):** 15 Julia-HEICs aus iCloud konvertiert nach `images/neu-2026-08/*.jpg` (2400 px, JPEG 85). Werden im v3-Redesign eingebaut.

**Redesign-Historie:** Redesign v2 (5f63dd1, Raleway/Archivo/Cream+Choice-Screen) wurde am 2026-08-10 revertet (7054ef5) — war zu experimentell. v3 orientiert sich stärker an agentur.juliabergles.de + Mia Page.

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

**In Arbeit — Redesign v3 (2026-08-14):**
- [ ] **Mia-Page-URL** von Julia holen (Layout-Referenz)
- [ ] `assets/site-v3.css` mit neuen Design-Tokens (Raleway 900 + Object Sans + Copper/Dark/Cream) aufbauen
- [ ] Startseite als erste Komplett-Umsetzung — TerraLuna zieht sich als roter Faden durch (Hero-CTA, dedizierte App-Sektion, Content-CTAs bei Rezepten/Blog)
- [ ] Unterseiten iterativ nachziehen: Über mich → App → HIT/MCAS/Reizdarm → Blog → Rezepte → Empfehlungen → Insights
- [ ] Neue Bilder aus `images/neu-2026-08/` in Hero/Sektionen einbauen
- [ ] Rezept-Bereich neu bauen (Übersicht + Rezept-Template, Recipe-Schema)
- [ ] Blog-Kategorien-System (Histamin, MCAS, Ernährung, Darm, Zyklus, Alltag, Erfahrungen, App, Rezepte)
- [ ] CLAUDE.md-Design-Sektion nachziehen (Julia freigeben lassen)

**Bestehendes weiter offen:**
- [ ] **Julia-Texte einbauen** — überall wo 📝 Platzhalter stehen (Blog-Artikel-Body, ggf. Info-Seiten). Julia schreibt selbst, Claude paste ein.
- [ ] Einführungs-Sektion auf Startseite: Julia korrigiert Draft-Texte am Handy live.
- [ ] Bilder in `blog-bilder/` den einzelnen Blog-Artikeln zuordnen
- [ ] MCAS-Testergebnis abwarten und Diagnosen-Sektion updaten (aktuell „vermutet")

**Regel für v3:** Bestehende Texte + Content grundsätzlich behalten, nur visuell/strukturell neu. Keine persönlichen Inhalte selbstständig kürzen oder streichen.

---

## Feedback-Regeln aus laufenden Sessions

- **Julia's Prosa gehört Julia.** Wenn prosa-artiger Content fehlt → Platzhalter setzen, nicht in ihrer Stimme schreiben.
- **Ehrlich sein, dass es Placeholder ist.** Kein Versuch, sanft in ihre Voice zu formulieren.
- **Bei Bug-Fixes tief graben** (siehe Selbsttest-Button-Fix: `page-hero::before/::after` haben Klicks abgefangen — pointer-events + z-index waren die Ursache, nicht der Button selbst)
- **Bilder brauchen kräftige Overlays** (50–85 % Malaga), sonst leidet Text-Lesbarkeit
