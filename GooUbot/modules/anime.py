__MODULE__ = "anime"
__HELP__ = """
<blockquote><b>Anime</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}waifu</code> — foto waifu random
<code>{0}anime</code> [query] — foto karakter
Query: keneki, megumin, yotsuba, shinomiya, yumeko, tsunade, kagura, madara, itachi, akira, toukachan, sasuke, cicho</blockquote>
"""

from io import BytesIO

import requests
from pyrogram.enums import ChatAction

from GooUbot import *

URLS = {
    "keneki": "https://api.botcahx.eu.org/api/anime/keneki?apikey=moire",
    "megumin": "https://api.botcahx.eu.org/api/anime/megumin?apikey=moire",
    "yotsuba": "https://api.botcahx.eu.org/api/anime/yotsuba?apikey=moire",
    "shinomiya": "https://api.botcahx.eu.org/api/anime/shinomiya?apikey=moire",
    "yumeko": "https://api.botcahx.eu.org/api/anime/yumeko?apikey=moire",
    "tsunade": "https://api.botcahx.eu.org/api/anime/tsunade?apikey=moire",
    "kagura": "https://api.botcahx.eu.org/api/anime/kagura?apikey=moire",
    "madara": "https://api.botcahx.eu.org/api/anime/madara?apikey=moire",
    "itachi": "https://api.botcahx.eu.org/api/anime/itachi?apikey=moire",
    "akira": "https://api.botcahx.eu.org/api/anime/akira?apikey=moire",
    "toukachan": "https://api.botcahx.eu.org/api/anime/toukachan?apikey=moire",
    "cicho": "https://api.botcahx.eu.org/api/anime/chiho?apikey=moire",
    "sasuke": "https://api.botcahx.eu.org/api/anime/sasuke?apikey=moire",
}


@PY.UBOT("waifu")
@PY.TOP_CMD
async def anime_cmd(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Processing...", quote=True)
    try:
        photo = API.waifu()
        await message.reply_photo(photo, quote=True)
        await status.delete()
    except Exception as error:
        await status.edit(f"{ggl}<code>{error}</code>")


@PY.UBOT("anime")
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
        photo.name = "anime.jpg"
        await client.send_photo(message.chat.id, photo)
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
