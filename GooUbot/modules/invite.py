__MODULE__ = "invite"
__HELP__ = """
<blockquote><b>Invite</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}invite</code> [user...]
Undang member ke grup ini.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}inviteall</code> [chat] [delay detik]
Undang member aktif dari grup lain (pakai delay biar aman).</blockquote>

<blockquote><b>Perintah:</b> <code>{0}cancel</code>
Stop proses inviteall.</blockquote>
"""

import asyncio

from pyrogram.enums import UserStatus

from GooUbot import *

invite_id = []


@PY.UBOT("invite")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [user...]</code>")

    status = await message.reply(f"{prs}Menambahkan...")
    users = message.text.split(None, 1)[1].split()

    try:
        await client.add_chat_members(message.chat.id, users, forward_limit=50)
        await status.edit(f"{brhsl}Berhasil tambah {len(users)} user.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("inviteall")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 3:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [chat_id/username] [delay]</code>"
        )

    status = await message.reply(f"{prs}Processing...")

    try:
        chat = await client.get_chat(message.command[1])
        delay = max(int(message.command[2]), 3)
    except Exception as e:
        return await status.edit(f"{ggl}<code>{e}</code>")

    if message.chat.id in invite_id:
        return await status.edit(
            f"{ggl}Inviteall sedang jalan. Pakai <code>.cancel</code>"
        )

    invite_id.append(message.chat.id)
    done, failed = 0, 0
    await status.edit(f"{prs}Invite dari <b>{chat.title}</b> (delay {delay}s)...")

    try:
        async for member in client.get_chat_members(chat.id):
            if message.chat.id not in invite_id:
                break
            if not member.user or member.user.is_bot or member.user.is_deleted:
                continue
            if member.user.status not in (
                UserStatus.ONLINE,
                UserStatus.OFFLINE,
                UserStatus.RECENTLY,
                UserStatus.LAST_WEEK,
            ):
                continue
            try:
                await client.add_chat_members(message.chat.id, member.user.id)
                done += 1
            except Exception:
                failed += 1
            await asyncio.sleep(delay)
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
    finally:
        if message.chat.id in invite_id:
            invite_id.remove(message.chat.id)

    await status.edit(
        f"{brhsl}Selesai\nBerhasil: <code>{done}</code>\nGagal: <code>{failed}</code>"
    )


@PY.UBOT("cancel")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if message.chat.id not in invite_id:
        return await message.reply(f"{ggl}Tidak ada inviteall yang berjalan.")

    try:
        invite_id.remove(message.chat.id)
        await message.reply(f"{brhsl}Inviteall dibatalkan.")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
