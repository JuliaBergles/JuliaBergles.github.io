# Phase 1 — Inventur

Stand: 17. Mai 2026

---

## 1.1 Aktuelle Bestellabwicklung

**Formular-Submission:** Das Formular in `bestellen.html` wird per **mailto-Link** abgesendet.

```javascript
window.location.href = 'mailto:julia@bergles.net?subject=...'
```

- **Kein externer Dienst** (kein Formspree, kein Tally, kein Netlify Forms)
- Die Bestellung wird als E-Mail-Text über das Mail-Programm der Kundin gesendet
- Zusätzlich wird die Bestellung in `localStorage` gespeichert (Key: `eatmoreart-orders`)
- Es gibt ein lokales `dashboard.html` — das liest aus localStorage (nur auf dem eigenen Gerät nutzbar)

**Problem:** Wenn die Kundin kein Mail-Programm konfiguriert hat, geht die Bestellung verloren. Keine automatische Bestätigung an die Kundin.

---

## 1.2 Rechtlicher Stand

### Vorhandene Dateien:
- `datenschutz.html` — **vorhanden und inhaltlich brauchbar**
  - Bezieht sich primär auf die TerraLuna App
  - Erwähnt NICHT: Tally, Bestellformular-Daten, PayPal-Zahlung, Social-Media-Einwilligung
  - Verantwortliche: Julia Bergles, Singoldstraße 5a, 86517 Wehringen
  - E-Mail: info@smacado.de
  - Stand: April 2026
  
- `impressum.html` — **vorhanden und brauchbar**
  - Julia Bergles, Singoldstraße 5a, 86517 Wehringen
  - E-Mail: info@smacado.de, Tel: +49 1511 8515394
  - USt-ID: "wird bei Bedarf ergänzt"
  - Knapp aber funktional

- `agb.html` — vorhanden (nicht gelesen, aber verlinkt)
- `widerruf.html` — vorhanden (nicht gelesen, aber verlinkt)

### Footer-Verlinkung:
- `index.html`: Impressum, AGB, Datenschutz, Widerruf — alle verlinkt ✓
- `eatmoreart.html`: Impressum, AGB, Datenschutzerklärung — verlinkt ✓
- `bestellen.html`: Impressum + Datenschutz verlinkt im Footer ✓

---

## 1.3 Tracking / Cookies

**Keine Tracking-Dienste gefunden:**
- Kein Google Analytics
- Kein Google Tag Manager
- Kein Facebook Pixel
- Kein Hotjar
- Kein Cookie-Banner

Die Website ist tracking-frei. Das ist gut für DSGVO.

---

## 1.4 Aktuelle Preise (aus bestellen.html)

| Produkt | Preis |
|---------|-------|
| Mini-Charm | 10,00 € |
| Kettenanhänger | 12,00 € |
| Schlüsselanhänger | 14,00 € |
| Mit Halskette | +11,00 € |
| Mit Armkette | +9,00 € |
| Geschenkverpackung | +1,00 € |

**In eatmoreart.html stehen andere Preise (veraltet!):**
- "Mini Charms ab 9 Euro" (Angebote-Grid auf index.html)
- "Kettenanhänger ab 14 Euro" (index.html)
- "Schlüsselanhänger ab 17 Euro" (index.html)
- In eatmoreart.html: Mini ab 10€, Ketten ab 12€, Schlüssel ab 14€

**Inkonsistenz:** index.html zeigt andere (höhere) Preise als eatmoreart.html und bestellen.html.

---

## 1.5 Sonstige Befunde

- **E-Mail-Adresse:** `julia@bergles.net` (Bestellungen) vs. `info@smacado.de` (Impressum/Datenschutz)
- **Keine separate CSS-Datei:** Alle Styles sind inline in jeder HTML-Datei
- **Keine JS-Dateien:** Alles inline
- **Dashboard:** `dashboard.html` existiert — liest aus localStorage (nur lokal nutzbar, nicht für echten Betrieb geeignet)
- **Flohmarkt:** `eatmoreart.html` hat ein Flohmarkt-System das ebenfalls aus localStorage liest

---

## Zusammenfassung / Handlungsbedarf

1. **Bestellabwicklung:** mailto-Link ist unzuverlässig → Tally als Lösung
2. **Datenschutz:** Muss um Bestelldaten, Tally, PayPal ergänzt werden
3. **Impressum:** Grundsätzlich okay, ggf. Kleinunternehmerregelung ergänzen
4. **Preise inkonsistent:** index.html zeigt falsche/veraltete Preise
5. **Kein Tracking:** Gut, vereinfacht Datenschutz erheblich
6. **E-Mail:** Klären ob julia@bergles.net oder info@smacado.de oder info@juliabergles.de
