__MODULE__ = "copy"
__HELP__ = """
<blockquote><b>Copy</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}copy</code> [link post]
Salin pesan/post dari channel via link.</blockquote>
"""

import os

from pyrogram.errors import RPCError

from GooUbot import *


@PY.UBOT("copy")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    link = get_arg(message)
    if not link:
        return await message.reply(f"{ggl}<code>{message.command[0]} [link]</code>")

    status = await message.reply(f"{prs}Processing...")

    try:
        parts = link.rstrip("/").split("/")
        msg_id = int(parts[-1])

        if "t.me/c/" in link:
            chat = int("-100" + str(parts[-2]))
        else:
            chat = parts[-2]

        src = await client.get_messages(chat, msg_id)
        if not src:
            return await status.edit(f"{ggl}Pesan tidak ditemukan.")

        caption = src.caption or None

        if src.text and not src.media:
            await src.copy(message.chat.id)
        elif src.photo:
            path = await client.download_media(src)
            await client.send_photo(message.chat.id, path, caption=caption)
            os.remove(path)
        elif src.video:
            path = await client.download_media(src)
            await client.send_video(message.chat.id, path, caption=caption)
            os.remove(path)
        elif src.audio:
            path = await client.download_media(src)
            await client.send_audio(message.chat.id, path, caption=caption)
            os.remove(path)
        elif src.voice:
            path = await client.download_media(src)
            await client.send_voice(message.chat.id, path, caption=caption)
            os.remove(path)
        elif src.document:
            path = await client.download_media(src)
            await client.send_document(message.chat.id, path, caption=caption)
            os.remove(path)
        else:
            await src.copy(message.chat.id)

        await status.delete()
        try:
            await message.delete()
        except Exception:
            pass
    except (RPCError, Exception) as e:
        await status.edit(f"{ggl}<code>{e}</code>")
