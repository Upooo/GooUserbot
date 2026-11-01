__MODULE__ = "carbon"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴀʀʙᴏɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}carbon</code>
🦠 ᴋᴇᴛ : ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ᴄᴀʀʙᴏɴᴀʀᴀ.</b></blockquote>
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
    text = (
        message.text.split(None, 1)[1]
        if len(message.command) != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.reply("memproses...")
    carbon = await make_carbon(text)
    await ex.edit("uploading...")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"carbonised by :{client.me.mention}",
        ),
    )
    carbon.close()
