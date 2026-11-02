__MODULE__ = "salam"
__HELP__ = """
<blockquote><b>Salam</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}p</code> — Assalamu'alaikum
<code>{0}pe</code> — Assalamualaikum Warahmatullahi Wabarakatuh
<code>{0}l</code> — Wa'alaikumsalam
<code>{0}wl</code> — Wa'alaikumsalam Warahmatullahi Wabarakatuh
<code>{0}as</code> — Salam dulu</blockquote>
"""

from GooUbot import *


@PY.UBOT("p")
@PY.TOP_CMD
async def _(client, message):
    await message.edit("Assalamu'alaikum")


@PY.UBOT("pe")
@PY.TOP_CMD
async def _(client, message):
    await message.edit("Assalamualaikum Warahmatullahi Wabarakatuh")


@PY.UBOT("l")
@PY.TOP_CMD
async def _(client, message):
    await message.edit("Wa'alaikumsalam")


@PY.UBOT("wl")
@PY.TOP_CMD
async def _(client, message):
    await message.edit("Wa'alaikumsalam Warahmatullahi Wabarakatuh")


@PY.UBOT("as")
@PY.TOP_CMD
async def _(client, message):
    await message.edit("Salam dulu!")
