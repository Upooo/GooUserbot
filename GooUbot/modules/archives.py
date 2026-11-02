__MODULE__ = "archive"
__HELP__ = """
<blockquote><b>Archive</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}arch</code> [all/pc/gc]
Arsipkan chat sesuai type.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}unarch</code> [all/pc/gc]
Batalkan arsip.</blockquote>
"""

from GooUbot import *
from GooUbot.core.helpers.tools import get_data_id


@PY.UBOT("arch")
@PY.TOP_CMD
async def archive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [all/pc/gc]</code>"
        )

    status = await message.reply(f"{prs}Processing...")
    tipe = message.command[1].lower()

    try:
        chats = await get_data_id(client, tipe)
        for chat_id in chats:
            try:
                await client.archive_chats(chat_id)
            except Exception:
                pass
        await status.edit(f"{brhsl}Archived <code>{tipe}</code> ({len(chats)} chat).")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("unarch")
@PY.TOP_CMD
async def unarchive_user(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [all/pc/gc]</code>"
        )

    status = await message.reply(f"{prs}Processing...")
    tipe = message.command[1].lower()

    try:
        chats = await get_data_id(client, tipe)
        for chat_id in chats:
            try:
                await client.unarchive_chats(chat_id)
            except Exception:
                pass
        await status.edit(f"{brhsl}Unarchived <code>{tipe}</code> ({len(chats)} chat).")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
