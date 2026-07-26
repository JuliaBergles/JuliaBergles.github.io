# juliabergles.de — Kontext & Plan

> Was diese Website ist, wo sie hin soll, was gerade in Arbeit ist.
> Bei jeder Session zuerst hier reinschauen.
> Letzte Aktualisierung: Juli 2026

---

## Was ist das hier

Julia Bergles' Personal-Brand-Website unter **www.juliabergles.de**.

- Deploy: **GitHub Pages** (Repo: `github.com/JuliaBergles/JuliaBergles.github.io`)
- Aktueller Ordner-Pfad: `~/Library/Mobile Documents/com~apple~CloudDocs/juliabergles Website/`
- Vorher lag der Ordner in `~/Desktop/App/website/` — Juli 2026 losgekoppelt und in eigenen Ordner verschoben
- CNAME → `juliabergles.de`

**Julia in Kürze** (20, Wehringen bei Augsburg):
- Instagram: @julia_bergles
- Persönliche Geschichte: Darmverschluss mit 19 → 2 Jahre nur 5 Lebensmittel vertragen → heute mehr, aber immer noch reduziert
- Diagnosen: Histaminintoleranz (HIT), MCAS, Reizdarm
- Auslöser: Corona-Infektion (Geschmack verloren) → Orthorexie → immer weniger essen, immer mehr Sport
- Heute im Griff durch: regelmäßig essen, wenig Ballaststoffe, kein HIIT, angstfrei essen, 10 Min nach dem Essen laufen, gekeimte Lebensmittel

---

## Warum wir gerade umbauen (Juli 2026)

Die Website hieß bisher **„EatMoreArt | Wear Your Healing"** — ein Mix aus App-Werbung + Food-Charm-Shop + Masterclass + Freebooks. Julia will das entrümpeln:

- **Fokus:** die TerraLuna App + ihre eigene Geschichte + informativer Blog
- **„Wear Your Healing" raus:** Charms macht sie aktuell nicht mehr aktiv → aus Navigation raus, Dateien bleiben aber liegen (jederzeit reaktivierbar)
- **Blog aufbauen:** informative Artikel, die sie Menschen auf Instagram in DMs schicken kann, wenn Fragen kommen
- **Persönlichere Note:** Personal Brand statt Multi-Angebot-Funnel

---

## Zielstruktur der neuen Startseite

1. **Nav** — prominenter, größere Schrift, fetter
2. **Hero** — Julia + TerraLuna App im Fokus (nicht mehr WYH)
3. **Was die App kann** — Feature-Highlights + Screenshots (bleibt größtenteils)
4. **Was ist Histaminintoleranz / MCAS / Reizdarm** — 3 Info-Kacheln → verlinken auf eigene Seiten
5. **Meine Geschichte** — Teaser mit Foto, verlinkt zum Blog
6. **Blog** — Kachel-Grid mit 11 Artikeln (siehe unten)
7. **Persönliches Gespräch** — 25 €/30 Min via Calendly (`calendly.com/julia-bergles/30min`)
8. **Meine Empfehlungen** — aho.bio (Code Smacado10), tägliche Lebensmittel
9. **Kontakt**
10. **Footer** (ohne WYH-Links)

---

## Blog-Artikel — Master-Liste (11 Stück)

Julia schreibt alle Texte selbst. Claude darf umschreiben, aber muss nach Julia klingen (siehe CLAUDE.md).

1. **Wie kam es zu meinem Darmverschluss**
2. **Warum ich nur wenig esse**
3. **Sport und Histamin / MCAS** (warum kein HIIT)
4. **Wie ich meinen Blähbauch (fast) losgeworden bin** — Julias 6-Punkte-Ansatz: regelmäßig essen, wenig Ballaststoffe, kein HIIT, angstfrei essen, 10 Min laufen nach dem Essen, gekeimte Lebensmittel (aho.bio)
5. **Wie ich gelernt habe auf meinen Körper zu hören**
6. **Warum ich von Ärzten enttäuscht bin**
7. **Was ich jedem empfehlen würde, der die Diagnose gerade bekommen hat**
8. **Wie Gym mir geholfen hat** — mit Vorher-Bildern + 6 Monate Transformation
9. **Mein Weg raus aus den Depressionen**
10. **Angst vor dem Essen — wie ich sie losgeworden bin**
11. **Meine Orthorexie — wie alles nach der Corona-Infektion anfing** (Geschmack verloren → weniger essen → gesünder essen → mehr Sport)

Alle Artikel enden mit CTA zur App (**„Alle Rezepte und Lebensmittel-Bewertungen in der TerraLuna App"**).

Ordner-Struktur (geplant): `blog/[artikel-slug]/index.html`
URL-Format: `juliabergles.de/blog/blaehbauch-in-griff/` (sauber teilbar)

---

## Bilder — was schon zugeordnet ist

Julias Bilder liegen in `blog-bilder/`. Diese Namen sind bereits klar zuordbar:

- `Hintergrund header.HEIC` → **Startseiten-Hero**
- `Bevor ich ins Gym bin.jpeg` + `6 Monate Gym.jpeg` → **Artikel 8 (Gym)**
- `Blähbauch und schmerzen/` (Unterordner) → **Artikel 4 (Blähbauch)**
- `Histamin Diagnose.jpg` → **Artikel 7 (Diagnose-Empfehlung)**
- `Erstes mal nach 2 Jahren hab ich mich auf Geburtstag getraut.jpg` → **Artikel 10 (Angst vor dem Essen)**

Rest (`IMG_xxxx.jpeg`) wird beim Schreiben der Artikel zugeordnet.

---

## Info-Seiten (neu, außerhalb Blog)

Kürzere, „lexikalische" Seiten — was die Diagnose ist, keine persönliche Geschichte:

- `histaminintoleranz.html`
- `mcas.html`
- `reizdarm.html`

Verlinkt aus der Startseite + jedem passenden Blog-Artikel.

---

## Telefonate — 1:1 Peer-Support

- **25 € / 30 Minuten**
- Buchung via bestehendem Calendly-Link: `calendly.com/julia-bergles/30min`
- Positionierung: **„Erfahrungsaustausch"** / **„Peer-Support"** — NIEMALS „Beratung" oder „Coaching" (Heilpraktiker-Gesetz)
- Disclaimer auf der Seite: „Ich teile meine eigene Erfahrung. Keine medizinische Beratung, kein Ersatz für Arzt/Therapeut."
- Zahlung: kann in Calendly-Settings über Stripe eingerichtet werden

---

## Design-Präferenzen (neu)

- **Fonts wie Agentur-Site (agentur.juliabergles.de):**
  - Headlines: **Playfair Display** (Serif)
  - Body/UI: **Object Sans**
- **Schrift 20-30 % größer als aktuell**, Body auf `font-weight: 500`, Headlines fetter
- **Menü prominenter:** mehr Padding, sichtbarere Schrift
- **Farbpalette bleibt** (aus altem Design):
  - Bordeaux `#955251` (Primary)
  - Copper `#C48B6C` (Accent)
  - Warm-White `#F8F2EE` (Background)
  - Text-Dark `#3D2B2E`

---

## WYH — raus (Stand Juli 2026, von Julia bestätigt)

Wear Your Healing ist aus Nav und Footer **komplett raus**. Dateien bleiben auf Platte liegen — falls Julia's je wieder aktivieren will, sind sie da. Aber im aktuellen Bild der Website: **nicht existent**.

Dateien, die liegen bleiben (nicht verlinkt, nicht löschen):
- `eatmoreart.html` (Shop)
- `bestellen.html`, `bestell-uebersicht.html`, `danke.html`, `widerruf.html` (Bestellprozess)
- `funnel.html`
- `freebook.html`, `ebooks.html` (Freebook-Landings — WYH-Ära)
- `dashboard.html`, `deine-speisekammer.html`, `onboarding.html`, `social-media.html` (WYH-Ära, unbenutzt)
- `masterclass/` gesamt (Seelenbauch Masterclass — WYH-Ära)
- `selbsttest.html` (unbenutzt seit Redesign)

**Nicht** in Nav/Footer aufnehmen. Wenn Julia je zurück will → explizit ansprechen.

---

## Deploy

- **Deploy = git push auf `main`** — GitHub Pages baut automatisch
- **Direkt pushen**, keine Zwischenschritte — Julia testet live am Handy
- Vor jedem Push: kurz commit-Message auf Deutsch (z. B. „Blog-Artikel Blähbauch fertig")

---

## ⚠️ Git-Zustand-Warnung (Juli 2026)

Beim Move waren ~100 Dateien als „gelöscht" im Git markiert (Freebooks, alte Posts, Screenshots, Masterclass-Stories). Sind wirklich lokal weg, nicht nur offline. **Vor dem nächsten Commit prüfen:** Sind diese Löschungen absichtlich (dann committen), oder müssen sie wiederhergestellt werden (`git restore <datei>`)?

Betroffen u. a.:
- `Social Media AngebotJulia Bergles.pdf`
- `contentplan/*.html`
- `freebooks/guide-allergie.html`, `guide-fructose.html`, `guide-zyklus.html`
- `images/julia-profil.jpeg`, `images/maskottchen/*`, viele `images/IMG_*`
- `masterclass/stories/*.png`, `vergleich.html`, `zeitplan.html`
- `posts/post_01_*`, `post_02_*`, `post_04_*` (Slide-PNGs)

---

## Was gerade offen ist (Juli 2026)

**Erledigt:**
- [x] Startseite neu gebaut — editorial Design nach Julias Screenshots, zentriertes „Julia" Logo, Menü-basiert (Über mich | Blog | App | Gespräch | Empfehlungen | Kontakt)
- [x] Info-Seiten `histaminintoleranz.html`, `mcas.html`, `reizdarm.html` als Skelett
- [x] Blog-Struktur: `blog/index.html` + 11 Platzhalter-Ordner
- [x] Neue Seiten: `ueber-mich.html`, `gespraech.html`
- [x] `empfehlungen.html` im neuen Design
- [x] WYH aus Nav/Footer raus, Dateien bleiben
- [x] Git-Löschungen aus dem Move committed
- [x] Shared CSS in `assets/site.css` für alle neuen Seiten

**Noch offen:**
- [ ] **Julia-Texte einbauen** — überall wo 📝 Platzhalter stehen (Homepage-Hero-Sub, Über mich, Info-Seiten, Blog-Artikel). Julia schreibt selbst, Claude paste ein.
- [ ] Bilder für Blog-Karten wo aktuell Text-Platzhalter (wenig, Sport, hören, enttäuscht)
- [ ] Ggf. Hero-Foto tauschen (aktuell `images/IMG_5738.jpeg` — falls besseres Bild da)
- [ ] `app.html` läuft noch im alten Design — entscheiden ob umziehen oder lassen
- [ ] Bilder in `blog-bilder/` (100MB, lokal, nicht im Repo) den Blog-Artikeln zuordnen

## Feedback-Regeln aus laufenden Sessions

- **Julia's Prosa gehört Julia.** Claude hat mehrfach Versuche in ihrer Stimme geschrieben (Hero-Sub, Meine-Geschichte-Teaser) — jedes Mal Rückmeldung „klingt nicht gut". Konsequenz: bei prosa-artigem Content nur Platzhalter setzen, Julia füllt.
- **Ehrlich sein, dass es Placeholder ist.** Kein Versuch, sanft in ihre Voice zu schreiben.
