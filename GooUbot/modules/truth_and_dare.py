__MODULE__ = "truth dare"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴛʀᴜᴛʜ & ᴅᴀʀᴇ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}dare</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴄᴏʙᴀ ᴛᴀɴᴛᴀɴɢᴀɴ ᴀᴄᴀᴋ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}truth</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴄᴏʙᴀ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴋᴇᴊᴜᴊᴜʀᴀɴ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}apakah</code>
🦠 ᴋᴇᴛ : ᴘᴇʀᴛᴀɴʏᴀᴀɴ ʏᴀɴɢ ᴀᴋᴀɴ ᴅɪᴊᴀᴡᴀʙ ʏᴀ/ᴛɪᴅᴀᴋ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}bagaimana</code>
🦠 ᴋᴇᴛ : ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴅᴇɴɢᴀɴ ᴊᴀᴡᴀʙᴀɴ ᴀᴄᴀᴋ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}kenapa</code>
🦠 ᴋᴇᴛ : ᴘᴇʀᴛᴀɴʏᴀᴀɴ "ᴋᴇɴᴀᴘᴀ" ᴅᴇɴɢᴀɴ ᴊᴀᴡᴀʙᴀɴ ᴀᴄᴀᴋ.</blockquote>
"""

import asyncio
import random

from GooUbot.modules import truth_and_dare_string as tod

from GooUbot import *


@PY.UBOT("apakah")
async def apakah(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.AP)}")


@PY.UBOT("kenapa")
async def kenapa(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.KN)}")


@PY.UBOT("bagaimana")
async def bagaimana(client, message):
    split_text = message.text.split(None, 1)
    if len(split_text) < 2:
        return await message.reply("Berikan saya pertanyaan 😐")
    cot = split_text[1]
    await message.reply(f"{random.choice(tod.BG)}")


@PY.UBOT("dare")
async def dare(client, message):
    try:        
        await message.edit(f"{random.choice(tod.DARE)}")
    except BaseException:
        pass

@PY.UBOT("truth")
async def truth(client, message):
    try:
        await message.edit(f"{random.choice(tod.TRUTH)}")
    except Exception:
        pass


