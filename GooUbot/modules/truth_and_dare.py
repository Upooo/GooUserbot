__MODULE__ = "truthdare"
__HELP__ = """
<blockquote><b>Truth & Dare</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}truth</code> — pertanyaan kejujuran
<code>{0}dare</code> — tantangan acak
<code>{0}apakah</code> [tanya] — jawab ya/tidak
<code>{0}bagaimana</code> [tanya]
<code>{0}kenapa</code> [tanya]</blockquote>
"""

import random

from GooUbot import *
from GooUbot.modules import truth_and_dare_string as tod


@PY.UBOT("apakah")
@PY.TOP_CMD
async def apakah(client, message):
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [pertanyaan]</code>")
    await message.reply(random.choice(tod.AP))


@PY.UBOT("kenapa")
@PY.TOP_CMD
async def kenapa(client, message):
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [pertanyaan]</code>")
    await message.reply(random.choice(tod.KN))


@PY.UBOT("bagaimana")
@PY.TOP_CMD
async def bagaimana(client, message):
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [pertanyaan]</code>")
    await message.reply(random.choice(tod.BG))


@PY.UBOT("dare")
@PY.TOP_CMD
async def dare(client, message):
    try:
        await message.edit(random.choice(tod.DARE))
    except Exception:
        await message.reply(random.choice(tod.DARE))


@PY.UBOT("truth")
@PY.TOP_CMD
async def truth(client, message):
    try:
        await message.edit(random.choice(tod.TRUTH))
    except Exception:
        await message.reply(random.choice(tod.TRUTH))
