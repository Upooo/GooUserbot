__MODULE__ = "colong"
__HELP__ = """
<blockquote><b>Colong / Save Media</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}colong</code> (reply media)
Simpan media (termasuk view-once) ke Saved Messages. Max 10MB.</blockquote>
"""

import os

from GooUbot import *

MAX_SIZE = 10_000_000


@PY.UBOT("colong")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    dia = message.reply_to_message
    if not dia:
        return await message.reply(f"{ggl}Reply ke media.")

    status = await message.reply(f"{prs}Processing...")
    caption = dia.caption or ""
    path = None

    try:
        media = (
            dia.photo
            or dia.video
            or dia.audio
            or dia.voice
            or dia.document
        )
        if not media:
            return await status.edit(f"{ggl}Media tidak didukung.")

        size = getattr(media, "file_size", 0) or 0
        if size > MAX_SIZE:
            return await status.edit(f"{ggl}File di atas 10MB tidak diizinkan.")

        path = await client.download_media(dia)

        if dia.photo:
            await client.send_photo(client.me.id, path, caption=caption)
        elif dia.video:
            await client.send_video(client.me.id, path, caption=caption)
        elif dia.audio:
            await client.send_audio(client.me.id, path, caption=caption)
        elif dia.voice:
            await client.send_voice(client.me.id, path, caption=caption)
        elif dia.document:
            await client.send_document(client.me.id, path, caption=caption)

        await status.edit(f"{brhsl}Tersimpan di Saved Messages.")
        try:
            await message.delete()
        except Exception:
            pass
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
    finally:
        if path and os.path.exists(path):
            os.remove(path)
