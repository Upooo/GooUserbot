__MODULE__ = "wallpaper"
__HELP__ = """
<blockquote><b>Wallpaper</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}wall</code> [query]
Query: teknologi, aesthetic, katakata, heker, anjing, hp, gamer, progaming, chuky, kucing</blockquote>
"""

from io import BytesIO

import requests
from pyrogram.enums import ChatAction

from GooUbot import *

URLS = {
    "teknologi": "https://api.botcahx.eu.org/api/wallpaper/teknologi?apikey=moire",
    "aesthetic": "https://api.botcahx.eu.org/api/wallpaper/aesthetic?apikey=moire",
    "katakata": "https://api.botcahx.eu.org/api/wallpaper/katakata?apikey=moire",
    "heker": "https://api.botcahx.eu.org/api/wallpaper/hacker?apikey=moire",
    "anjing": "https://api.botcahx.eu.org/api/wallpaper/anjing?apikey=moire",
    "hp": "https://api.botcahx.eu.org/api/wallpaper/wallhp?apikey=moire",
    "gamer": "https://api.botcahx.eu.org/api/wallpaper/gaming?apikey=moire",
    "progaming": "https://api.botcahx.eu.org/api/wallpaper/programing?apikey=moire",
    "chuky": "https://api.botcahx.eu.org/api/wallpaper/boneka-chucky?apikey=moire",
    "kucing": "https://api.botcahx.eu.org/api/wallpaper/kucing?apikey=moire",
}


@PY.UBOT("wall")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    query = message.command[1].lower() if len(message.command) > 1 else None
    if query not in URLS:
        valid = ", ".join(URLS.keys())
        return await message.reply(f"{ggl}Query: <code>{valid}</code>")

    status = await message.reply(f"{prs}Processing...")
    try:
        await client.send_chat_action(message.chat.id, ChatAction.UPLOAD_PHOTO)
        response = requests.get(URLS[query], timeout=20)
        response.raise_for_status()

        photo = BytesIO(response.content)
        photo.name = "wall.jpg"
        await client.send_photo(message.chat.id, photo)
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
