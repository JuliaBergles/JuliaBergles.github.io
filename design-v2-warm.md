# Design v2 — Warm / Mediterran (das davor)

> Das Design, das vor v3 auf der Website lief. Warme Bordeaux/Copper-Palette, Playfair-Serif, sehr weiblich, „Freundin von nebenan".
> **Stylesheet:** `assets/site.css` (das alte, weiter im Repo).
> **Zurückwechseln:** In `git log` nach Commit `7cdac10` (letzter v2-Stand) oder Datei-für-Datei per `git checkout 7cdac10 -- <datei>` — dann Nav/Content anpassen wie du willst.

---

## Stimmung in einem Satz

Mediterran-warm, personal blog, sehr weiblich, Insta-nah.

## Fonts

```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;1,400;1,500;1,600&display=swap">
<link rel="stylesheet" href="https://api.fontshare.com/v2/css?f[]=object-sans@300,400,500,600,700&display=swap">
```

- **Headlines:** Playfair Display (Serif), weight 500–700
- **Body/UI:** Object Sans (Sans, weich), 18–19 px, weight 500
- **Betonung:** Kursiv oder Fett

## Farben

```css
--bordeaux:   #955251;   /* Primary */
--copper:     #C48B6C;   /* Accent */
--warm-white: #F8F2EE;   /* BG */
--warm-grey:  #F0E8E4;
--text-dark:  #3D2B2E;
--text-muted: #8A7B75;
```

**Regeln:**
- Bordeaux als Herzfarbe (Buttons, Marker, dunkle Sektionen)
- Copper als Zweitakzent
- Kein Blau, kein Grün, kein Schwarz — durchgehend warm

## Bausteine

- **Runde Ecken** (Buttons `border-radius: 12–24 px`, Karten mit sanften Radien)
- **Malaga-Gradienten** in Hero + Zeitstrahl-Karten
- **Glasmorph-Nav** mit Blur
- **Zeitstrahl** mit Pill-Markern + Gold-Fade-Linie (Über mich)
- **Choice-Cards** mit Farbcodes (`.c-orange`, `.c-blue`, `.c-pink`, `.c-ink`)
- **Full-Bleed Hero-Bilder** mit dunklem Overlay 40–60 %

## Nav

Damals-Struktur (mit Dropdowns Diagnosen + Shop):
- Über mich · Diagnosen ▾ · Selbsttest · Blog · Rezepte · Shop ▾ · Empfehlungen · Gespräch (CTA)

Selbe Struktur wie v3 — nur andere Fonts/Farben.

## Live-Referenz-Seiten (letzter v2-Stand)

- Vor Commit `418ad0a` (2026-08-17) — vor v3-Umstellung
- Konkret erhaltene v2-Seiten: aktuell noch alle Unter-Seiten (ueber-mich, HIT/MCAS/Reizdarm, Blog, etc.) bis sie auf v3 umgestellt werden.

## Wenn Julia wieder auf v2 wechseln will

Zwei Optionen:

**A) Komplett zurück (alle Seiten):**
```bash
git checkout 7cdac10  # letzter v2-Commit vor v3
```
Dann neu forken oder als Branch weitertragen.

**B) Einzelne Seiten zurück:**
```bash
git checkout 7cdac10 -- index.html
```
Und dann `<link>` auf `assets/site.css` prüfen.

**C) v2 als Alternative Live:** Dupliziere die aktuellen Seiten (`index-v3.html`, `index-v2.html`) und verlinke intern. Aufwändig, wenn beide gepflegt werden sollen.

**Empfehlung:** v2 als Referenz behalten für später — nicht parallel pflegen, sonst doppelter Aufwand.

---

## Meine ehrliche Design-Meinung (Claude)

- **v3 (Editorial):** stärker wiedererkennbar, professioneller, passt zum E-Book-Design → **empfohlen** für deine Marke (Personal Brand + Produkte)
- **v2 (Warm):** persönlicher, weicher, weniger einzigartig — funktioniert für pure Blog-Wirkung
- **Beides:** kombinierbar innerhalb v3 (warme Sektionen + kühles Blau als Kontrast). Was ich jetzt versuche.

Wenn du unsicher bist: **v3 mit mehr Wärme drin** ist der beste Mittelweg. Genau darauf ziele ich mit den aktuellen Iterationen ab (Copper-CTA statt Blau, warme Bild-Breaks zwischen kühlen Sektionen).
