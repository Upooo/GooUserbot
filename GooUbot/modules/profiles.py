__MODULE__ = "profiles"
__HELP__ = """
<blockquote><b>Profiles</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}sg</code> [user] — history nama/username
<code>{0}info</code> [user] — info user
<code>{0}cinfo</code> [chat] — info grup/channel
<code>{0}id</code> — info id pesan/chat/user
<code>{0}setbio</code> [teks] — ganti bio
<code>{0}setname</code> [teks] — ganti nama
<code>{0}block</code> / <code>{0}unblock</code> [user]</blockquote>
"""

import asyncio
import random

from pyrogram.enums import ChatType
from pyrogram.raw.functions.messages import DeleteHistory

from GooUbot import *


@PY.UBOT("sg")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    get_user = await extract_user(message)
    status = await message.reply(f"{prs}Processing...")

    if not get_user:
        return await status.edit(f"{ggl}User tidak ditemukan.")

    try:
        user_id = (await client.get_users(get_user)).id
    except Exception:
        try:
            user_id = int(message.command[1])
        except Exception as e:
            return await status.edit(f"{ggl}<code>{e}</code>")

    bots = ["Sangmata_bot", "SangMata_beta_bot"]
    target_bot = random.choice(bots)

    try:
        await client.unblock_user(target_bot)
        sent = await client.send_message(target_bot, str(user_id))
        await asyncio.sleep(4)
        try:
            await sent.delete()
        except Exception:
            pass
        await status.delete()

        async for msg in client.search_messages(target_bot, limit=2):
            if msg.text:
                await message.reply(msg.text, quote=True)
            else:
                await message.reply(f"{ggl}@{target_bot} tidak merespon.", quote=True)

        peer = await client.resolve_peer(target_bot)
        await client.invoke(DeleteHistory(peer=peer, max_id=0, revoke=True))
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("info")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    user_id = await extract_user(message)
    status = await message.reply(f"{prs}Processing...")

    if not user_id:
        return await status.edit(f"{ggl}<code>{message.command[0]}</code> [user/reply]")

    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first = user.first_name or "-"
        last = user.last_name or "-"
        fullname = f"{user.first_name} {user.last_name}".strip() if user.last_name else user.first_name

        try:
            bio = (await client.get_chat(user.id)).bio or "-"
        except Exception:
            bio = "-"

        status_name = str(user.status).replace("UserStatus.", "").capitalize() if user.status else "-"
        dc = user.dc_id or "-"

        try:
            common = len(await client.get_common_chats(user.id))
        except Exception:
            common = "-"

        text = f"""
<blockquote><b>User Info</b>
ID: <code>{user.id}</code>
Nama: {first} {last}
Username: {username}
DC: <code>{dc}</code>
Bot: {user.is_bot}
Premium: {user.is_premium}
Verified: {user.is_verified}
Scam: {user.is_scam}
Restricted: {user.is_restricted}
Bio: {bio}
Common groups: {common}
Last seen: {status_name}
Link: <a href="tg://user?id={user.id}">{fullname}</a></blockquote>
""".strip()
        await status.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("cinfo")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...")
    try:
        if len(message.command) > 1:
            chat = await client.get_chat(message.command[1])
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await status.edit(
                    f"{ggl}Pakai di grup atau <code>.cinfo [username/id]</code>"
                )
            chat = await client.get_chat(message.chat.id)

        ctype = str(chat.type).replace("ChatType.", "").capitalize()
        username = f"@{chat.username}" if chat.username else "-"
        desc = chat.description or "-"
        dc = chat.dc_id or "-"

        text = f"""
<blockquote><b>Chat Info</b>
ID: <code>{chat.id}</code>
Title: {chat.title}
Username: {username}
Type: {ctype}
DC: <code>{dc}</code>
Members: {chat.members_count or "-"}
Scam: {chat.is_scam}
Fake: {chat.is_fake}
Verified: {chat.is_verified}
Restricted: {chat.is_restricted}
Protected: {chat.has_protected_content}
Desc: {desc}</blockquote>
""".strip()
        await status.edit(text, disable_web_page_preview=True)
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("id")
@PY.TOP_CMD
async def _(client, message):
    lines = [f"Message ID: <code>{message.id}</code>"]

    if message.chat.type == ChatType.CHANNEL:
        lines.append(f"Chat ID: <code>{message.sender_chat.id}</code>")
    else:
        if message.from_user:
            lines.append(f"Your ID: <code>{message.from_user.id}</code>")
        lines.append(f"Chat ID: <code>{message.chat.id}</code>")

        if len(message.command) > 1:
            try:
                user = await client.get_chat(message.command[1])
                lines.append(f"Target ID: <code>{user.id}</code>")
            except Exception:
                return await message.reply("User tidak ditemukan.")

    if message.reply_to_message:
        rep = message.reply_to_message
        rid = rep.from_user.id if rep.from_user else rep.sender_chat.id
        lines.append(f"Replied msg: <code>{rep.id}</code>")
        lines.append(f"Replied user: <code>{rid}</code>")
        try:
            file_info = get_file_id(rep)
            if file_info:
                lines.append(f"Media ID: <code>{file_info.file_id}</code>")
        except Exception:
            pass

    await message.reply("<blockquote>" + "\n".join(lines) + "</blockquote>")


@PY.UBOT("setbio")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...")
    if len(message.command) < 2:
        return await status.edit(f"{ggl}<code>{message.command[0]} [teks]</code>")

    bio = message.text.split(None, 1)[1]
    try:
        await client.update_profile(bio=bio)
        await status.edit(f"{brhsl}Bio diubah.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("setname")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...")
    if len(message.command) < 2:
        return await status.edit(f"{ggl}<code>{message.command[0]} [teks]</code>")

    name = message.text.split(None, 1)[1]
    try:
        await client.update_profile(first_name=name)
        await status.edit(f"{brhsl}Nama diubah ke <b>{name}</b>")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("block")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    user_id = await extract_user(message)
    status = await message.reply(f"{prs}Processing...")

    if not user_id:
        return await status.edit(f"{ggl}<code>{message.command[0]}</code> [user/reply]")
    if user_id == client.me.id:
        return await status.edit(f"{ggl}Tidak bisa block diri sendiri.")

    try:
        await client.block_user(user_id)
        user = await client.get_users(user_id)
        await status.edit(f"{brhsl}Blocked {user.mention}")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("unblock")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    user_id = await extract_user(message)
    status = await message.reply(f"{prs}Processing...")

    if not user_id:
        return await status.edit(f"{ggl}<code>{message.command[0]}</code> [user/reply]")

    try:
        await client.unblock_user(user_id)
        user = await client.get_users(user_id)
        await status.edit(f"{brhsl}Unblocked {user.mention}")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("idm")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    if not message.reply_to_message or not message.reply_to_message.entities:
        return await message.reply(f"{ggl}Reply ke custom emoji.")

    for ent in message.reply_to_message.entities:
        if getattr(ent, "custom_emoji_id", None):
            return await message.reply(f"<code>{ent.custom_emoji_id}</code>")

    await message.reply(f"{ggl}Tidak ada custom emoji.")
