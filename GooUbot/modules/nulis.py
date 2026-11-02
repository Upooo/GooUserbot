__MODULE__ = "nulis"
__HELP__ = """
<blockquote><b>Nulis</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}nulis</code> [teks/reply]
Tulis teks di template buku (tulisan tangan).</blockquote>
"""

import os

from PIL import Image, ImageDraw, ImageFont

from GooUbot import *


def text_set(text):
    lines = []
    for line in text.split("\n"):
        if len(line) <= 55:
            lines.append(line)
        else:
            k = (len(line) // 55) + 1
            for z in range(k):
                lines.append(line[z * 55 : (z + 1) * 55])
    return lines[:25]


@PY.UBOT("nulis")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
        if not text:
            return await message.reply(f"{ggl}Reply ke teks/caption.")
    elif len(message.command) > 1:
        text = message.text.split(None, 1)[1]
    else:
        return await message.reply(f"{ggl}<code>{message.command[0]} [teks/reply]</code>")

    status = await message.reply(f"{prs}Menulis...")
    out = f"nulis_{message.from_user.id}.jpg"
    try:
        img = Image.open("storage/template.jpg")
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype("storage/assfont.ttf", 30)
        x, y = 150, 140
        lines = text_set(text)
        try:
            line_height = font.getbbox("hg")[3]
        except Exception:
            line_height = 30

        for line in lines:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y += line_height - 5

        img.save(out)
        await message.reply_photo(photo=out)
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
    finally:
        if os.path.exists(out):
            os.remove(out)
