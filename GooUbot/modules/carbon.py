__MODULE__ = "carbon"
__HELP__ = """
<blockquote><b>Carbon</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}carbon</code> [teks/reply]
Buat image code style Carbon.</blockquote>
"""

import asyncio
from io import BytesIO

from GooUbot import *


async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    session = await get_aiosession()
    async with session.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@PY.UBOT("carbon")
@PY.TOP_CMD
async def carbon_func(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    text = None
    if len(message.command) > 1:
        text = message.text.split(None, 1)[1]
    elif message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption

    if not text:
        return await message.reply(f"{ggl}<code>{message.command[0]} [teks/reply]</code>")

    status = await message.reply(f"{prs}Processing...")
    try:
        carbon = await make_carbon(text)
        await status.edit(f"{prs}Uploading...")
        await client.send_photo(
            message.chat.id,
            carbon,
            caption=f"Carbon by {client.me.mention}",
        )
        await status.delete()
        carbon.close()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
