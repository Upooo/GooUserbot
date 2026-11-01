__MODULE__ = "admin"
__HELP__ = """
<blockquote><b>Admin</b></blockquote>

<blockquote><b>Perintah moderasi:</b>
<code>{0}kick</code> / <code>{0}ban</code> / <code>{0}mute</code>
<code>{0}unban</code> / <code>{0}unmute</code>
<code>{0}etmin</code> / <code>{0}ceo</code> / <code>{0}demote</code></blockquote>

<blockquote><b>Perintah lock:</b>
<code>{0}lock</code> / <code>{0}unlock</code> / <code>{0}locks</code>
Type: msg, media, stickers, polls, info, invite, pin, all</blockquote>

<blockquote><b>Lainnya:</b>
<code>{0}getlink</code> — ambil invite link grup</blockquote>
"""

import asyncio

from pyrogram.errors import ChatAdminRequired, ChatNotModified
from pyrogram.types import ChatPermissions, ChatPrivileges

from GooUbot import *
from GooUbot.config import OWNER_ID

data = {
    "msg": "can_send_messages",
    "stickers": "can_send_other_messages",
    "gifs": "can_send_other_messages",
    "media": "can_send_media_messages",
    "games": "can_send_other_messages",
    "inline": "can_send_other_messages",
    "url": "can_add_web_page_previews",
    "polls": "can_send_polls",
    "info": "can_change_info",
    "invite": "can_invite_users",
    "pin": "can_pin_messages",
}


async def current_chat_permissions(client, chat_id):
    perms = []
    perm = (await client.get_chat(chat_id)).permissions
    if not perm:
        return perms
    mapping = [
        ("can_send_messages", perm.can_send_messages),
        ("can_send_media_messages", perm.can_send_media_messages),
        ("can_send_other_messages", perm.can_send_other_messages),
        ("can_add_web_page_previews", perm.can_add_web_page_previews),
        ("can_send_polls", perm.can_send_polls),
        ("can_change_info", perm.can_change_info),
        ("can_invite_users", perm.can_invite_users),
        ("can_pin_messages", perm.can_pin_messages),
    ]
    for name, value in mapping:
        if value:
            perms.append(name)
    return perms


async def tg_lock(client, message, parameter, permissions, perm, lock):
    if lock:
        if perm not in permissions:
            return await message.reply(f"<blockquote><b>{parameter}</b> sudah terkunci.</blockquote>")
        permissions.remove(perm)
    else:
        if perm in permissions:
            return await message.reply(f"<blockquote><b>{parameter}</b> sudah terbuka.</blockquote>")
        permissions.append(perm)

    perms_dict = {p: True for p in set(permissions)}
    try:
        await client.set_chat_permissions(message.chat.id, ChatPermissions(**perms_dict))
    except ChatNotModified:
        return await message.reply(f"<code>{message.command[0]} [type]</code>")
    except ChatAdminRequired:
        return await message.reply("Tidak punya izin admin.")

    status = "terkunci" if lock else "terbuka"
    await message.reply(
        f"<blockquote><b>{parameter}</b> {status} untuk non-admin.\n"
        f"Grup: {message.chat.title}</blockquote>"
    )


@PY.UBOT("lock|unlock")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    if len(message.command) != 2:
        return await message.reply(f"<code>{message.command[0]} [type]</code>")

    chat_id = message.chat.id
    parameter = message.command[1].lower()
    state = message.command[0].lower()

    if parameter not in data and parameter != "all":
        return await message.reply("Type tidak valid. Cek <code>.help admin</code>")

    permissions = await current_chat_permissions(client, chat_id)

    if parameter in data:
        return await tg_lock(
            client, message, parameter, permissions, data[parameter], state == "lock"
        )

    if parameter == "all" and state == "lock":
        try:
            await client.set_chat_permissions(chat_id, ChatPermissions())
            await message.reply(
                f"<blockquote>Semua permission terkunci.\nGrup: {message.chat.title}</blockquote>"
            )
        except ChatAdminRequired:
            return await message.reply("Tidak punya izin admin.")
        except ChatNotModified:
            return await message.reply("Sudah terkunci semua.")

    elif parameter == "all" and state == "unlock":
        try:
            await client.set_chat_permissions(
                chat_id,
                ChatPermissions(
                    can_send_messages=True,
                    can_send_media_messages=True,
                    can_send_other_messages=True,
                    can_add_web_page_previews=True,
                    can_send_polls=True,
                    can_change_info=False,
                    can_invite_users=True,
                    can_pin_messages=False,
                ),
            )
            await message.reply(
                f"<blockquote>Permission dibuka untuk non-admin.\nGrup: {message.chat.title}</blockquote>"
            )
        except ChatAdminRequired:
            return await message.reply("Tidak punya izin admin.")


@PY.UBOT("locks")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    permissions = await current_chat_permissions(client, message.chat.id)
    if not permissions:
        return await message.reply("Semua permission terkunci.")
    text = "<blockquote><b>Active permissions</b></blockquote>\n" + "\n".join(
        f"• <code>{p}</code>" for p in permissions
    )
    await message.reply(text)


@PY.UBOT("kick|ban|mute|unmute|unban")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    cmd = message.command[0].lower()

    if cmd in ("kick", "ban", "mute"):
        user_id, reason = await extract_user_and_reason(message)
    else:
        user_id = await extract_user(message)
        reason = None

    if not user_id:
        return await message.reply(f"{ggl}<code>{cmd}</code> [user / reply]")

    if user_id == OWNER_ID:
        return await message.reply(f"{ggl}Tidak bisa target owner.")

    try:
        admins = await list_admins(message)
        if user_id in admins:
            return await message.reply(f"{ggl}Tidak bisa target admin.")
    except Exception:
        pass

    try:
        user = await client.get_users(user_id)
        mention = user.mention
    except Exception as e:
        return await message.reply(f"{ggl}<code>{e}</code>")

    reason = reason or "-"

    try:
        if cmd == "kick":
            await message.chat.ban_member(user_id)
            await asyncio.sleep(0.5)
            await message.chat.unban_member(user_id)
            await message.reply(
                f"<blockquote>{brhsl}<b>Kicked</b> {mention}\nAlasan: {reason}</blockquote>"
            )
        elif cmd == "ban":
            await message.chat.ban_member(user_id)
            await message.reply(
                f"<blockquote>{brhsl}<b>Banned</b> {mention}\nAlasan: {reason}</blockquote>"
            )
        elif cmd == "mute":
            await message.chat.restrict_member(user_id, ChatPermissions())
            await message.reply(
                f"<blockquote>{brhsl}<b>Muted</b> {mention}\nAlasan: {reason}</blockquote>"
            )
        elif cmd == "unmute":
            await message.chat.unban_member(user_id)
            await message.reply(f"{brhsl}{mention} bisa chat lagi.")
        elif cmd == "unban":
            await message.chat.unban_member(user_id)
            await message.reply(f"{brhsl}{mention} di-unban.")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")


@PY.UBOT("etmin")
@PY.TOP_CMD
@PY.GROUP
async def promotte(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    user_id = await extract_user(message)
    status = await message.reply(f"{prs}Processing...")

    if not user_id:
        return await status.edit(f"{ggl}User tidak ditemukan.")

    try:
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=False,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=False,
            ),
        )
        user = await client.get_users(user_id)
        await status.edit(
            f"{sks}Promoted {user.mention}\nGrup: {message.chat.title}"
        )
    except ChatAdminRequired:
        await status.edit(f"{ggl}Butuh izin promote.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("ceo")
@PY.TOP_CMD
@PY.GROUP
async def promotte_full(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    user_id = await extract_user(message)
    status = await message.reply(f"{prs}Processing...")

    if not user_id:
        return await status.edit(f"{ggl}User tidak ditemukan.")

    try:
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        user = await client.get_users(user_id)
        await status.edit(
            f"{sks}Full promote {user.mention}\nGrup: {message.chat.title}"
        )
    except ChatAdminRequired:
        await status.edit(f"{ggl}Butuh izin promote.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("demote")
@PY.TOP_CMD
@PY.GROUP
async def demote(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    user_id = await extract_user(message)
    status = await message.reply(f"{prs}Processing...")

    if not user_id:
        return await status.edit(f"{ggl}User tidak ditemukan.")
    if user_id == client.me.id:
        return await status.edit(f"{ggl}Tidak bisa demote diri sendiri.")

    try:
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=False,
                can_delete_messages=False,
                can_manage_video_chats=False,
                can_restrict_members=False,
                can_change_info=False,
                can_invite_users=False,
                can_pin_messages=False,
                can_promote_members=False,
            ),
        )
        user = await client.get_users(user_id)
        await status.edit(f"{sks}Demoted {user.mention}")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("getlink")
@PY.TOP_CMD
@PY.GROUP
async def get_link(client, message):
    ggl = await EMO.GAGAL(client)
    sks = await EMO.BERHASIL(client)
    try:
        link = await client.export_chat_invite_link(message.chat.id)
        await message.reply(
            f"{sks}Invite link:\n<code>{link}</code>",
            disable_web_page_preview=True,
        )
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
