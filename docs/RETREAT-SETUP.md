# Retreat-Seite — Setup-Anleitung

**Datei:** `retreat.html`
**URL nach Deploy:** `juliabergles.de/retreat.html`

Die Seite läuft **sofort** als statische HTML-Seite — ohne Setup. Formular schickt dann aber nur `mailto:`-Mails und die Städte-Abstimmung läuft lokal im Browser (jede Besucherin sieht nur ihre eigene Stimme).

Um das richtig live zu nehmen, zwei Dinge einrichten:

---

## 1. Formular live schalten (Formspree)

Momentan öffnet das Formular eine Mail an `julia@bergles.net` beim Absenden (Fallback). Für ein echtes Formular ohne Mail-Programm-Öffnung:

1. Account auf **[formspree.io](https://formspree.io/)** anlegen (Free-Tier reicht am Anfang).
2. Neues Formular erstellen, Ziel-E-Mail `julia@bergles.net`.
3. Formspree gibt dir eine URL wie `https://formspree.io/f/xkgrabcd`.
4. In `retreat.html` oben im `<script>`-Block den Wert eintragen:
   ```js
   formspreeUrl: "https://formspree.io/f/xkgrabcd",
   ```
5. Commit + Push → fertig.

**Was Formspree automatisch macht:**
- Spam-Schutz (reCaptcha, Honeypot haben wir zusätzlich eingebaut)
- Mail-Benachrichtigung an dich bei jeder Anmeldung
- Export der Antworten als CSV

**Falls Formspree Grenzen erreicht (50 Submissions/Monat Free-Tier)** → entweder Paid-Tier (ca. 10 $/Monat für 500) oder Alternative: `Netlify Forms` (wenn du mal auf Netlify umziehst), `Basin`, `Getform`.

---

## 2. Städte-Abstimmung live mit Supabase

So lange `supabaseUrl` und `supabaseAnonKey` leer sind, zählt die Abstimmung nur lokal im Browser der Besucherin — nicht gemeinsam sichtbar. Für echte Abstimmung über alle Besucher hinweg:

### Schritt 1: Supabase-Projekt anlegen

1. Account auf **[supabase.com](https://supabase.com/)** erstellen (Free-Tier reicht hier locker — bis 500 MB DB).
2. Neues Projekt erstellen. Region EU wählen (für DSGVO).
3. Nach Setup: **Project URL** und **anon public key** notieren (unter `Project Settings → API`).

### Schritt 2: Tabelle anlegen

Im Supabase-Dashboard → `SQL Editor` → folgendes Script ausführen:

```sql
-- Tabelle für Städte-Stimmen
create table public.retreat_votes (
  id uuid primary key default gen_random_uuid(),
  city text not null,
  would_attend boolean default false,
  voter_token text not null,
  created_at timestamptz default now()
);

-- Doppelte Stimmen pro Browser verhindern
create unique index retreat_votes_token_idx on public.retreat_votes (voter_token);

-- RLS aktivieren
alter table public.retreat_votes enable row level security;

-- Jeder darf einfügen
create policy "allow insert for all"
  on public.retreat_votes
  for insert
  to anon
  with check (true);

-- Jeder darf aggregierte Stimmen lesen (nur die Spalte city, keine Tokens)
create policy "allow read city for all"
  on public.retreat_votes
  for select
  to anon
  using (true);
```

### Schritt 3: Keys in `retreat.html` eintragen

Oben im `<script>`-Block:

```js
supabaseUrl: "https://xxxxxxxx.supabase.co",
supabaseAnonKey: "eyJhbGciOi... (der anon public key)"
```

Der **anon key** ist OK im Browser-Code — er ist mit `public` gekennzeichnet. Niemals aber den **service_role key** ins Frontend!

### Schritt 4: Testen

- Lade die Seite in zwei verschiedenen Browsern/Geräten.
- Stimme je einmal ab.
- Beide sollten die Gesamtzahl sehen.

### Was die Besucherinnen sehen

- Nur die aggregierten Zahlen (z. B. "Berlin · 7 · 23 %").
- Keine persönlichen Daten.
- Pro Browser nur eine Stimme (Token im `localStorage`).

### Später: Admin-Übersicht

Fürs Admin-Dashboard (Antworten auswerten) kannst du direkt im Supabase-Dashboard unter `Table Editor → retreat_votes` jederzeit alle Stimmen sehen. Separate Admin-Seite ist noch nicht gebaut — brauchst du erst, wenn mehrere Städte dazukommen.

---

## 3. Checkliste vor dem richtigen Livegang

- [ ] Formspree-URL eingetragen (sonst Mail-Fallback)
- [ ] Supabase-Keys eingetragen (sonst Browser-lokale Abstimmung)
- [ ] Stornierungsbedingungen in der FAQ ergänzen (aktuell Platzhalter!)
- [ ] AGB / Datenschutz prüfen, ob Retreat erwähnt werden muss
- [ ] Echte Fotos ins Hero + an die Spots mit Platzhalter-Covern
- [ ] Instagram-Post / Newsletter-Mail mit Link `juliabergles.de/retreat.html`

---

## 4. Konfiguration — häufige Änderungen

Alle wichtigen Werte stehen ganz oben in `retreat.html` im `window.RETREAT_CONFIG`:

```js
window.RETREAT_CONFIG = {
  ort:        "Wehringen bei Augsburg",
  adresse:    "Singoldstraße 5a, 86517 Wehringen",
  datum:      "21. November 2026",
  datumIso:   "2026-11-21",
  beginn:     "15:00 Uhr",
  preis:      "99 €",
  maxTeilnehmer: 12,
  uebernachtung: "15 € (inkl. Frühstück)",
  ...
};
```

Datum, Ort, Preis, Teilnehmerzahl ändern → hier und einmal unten im Formular-Radio-Button-Text. Alles andere zieht sich der JavaScript-Code automatisch.
