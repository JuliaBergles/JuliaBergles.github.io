# Prompt: Statische Website bauen (wie juliabergles.de)

> Kopiere diesen Prompt in Claude Code um eine ähnliche Website zu bauen.
> Passe die Platzhalter [IN KLAMMERN] an dein Projekt an.

---

## Aufgabe

Baue eine statische Website für [MARKENNAME]. Die Website wird auf
GitHub Pages gehostet. Kein Framework, kein Build-Tool, kein Backend.
Nur HTML, CSS und minimales JavaScript.

## Tech Stack

- **Hosting:** GitHub Pages (kostenlos, statisch)
- **Sprache:** HTML5, CSS3, Vanilla JavaScript
- **Fonts:** Google Fonts (z.B. Cormorant Garamond für Headings, Inter für Body)
- **Formulare:** Tally.so (kostenlos, DSGVO-konform, EU-Server)
- **Styling:** Inline CSS pro Seite (kein Build-Prozess nötig)
- **Responsive:** Mobile-first, funktioniert auf allen Geräten

## Design-System

Definiere am Anfang jeder HTML-Datei CSS-Variablen:

```css
:root {
  --primary: [HAUPTFARBE];       /* z.B. #2c3e6b */
  --secondary: [AKZENTFARBE];    /* z.B. #bf6b6b */
  --accent: [GOLDAKZENT];        /* z.B. #c9a96e */
  --bg: [HINTERGRUND];           /* z.B. #faf4eb */
  --text: [TEXTFARBE];           /* z.B. #5c5047 */
  --text-light: [HELLTEXT];      /* z.B. #c4b5a6 */
  --white: #fffdf9;
}
```

### Schriftarten:
- Headings: Serif (elegant, warm)
- Body: Sans-Serif (klar, lesbar)

### Design-Prinzipien:
- Viel Weißraum
- Runde Ecken (border-radius: 20px+)
- Dezente Schatten
- Scroll-Animationen (.fade-up Klasse)
- Kein Grün, kein Orange (nur die definierten Farben)
- Keine Gedankenstriche, keine Emojis

## Seitenstruktur

Jede Seite folgt diesem Aufbau:

```
1. Navigation (fixed, transparent mit Blur)
2. Hero/Header
3. Inhaltssektionen
4. Footer (dunkel, mit Links zu Impressum/Datenschutz)
```

### Navigation (auf jeder Seite gleich):
```html
<nav>
  <div class="nav-inner">
    <a href="index.html" class="nav-logo">[LOGO]</a>
    <button class="menu-toggle">☰</button>
    <div class="nav-links">
      <a href="seite1.html">Link 1</a>
      <a href="seite2.html">Link 2</a>
      <a href="seite3.html" class="nav-cta">CTA</a>
    </div>
  </div>
</nav>
```

### Footer (auf jeder Seite gleich):
```html
<footer>
  <div class="footer-inner">
    <div class="footer-logo">[LOGO]</div>
    <div class="footer-links">
      <a href="impressum.html">Impressum</a>
      <a href="datenschutz.html">Datenschutz</a>
    </div>
  </div>
</footer>
```

## Scroll-Animation

Auf jeder Seite dieses Script + die Klasse .fade-up auf Elementen:

```html
<script>
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) entry.target.classList.add('visible');
  });
}, { threshold: 0.1 });
document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));
</script>
```

```css
.fade-up { opacity: 0; transform: translateY(30px); transition: all 0.8s ease; }
.fade-up.visible { opacity: 1; transform: translateY(0); }
```

## Seiten die gebraucht werden

1. **index.html** - Startseite (Hero, Angebote, Über mich, Kontakt)
2. **[produkt].html** - Produktseite/Shop
3. **bestell-uebersicht.html** - Übersicht vor der Bestellung
4. **bestellen.html** - Bestellformular (Tally embed)
5. **danke.html** - Danke-Seite nach Bestellung
6. **datenschutz.html** - Datenschutzerklärung (DSGVO)
7. **impressum.html** - Impressum (§5 TMG)
8. **widerruf.html** - Widerrufsbelehrung

## Formulare mit Tally

Tally-Formulare werden per iframe eingebettet:

```html
<iframe
  data-tally-src="https://tally.so/embed/[FORM-ID]?alignLeft=1&hideTitle=1&transparentBackground=1&dynamicHeight=1"
  loading="lazy"
  width="100%"
  height="500"
  frameborder="0"
  title="Formular"
  style="border: none;">
</iframe>
<script src="https://tally.so/widgets/embed.js"></script>
```

Tally Settings:
- Self email notifications aktivieren
- Redirect on completion auf danke.html
- Sprache: Deutsch
- Region: EU

## Bestellsystem

- Nur Vorkasse (Überweisung)
- Tally sendet Mail an Betreiber bei neuer Bestellung
- Betreiber antwortet manuell mit IBAN
- Google Sheets Integration für Bestellübersicht
- Kein PayPal nötig (spart Gebühren)

## Rechtliches (Pflicht für DE)

Jede kommerzielle Website braucht:
- **Impressum** (§5 TMG, Name, Adresse, Kontakt, USt-ID/Kleinunternehmer)
- **Datenschutzerklärung** (DSGVO, welche Daten, welche Dienste, Rechte)
- **Widerrufsbelehrung** (bei Sonderanfertigungen: kein Widerrufsrecht gem. §312g BGB)
- Links im Footer auf jeder Seite

## Deployment

```bash
git add .
git commit -m "Beschreibung der Änderung"
git push
```

GitHub Pages baut automatisch. Änderungen sind nach 1-2 Minuten live.
Custom Domain über CNAME-Datei im Repo.

## Wichtig

- Alle Styles inline (kein separates CSS-File nötig)
- Kein JavaScript-Framework
- Kein Cookie-Banner nötig (wenn kein Tracking)
- Kein Node.js, kein npm, kein Build
- Mobile-first responsive (@media max-width: 768px)
- Bilder im images/ Ordner
- IBAN/BIC niemals im Code, nur in Tally/Mail
