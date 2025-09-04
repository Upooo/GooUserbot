__MODULE__ = "colong"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏʟᴏɴɢ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}colong</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴍʙɪʟ ᴍᴇᴅɪᴀ/ᴠɪᴅɪᴏ ʏᴀɴɢ 1x ʟɪʜᴀᴛ.</b></blockquote>
"""

import asyncio
import os

from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto

from GooUbot import *

@PY.UBOT("colong")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    dia = message.reply_to_message
    if not dia:
        return await message.reply(f"{ggl}mohon balas ke media")
    anjing = dia.caption or ""
    Tm = await message.reply(f"{prs}processing...")
    if dia.photo:
        if message.reply_to_message.photo.file_size > 10000000:
            return await Tm.edit(f"{ktrng}file di atas 10mb tidak di izinkan")
        anu = await client.download_media(dia)
        await client.send_photo(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    if dia.video:
        if message.reply_to_message.video.file_size > 10000000:
            return await Tm.edit(f"{ktrng}file di atas 10mb tidak di izinkan")
        anu = await client.download_media(dia)
        await client.send_video(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    if dia.audio:
        if message.reply_to_message.audio.file_size > 10000000:
            return await Tm.edit(f"{ktrng}file di atas 10mb tidak di izinkan")
        anu = await client.download_media(dia)
        await client.send_audio(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    if dia.voice:
        if message.reply_to_message.voice.file_size > 10000000:
            return await Tm.edit(f"{ktrng}file di atas 10mb tidak di izinkan")
        anu = await client.download_media(dia)
        await client.send_voice(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    if dia.document:
        if message.reply_to_message.document.file_size > 10000000:
            return await Tm.edit(f"{ktrng}file di atas 10mb tidak di izinkan")
        anu = await client.download_media(dia)
        await client.send_document(client.me.id, anu, anjing)
        os.remove(anu)
        await message.delete()
        return await Tm.delete()
    else:
        return await Tm.reply(f"{ggl}sepertinya terjadi kesalahan")

