__MODULE__ = "download"
__HELP__ = """
<blockquote><b>Download Sosmed</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}dl</code> [link]
Download video dari link (TikTok, IG, YT, dll) via yt-dlp.</blockquote>
"""

import asyncio
import os
import uuid

from GooUbot import *


@PY.UBOT("dl")
@PY.TOP_CMD
async def download_video(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [link]</code>"
        )

    url = message.command[1]
    status = await message.reply(f"{prs}Downloading...")
    filename = f"dl_{uuid.uuid4().hex[:8]}.mp4"

    try:
        process = await asyncio.create_subprocess_exec(
            "yt-dlp",
            "-o",
            filename,
            "--no-playlist",
            "--quiet",
            url,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        await process.communicate()

        if not os.path.exists(filename):
            return await status.edit(f"{ggl}Gagal download.")

        await client.send_video(
            chat_id=message.chat.id,
            video=filename,
            caption=f"{brhsl}Downloaded",
            reply_to_message_id=message.id,
        )
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
    finally:
        if os.path.exists(filename):
            os.remove(filename)
