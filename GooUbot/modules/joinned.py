__MODULE__ = "joinleave"
__HELP__ = """
<blockquote><b>Join / Leave</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}join</code> [link/username] — join chat
<code>{0}kickme</code> — leave chat ini
<code>{0}leaveallgc</code> — leave semua grup (kecuali admin/owner)
<code>{0}leaveallch</code> — leave semua channel (kecuali admin/owner)
<code>{0}leavemute</code> — leave grup yang restrict akun kamu</blockquote>
"""

from pyrogram.enums import ChatMemberStatus, ChatType

from GooUbot import *
from GooUbot.config import BLACKLIST_CHAT


@PY.UBOT("kickme")
@PY.IDOL("ckickme")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    target = message.command[1] if len(message.command) > 1 else message.chat.id
    status = await message.reply(f"{prs}Leaving...")

    if message.chat.id in (BLACKLIST_CHAT or []):
        return await status.edit(f"{ggl}Dilarang di chat ini.")

    try:
        await status.edit(f"{brhsl}Leaving chat...")
        await client.leave_chat(target)
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("join")
@PY.IDOL("cjoin")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [link/username]</code>")

    target = message.command[1]
    status = await message.reply(f"{prs}Joining...")

    try:
        await client.join_chat(target)
        await status.edit(f"{brhsl}Joined: <code>{target}</code>")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Leaving all groups...")
    done = failed = 0

    async for dialog in client.get_dialogs():
        if dialog.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
            continue
        try:
            member = await client.get_chat_member(dialog.chat.id, "me")
            if member.status not in (
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER,
            ):
                await client.leave_chat(dialog.chat.id)
                done += 1
        except Exception:
            failed += 1

    await status.edit(
        f"{brhsl}Leave grup: <code>{done}</code>\n{ggl}Gagal: <code>{failed}</code>"
    )


@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Leaving all channels...")
    done = failed = 0

    async for dialog in client.get_dialogs():
        if dialog.chat.type != ChatType.CHANNEL:
            continue
        try:
            member = await client.get_chat_member(dialog.chat.id, "me")
            if member.status not in (
                ChatMemberStatus.ADMINISTRATOR,
                ChatMemberStatus.OWNER,
            ):
                await client.leave_chat(dialog.chat.id)
                done += 1
        except Exception:
            failed += 1

    await status.edit(
        f"{brhsl}Leave channel: <code>{done}</code>\n{ggl}Gagal: <code>{failed}</code>"
    )


@PY.UBOT("lvmute|leavemute")
@PY.IDOL("cleavemute")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    status = await message.reply(f"{prs}Checking muted groups...")
    done = 0

    async for dialog in client.get_dialogs():
        if dialog.chat.type not in (ChatType.SUPERGROUP, ChatType.GROUP):
            continue
        try:
            member = await client.get_chat_member(dialog.chat.id, "me")
            if member.status == ChatMemberStatus.RESTRICTED:
                await client.leave_chat(dialog.chat.id)
                done += 1
        except Exception:
            pass

    await status.edit(f"{brhsl}Leave dari <code>{done}</code> grup yang restrict.")
