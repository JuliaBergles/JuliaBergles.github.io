#!/usr/bin/env python3
"""
build_carousel.py v3 — Instagram-Karussell (1080x1350)
Design-Standards: Safe Area, deutsche Typografie, Kontrast-Check,
Schusterjungen-Vermeidung, konsistentes Layout.
"""

import sys, os, textwrap, re, unicodedata

try:
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

from PIL import Image, ImageDraw, ImageFont

# === KONSTANTEN ===
W, H = 1080, 1350
SAFE_X, SAFE_Y = 80, 100  # Safe Area
CONTENT_W = W - 2 * SAFE_X  # 920
CONTENT_H = H - 2 * SAFE_Y  # 1150

# === FARBEN ===
BEIGE = (244, 237, 228)
PEACH = (235, 210, 195)
DARK = (58, 46, 42)
MUTED = (122, 111, 101)
ACCENT = (155, 91, 85)
CREAM = (250, 244, 235)
CTA_BG = (50, 44, 38)
LOGO_LIGHT = (170, 160, 150)
LOGO_DARK = (140, 132, 122)

# === TYPOGRAFIE ===
def _find(paths, fallback_size=32):
    for p in paths:
        if os.path.exists(p):
            return p
    return None

SERIF_BOLD_PATH = _find([
    "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "/Library/Fonts/Georgia Bold.ttf",
])
SERIF_PATH = _find([
    "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "/Library/Fonts/Georgia.ttf",
])
SERIF_ITALIC_PATH = _find([
    "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
])
SANS_PATH = _find([
    "/System/Library/Fonts/Helvetica.ttc",
    "/System/Library/Fonts/Supplemental/Arial.ttf",
])
SANS_BOLD_PATH = _find([
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/System/Library/Fonts/HelveticaNeue.ttc",
])

def font(path, size):
    if path and os.path.exists(path):
        return ImageFont.truetype(path, size)
    return ImageFont.load_default()

# === DEUTSCHE TYPOGRAFIE ===
def fix_typo(text):
    """Deutsche Typografie-Regeln anwenden."""
    t = text
    t = t.replace('...', '\u2026')         # Auslassungspunkte
    t = t.replace(' - ', ' \u2013 ')       # Gedankenstrich
    t = t.replace('"', '\u201E', 1)        # Öffnendes Anführungszeichen
    t = t.replace('"', '\u201C')           # Schließendes
    t = re.sub(r"(?<=[a-zäöüß])'(?=[a-zäöüß])", '\u2019', t)  # Apostroph
    return t

# === ZEILENUMBRUCH (keine Schusterjungen) ===
def smart_wrap(text, max_chars):
    """Umbrechen ohne einzelne Wörter am Ende."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        if len(test) <= max_chars:
            current = test
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        # Schusterjungen-Check: letztes Wort allein?
        if len(lines) > 0 and len(current.split()) == 1 and len(current) < 8:
            # Letztes Wort der vorigen Zeile umhängen
            prev = lines[-1]
            prev_words = prev.split()
            if len(prev_words) > 2:
                move = prev_words[-1]
                lines[-1] = " ".join(prev_words[:-1])
                current = move + " " + current
        lines.append(current)
    return lines

# === TEXT ZEICHNEN ===
def draw_text_block(draw, lines, x_center, y_start, fnt, color, line_height=1.4):
    """Zentrierten Textblock zeichnen. Gibt y_end zurück."""
    y = y_start
    for line in lines:
        line = fix_typo(line)
        bbox = draw.textbbox((0, 0), line, font=fnt)
        tw = bbox[2] - bbox[0]
        th = bbox[3] - bbox[1]
        x = x_center - tw // 2
        draw.text((x, y), line, fill=color, font=fnt)
        y += int(th * line_height)
    return y

def draw_text_centered(draw, text, y, fnt, color, max_chars=22, line_height=1.4):
    """Text umbrechen und zentriert zeichnen."""
    lines = smart_wrap(text, max_chars)
    return draw_text_block(draw, lines, W // 2, y, fnt, color, line_height)

# === BILD EINPASSEN ===
def fit_image(path, w, h):
    img = Image.open(path).convert('RGB')
    ratio = max(w / img.width, h / img.height)
    img = img.resize((int(img.width * ratio), int(img.height * ratio)), Image.LANCZOS)
    cx, cy = (img.width - w) // 2, (img.height - h) // 2
    return img.crop((cx, cy, cx + w, cy + h))

# === LOGO ===
def add_logo(draw, color=LOGO_LIGHT):
    fnt = font(SANS_PATH, 22)
    text = "juliabergles"
    bbox = draw.textbbox((0, 0), text, font=fnt)
    tw = bbox[2] - bbox[0]
    draw.text((W // 2 - tw // 2, H - SAFE_Y - 10), text, fill=color, font=fnt)

# === SLIDE-TYPEN ===

def slide_hook(text_lines, bg_path=None):
    """Slide 1: Große Headline, optional Foto-Hintergrund."""
    if bg_path:
        img = fit_image(bg_path, W, H)
        overlay = Image.new('RGBA', (W, H), (244, 237, 228, 185))
        img = img.convert('RGBA')
        img = Image.alpha_composite(img, overlay).convert('RGB')
    else:
        img = Image.new('RGB', (W, H), BEIGE)
    draw = ImageDraw.Draw(img)

    fnt = font(SERIF_BOLD_PATH or SERIF_PATH, 76)
    full = " ".join(l for l in text_lines if l.strip())

    # Optisch leicht über Mitte
    lines = smart_wrap(full, 16)
    block_h = len(lines) * int(76 * 1.15)
    y = (H // 2) - (block_h // 2) - 40

    draw_text_block(draw, lines, W // 2, y, fnt, DARK, line_height=1.15)

    # Dezente Linie
    line_y = y + block_h + 30
    draw.line([(W//2 - 35, line_y), (W//2 + 35, line_y)], fill=ACCENT, width=2)

    add_logo(draw, LOGO_LIGHT)
    return img


def slide_text(text_lines, bg=BEIGE):
    """Text-Slide: Headline fett, Body normal."""
    img = Image.new('RGB', (W, H), bg)
    draw = ImageDraw.Draw(img)

    all_text = [l.strip() for l in text_lines if l.strip()]
    if not all_text:
        return img

    h_fnt = font(SANS_BOLD_PATH or SANS_PATH, 38)
    b_fnt = font(SANS_PATH, 32)

    # Block-Höhe schätzen für vertikale Zentrierung
    total_lines = 0
    for i, t in enumerate(all_text):
        mc = 24 if i == 0 else 34
        total_lines += len(smart_wrap(t, mc))
    est_h = total_lines * 52
    y = max(SAFE_Y + 40, (H - est_h) // 2 - 30)

    for i, text in enumerate(all_text):
        if i == 0:
            y = draw_text_centered(draw, text, y, h_fnt, DARK, max_chars=24, line_height=1.3)
            y += 100  # Großer Abstand Headline -> Body
        else:
            y = draw_text_centered(draw, text, y, b_fnt, MUTED, max_chars=34, line_height=1.4)
            y += 20

    add_logo(draw)
    return img


def slide_photo_text(text_lines, bg_path):
    """Foto mit halbtransparenter Textbox im unteren Drittel."""
    img = fit_image(bg_path, W, H)

    # Textbox als Overlay
    all_text = [l.strip() for l in text_lines if l.strip()]
    box_h = min(480, 80 + len(all_text) * 65)
    box_y = H - box_h - SAFE_Y - 20
    box_x = SAFE_X
    box_w = W - 2 * SAFE_X

    overlay = Image.new('RGBA', (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(overlay)
    od.rounded_rectangle(
        [box_x, box_y, box_x + box_w, box_y + box_h],
        radius=16, fill=(250, 244, 235, 225)
    )
    img = img.convert('RGBA')
    img = Image.alpha_composite(img, overlay).convert('RGB')
    draw = ImageDraw.Draw(img)

    h_fnt = font(SANS_BOLD_PATH or SANS_PATH, 32)
    b_fnt = font(SANS_PATH, 28)

    y = box_y + 35
    for i, text in enumerate(all_text):
        f = h_fnt if i == 0 else b_fnt
        c = DARK if i == 0 else MUTED
        y = draw_text_centered(draw, text, y, f, c, max_chars=30, line_height=1.35)
        y += 10

    add_logo(draw, (180, 170, 160))
    return img


def slide_quote(text_lines):
    """Zitat-Slide: kursiv, zentriert, Rotgrau-Akzent."""
    img = Image.new('RGB', (W, H), BEIGE)
    draw = ImageDraw.Draw(img)

    fnt = font(SERIF_ITALIC_PATH or SERIF_PATH, 42)
    full = " ".join(l.strip() for l in text_lines if l.strip())

    lines = smart_wrap(full, 24)
    block_h = len(lines) * int(42 * 1.4)
    y = (H // 2) - (block_h // 2) - 20

    draw_text_block(draw, lines, W // 2, y, fnt, ACCENT, line_height=1.4)

    add_logo(draw)
    return img


def slide_cta(text_lines):
    """CTA-Slide: dunkler Hintergrund, ruhig, klar."""
    img = Image.new('RGB', (W, H), CTA_BG)
    draw = ImageDraw.Draw(img)

    all_text = [l.strip() for l in text_lines if l.strip()]

    h_fnt = font(SERIF_BOLD_PATH or SERIF_PATH, 44)
    b_fnt = font(SANS_PATH, 26)
    s_fnt = font(SANS_PATH, 22)

    # CTA-Text optisch zentrieren
    y = H // 2 - 180

    for i, line in enumerate(all_text):
        if line.startswith('@') or line.startswith('julia'):
            draw_text_centered(draw, line, y, s_fnt, LOGO_DARK, max_chars=36, line_height=1.5)
            y += 38
        elif i < 3:
            y = draw_text_centered(draw, line, y, h_fnt, CREAM, max_chars=22, line_height=1.2)
            y += 12
        else:
            y = draw_text_centered(draw, line, y, b_fnt, LOGO_DARK, max_chars=34, line_height=1.45)
            y += 10

    # Dezente Linie
    draw.line([(W//2 - 25, y + 20), (W//2 + 25, y + 20)], fill=ACCENT, width=1)

    # Logo unten
    logo_fnt = font(SANS_PATH, 22)
    logo_text = "juliabergles"
    bbox = draw.textbbox((0, 0), logo_text, font=logo_fnt)
    tw = bbox[2] - bbox[0]
    draw.text((W // 2 - tw // 2, H - SAFE_Y - 10), logo_text, fill=LOGO_DARK, font=logo_fnt)

    return img


# === QUALITÄTS-CHECK ===
def check_slide(num, text_lines):
    warnings = []
    for line in text_lines:
        if len(line) > 40:
            warnings.append(f"Slide {num}: Zeile zu lang ({len(line)} Zeichen): {line[:30]}...")
        if '"' in line or "'" in line:
            warnings.append(f"Slide {num}: Englische Anführungszeichen gefunden")
    return warnings


# === POST BAUEN ===
def build_post(post_dir):
    brief_path = os.path.join(post_dir, "brief.md")
    output_dir = os.path.join(post_dir, "output")
    input_dir = os.path.join(post_dir, "input")
    # Resolve symlinks
    if os.path.islink(input_dir):
        input_dir = os.path.realpath(input_dir)
    os.makedirs(output_dir, exist_ok=True)

    if not os.path.exists(brief_path):
        print(f"Kein brief.md in {post_dir}")
        return

    with open(brief_path, 'r') as f:
        content = f.read()

    # Parse
    slides = []
    current_slide = None
    current_lines = []
    caption_lines = []
    in_caption = False

    for line in content.split('\n'):
        if line.startswith('### Slide'):
            if current_slide and current_lines:
                slides.append((current_slide, [l for l in current_lines if l.strip()]))
            current_slide = line.strip('# ').strip()
            current_lines = []
            in_caption = False
        elif line.startswith('## CAPTION'):
            if current_slide and current_lines:
                slides.append((current_slide, [l for l in current_lines if l.strip()]))
            current_slide = None
            in_caption = True
        elif in_caption:
            caption_lines.append(line)
        elif current_slide:
            current_lines.append(line)

    if current_slide and current_lines:
        slides.append((current_slide, [l for l in current_lines if l.strip()]))

    # Bilder
    images = []
    if os.path.exists(input_dir):
        for f in sorted(os.listdir(input_dir)):
            if f.startswith('.') or os.path.isdir(os.path.join(input_dir, f)):
                continue
            if f.lower().endswith(('.jpg', '.jpeg', '.png', '.heic')):
                images.append(os.path.join(input_dir, f))

    print(f"  {len(slides)} Slides, {len(images)} Bilder")
    all_warnings = []

    for i, (title, lines) in enumerate(slides):
        num = i + 1
        warns = check_slide(num, lines)
        all_warnings.extend(warns)

        if 'Hook' in title or num == 1:
            bg = images[0] if images else None
            img = slide_hook(lines, bg)

        elif 'CTA' in title or num == len(slides):
            img = slide_cta(lines)

        elif num == len(slides) - 1:
            img = slide_quote(lines)

        elif num % 3 == 0 and images:
            idx = min(num, len(images) - 1)
            img = slide_photo_text(lines, images[idx])

        elif num % 5 == 0:
            img = slide_text(lines, bg=PEACH)

        else:
            img = slide_text(lines)

        # Warnung im Dateinamen?
        suffix = ""
        slide_warns = [w for w in warns if f"Slide {num}" in w]
        if slide_warns:
            suffix = "_PRUEFEN"
            for w in slide_warns:
                print(f"  WARNUNG: {w}")

        path = os.path.join(output_dir, f"slide_{num:02d}{suffix}.png")
        img = img.convert('RGB')
        img.save(path, 'PNG')
        print(f"  Slide {num}: OK")

    # Caption
    if caption_lines:
        cap = os.path.join(output_dir, "caption.txt")
        with open(cap, 'w') as f:
            f.write('\n'.join(caption_lines).strip())
        print(f"  Caption gespeichert")

    if all_warnings:
        print(f"\n  {len(all_warnings)} Warnung(en) — bitte prüfen")
    else:
        print(f"  Alle Checks bestanden")

    print(f"  Fertig! {len(slides)} Slides in {output_dir}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Verwendung: python3 tools/build_carousel.py posts/post_XX_thema")
        sys.exit(1)
    d = sys.argv[1]
    if not os.path.isabs(d):
        d = os.path.join(os.getcwd(), d)
    print(f"Baue: {os.path.basename(d)}")
    build_post(d)
