__MODULE__ = "ping"
__HELP__ = """
<blockquote><b>Ping</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}ping</code>
Cek latency userbot ke server Telegram.</blockquote>
"""

from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping

from GooUbot import *


@PY.UBOT("ping|pink")
@PY.IDOL("cpink|ceponk|sepong")
@PY.TOP_CMD
async def _(client, message):
    start = datetime.now()
    try:
        await client.invoke(Ping(ping_id=0))
    except Exception:
        pass
    end = datetime.now()

    delta_ms = round((end - start).total_seconds() * 1000, 2)
    uptime = await get_time((time() - start_time))

    pong = await EMO.PING(client)
    tion = await EMO.MENTION(client)
    yubot = await EMO.UBOT(client)

    text = f"""
<blockquote><b>{pong}Ping:</b> <code>{delta_ms} ms</code>
<b>{tion}User:</b> {client.me.mention}
<b>{yubot}Bot:</b> {bot.me.mention}
<b>Uptime:</b> <code>{uptime}</code></blockquote>
""".strip()

    await message.reply(text)
