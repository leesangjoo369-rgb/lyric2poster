
from PIL import Image, ImageDraw, ImageFont
import textwrap


def create_poster(song_title, artist, style="Minimal"):
    width, height = 1080, 1350

    backgrounds = {
        "Minimal": (235, 230, 220),
        "Vintage": (190, 160, 125),
        "Dreamy": (190, 190, 225),
        "Pop Art": (245, 120, 130),
    }

    background = backgrounds.get(style, backgrounds["Minimal"])

    image = Image.new("RGB", (width, height), background)
    draw = ImageDraw.Draw(image)

    try:
        title_font = ImageFont.truetype(
            "DejaVuSans-Bold.ttf", 75
        )
        artist_font = ImageFont.truetype(
            "DejaVuSans.ttf", 40
        )
    except OSError:
        title_font = ImageFont.load_default()
        artist_font = ImageFont.load_default()

    # Decorative circle
    draw.ellipse(
        (290, 180, 790, 680),
        fill=(80, 75, 110)
    )

    # Song title
    title_lines = textwrap.wrap(song_title, width=18)
    y = 760

    for line in title_lines:
        draw.text(
            (100, y),
            line,
            fill=(30, 30, 30),
            font=title_font
        )
        y += 100

    # Artist name
    draw.text(
        (105, y + 35),
        artist,
        fill=(60, 60, 60),
        font=artist_font
    )

    return image
