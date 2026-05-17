# Tally Setup — Schritt-für-Schritt

## Was ist Tally?

Tally (tally.so) ist ein Formular-Tool aus der EU. Kostenlos, DSGVO-konform, Server in Deutschland.
Du bekommst: Formular + Dashboard + automatische Mails — alles in einem.

---

## SETUP (einmalig, ca. 30 Minuten)

### 1. Account anlegen

1. Gehe auf https://tally.so
2. Registriere dich mit `julia@bergles.net`
3. Bestätige deine E-Mail

### 2. Neues Formular anlegen

Klicke "Create form" → Titel: **"Wear Your Healing — Bestellung"**

### 3. Felder anlegen (Reihenfolge wichtig!)

---

#### BLOCK: PERSÖNLICHES

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Vor- und Nachname | Short text | Ja |
| E-Mail-Adresse | Email | Ja |
| Telefonnummer | Phone | Nein |

---

#### BLOCK: LIEFERADRESSE

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Straße + Hausnummer | Short text | Ja |
| PLZ | Short text | Ja |
| Ort | Short text | Ja |
| Land | Dropdown: Deutschland, Österreich, Schweiz, Sonstiges | Ja |

---

#### BLOCK: DEINE BESTELLUNG

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Charm-Typ | Multiple Choice (single): Mini-Charm 10€, Ketten-Charm 11€, Schlüssel-Charm 12€ | Ja |
| Mit Schmuckstück? | Multiple Choice (single): Nur Charm, Mit Armkette (+14€), Mit Halskette (+18€) | Ja |
| Welche Farbe? | Multiple Choice (single): Gold, Silber, Rosé | Ja |
| Welche Größe? | Multiple Choice (single): Klein (ca. 1,8cm), Mittel (ca. 2,0cm), Groß (ca. 2,2cm) | Ja |
| Welches Lebensmittel oder Wort soll auf dem Charm sein? | Short text | Ja |

---

#### BLOCK: DEINE GESCHICHTE (optional)

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Hat dein Charm eine Geschichte? Magst du sie mit mir teilen? | Long text | Nein |

**Bedingte Logik:** NUR anzeigen wenn das Geschichte-Feld ausgefüllt ist:

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Darf Julia deine Geschichte anonym auf Social Media teilen? | Multiple Choice: "Ja, gerne anonym" / "Nein, lieber nicht" (Default: Nein) | Ja (wenn sichtbar) |

---

#### BLOCK: SOCIAL MEDIA

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Darf Julia ein Video vom Designprozess deines Charms auf Social Media posten? | Multiple Choice: "Ja, gerne" / "Nein, lieber nicht" (Default: Nein) | Ja |

---

#### BLOCK: ZAHLUNGSMETHODE

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Wie möchtest du bezahlen? | Multiple Choice: "Vorkasse per Überweisung (empfohlen)" / "PayPal" | Ja |

---

#### BLOCK: BEMERKUNG (optional)

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Möchtest du mir noch etwas mitteilen? | Long text | Nein |

---

#### BLOCK: PFLICHTABFRAGEN

| Feld | Typ | Pflicht? |
|------|-----|----------|
| Ich habe die Datenschutzerklärung gelesen und stimme zu | Checkbox | Ja |
| Ich verstehe, dass bei Vorkasse erst nach Zahlungseingang produziert und versendet wird | Checkbox | Ja |

---

### 4. Einstellungen in Tally

#### a) Bestätigungs-Mail an Kundin
- Settings → "After submission" → "Send confirmation email"
- Aktivieren
- Subject: `Deine Bestellung bei Wear Your Healing`
- Body: Siehe Datei `notes/03-mail-kundin.md`

#### b) Benachrichtigung an Julia
- Settings → Notifications → "Email notification"
- E-Mail: `julia@bergles.net`
- Aktivieren

#### c) Optional: Google Sheets Integration
- Settings → Integrations → Google Sheets
- Verbinden (kostenlos) → jede Bestellung landet als Zeile in einer Tabelle

#### d) Datenschutz
- Settings → Data → Region: "EU" wählen
- Tally setzt keine eigenen Tracking-Cookies

### 5. Form veröffentlichen

- Klicke "Publish"
- Kopiere die Form-URL (z.B. `https://tally.so/r/abc123`)
- Diese URL brauchst du für Phase 4

---

## Was kostet Tally?

- **Free Plan:** Unbegrenzte Formulare, unbegrenzte Submissions
- Bestätigungs-Mails: kostenlos
- Bedingte Logik: kostenlos
- EU-Server: kostenlos

Du brauchst keinen bezahlten Plan.

---

## Nächster Schritt

Wenn du das Formular angelegt hast, schick mir die Tally-URL.
Dann bette ich es in `bestellen.html` ein.
