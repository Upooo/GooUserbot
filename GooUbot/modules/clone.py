__MODULE__ = "clone"
__HELP__ = """
<blockquote><b>Clone Profile</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}clone</code> [user/reply]
Salin profil user (nama, bio, foto).</blockquote>

<blockquote><b>Perintah:</b> <code>{0}clone restore</code>
Kembalikan profil asli.</blockquote>
"""

from GooUbot import *

STORAGE = {}


@PY.UBOT("clone")
@PY.TOP_CMD
async def impostor(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    user_id = message.from_user.id
    args = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else ""

    status = await message.reply(f"{prs}Processing...")

    if args.strip().lower() == "restore":
        if user_id not in STORAGE:
            return await status.edit(f"{ggl}Belum pernah clone. Tidak ada data restore.")
        await update_profile(client, STORAGE[user_id], restore=True)
        del STORAGE[user_id]
        return await status.edit(f"{brhsl}Profil asli dikembalikan.")

    user_obj = None
    if args:
        try:
            user = await client.get_users(args)
            user_obj = await client.get_chat(user.id)
        except Exception:
            return await status.edit(f"{ggl}User tidak valid.")
    elif message.reply_to_message and message.reply_to_message.from_user:
        user_obj = await client.get_chat(message.reply_to_message.from_user.id)
    else:
        return await status.edit(
            f"{ggl}<code>{message.command[0]} [user/reply]</code>"
        )

    if user_id not in STORAGE:
        my_profile = await client.get_chat("me")
        my_photos = [p async for p in client.get_chat_photos("me")]
        STORAGE[user_id] = {"profile": my_profile, "photos": my_photos}

    await update_profile(client, user_obj)
    await status.edit(f"{brhsl}Profil di-clone.")


async def update_profile(client, user_obj, restore=False):
    if restore:
        profile = user_obj["profile"]
        photos = user_obj["photos"]
        await client.update_profile(
            first_name=profile.first_name or "User",
            last_name=profile.last_name or "",
            bio=profile.bio or "",
        )
        if photos:
            try:
                pfp = await client.download_media(photos[0].file_id)
                await client.set_profile_photo(photo=pfp)
            except Exception:
                pass
        return

    first_name = user_obj.first_name or "User"
    last_name = user_obj.last_name or ""

    try:
        user_info = await client.get_users(user_obj.id)
        is_premium = getattr(user_info, "is_premium", False)
    except Exception:
        is_premium = False

    bio = user_obj.bio or ""
    if not is_premium and len(bio) > 70:
        bio = bio[:70]

    try:
        photos = [p async for p in client.get_chat_photos(user_obj.id)]
        if photos:
            pfp = await client.download_media(photos[0].file_id)
            await client.set_profile_photo(photo=pfp)
    except Exception:
        pass

    await client.update_profile(first_name=first_name, last_name=last_name, bio=bio)
