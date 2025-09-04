import asyncio
from pyrogram import Client
from pyrogram.types import Message
import os
from GooUbot import *

__MODULE__ = "download"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴅᴏᴡɴʟᴏᴀᴅ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}dl [link]</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴅᴏᴡɴʟᴏᴀᴅ ᴠɪᴅᴇᴏ ꜱᴏꜱᴍᴇᴅ ᴠɪᴀ ʟɪɴᴋ.</b></blockquote>"""

@PY.UBOT("dl")
@PY.TOP_CMD
async def download_video(client: Client, message: Message):
    if not (args := message.text.split(maxsplit=1)[1:]):
        return await message.reply("❌ Kirimkan link video!\n\nContoh: <code>.dl https://tiktok.com/xxx</code>")
    
    url = args[0]
    await message.reply("🔄 Mendownload...")

    filename = "video.mp4"
    try:
        # Unduh via yt-dlp
        process = await asyncio.create_subprocess_exec(
            "yt-dlp", "-o", filename, url,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE
        )
        stdout, stderr = await process.communicate()

        if not os.path.exists(filename):
            return await message.reply("❌ Gagal mengunduh video.")

        # Kirim ke Telegram
        await client.send_video(
            chat_id=message.chat.id,
            video=filename,
            caption="✅ Video berhasil diunduh!",
            reply_to_message_id=message.id
        )
        os.remove(filename)
    except Exception as e:
        await message.reply(f"❌ Error: {e}")
