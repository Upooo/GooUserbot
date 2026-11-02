__MODULE__ = "profile"
__HELP__ = """
<blockquote><b>Profile Photo</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}getpp</code> [user/reply]
Ambil foto profil.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}setpp</code> (reply foto)
Ganti foto profil akun.</blockquote>
"""

import os

from pyrogram.errors import PeerIdInvalid, UsernameNotOccupied, UserNotParticipant

from GooUbot import *


@PY.UBOT("getpp|getprofile")
@PY.TOP_CMD
async def get_profile_pic(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if message.reply_to_message and message.reply_to_message.from_user:
        target = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        target = message.command[1]
    else:
        target = message.chat.id

    try:
        async for photo in client.get_chat_photos(target, limit=1):
            await client.send_photo(
                message.chat.id,
                photo=photo.file_id,
                caption=f"{brhsl}Profile photo",
            )
            return
        await message.reply(f"{ggl}Tidak ada foto profil.")
    except (UsernameNotOccupied, UserNotParticipant, PeerIdInvalid):
        await message.reply(f"{ggl}Akun/grup tidak ditemukan.")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")


@PY.UBOT("setpp")
@PY.TOP_CMD
async def set_profile_photo(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if not message.reply_to_message:
        return await message.reply(f"{ggl}Reply ke foto/media.")

    media = message.reply_to_message
    path = None
    try:
        if media.photo:
            path = await media.download()
        elif media.document and media.document.mime_type and "image" in media.document.mime_type:
            path = await media.download()
        else:
            return await message.reply(f"{ggl}Media harus foto/gambar.")

        await client.set_profile_photo(photo=path)
        await message.reply(f"{brhsl}Foto profil diganti.")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
    finally:
        if path and os.path.exists(path):
            os.remove(path)
