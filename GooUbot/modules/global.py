__MODULE__ = "global"
__HELP__ = """
<blockquote><b>Global Moderation</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}gban</code> / <code>{0}ungban</code> [user]
<code>{0}gmute</code> / <code>{0}ungmute</code> [user]

Berlaku di chat di mana kamu admin.</blockquote>
"""

import asyncio

from pyrogram.types import ChatPermissions

from GooUbot import *
from GooUbot.config import OWNER_ID


async def _global_action(client, message, action, mode_label):
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    user_id = await extract_user(message)
    status = await message.reply(f"{prs}Processing...")

    if not user_id:
        return await status.edit(f"{ggl}User tidak ditemukan.")

    try:
        user = await client.get_users(user_id)
    except Exception as e:
        return await status.edit(f"{ggl}<code>{e}</code>")

    if user.id == OWNER_ID:
        return await status.edit(f"{ggl}Tidak bisa target owner.")
    if user.id == client.me.id:
        return await status.edit(f"{ggl}Tidak bisa target diri sendiri.")

    done = failed = 0
    chats = await get_data_id(client, "global" if action in ("ban", "unban") else "group")

    for chat_id in chats:
        try:
            if action == "ban":
                await client.ban_chat_member(chat_id, user.id)
            elif action == "unban":
                await client.unban_chat_member(chat_id, user.id)
            elif action == "mute":
                await client.restrict_chat_member(
                    chat_id, user.id, ChatPermissions(can_send_messages=False)
                )
            elif action == "unmute":
                await client.restrict_chat_member(
                    chat_id, user.id, ChatPermissions(can_send_messages=True)
                )
            done += 1
        except Exception:
            failed += 1
        await asyncio.sleep(0.15)

    await status.edit(
        f"{brhsl}<b>Global {mode_label}</b>\n"
        f"Berhasil: <code>{done}</code>\n"
        f"Gagal: <code>{failed}</code>\n"
        f"User: {user.mention}"
    )


@PY.UBOT("gban")
@PY.IDOL("cgban")
@PY.TOP_CMD
async def _(client, message):
    await _global_action(client, message, "ban", "Ban")


@PY.UBOT("ungban")
@PY.IDOL("cungban")
@PY.TOP_CMD
async def _(client, message):
    await _global_action(client, message, "unban", "Unban")


@PY.UBOT("gmute")
@PY.IDOL("cgmute")
@PY.TOP_CMD
async def _(client, message):
    await _global_action(client, message, "mute", "Mute")


@PY.UBOT("ungmute")
@PY.IDOL("cungmute")
@PY.TOP_CMD
async def _(client, message):
    await _global_action(client, message, "unmute", "Unmute")
