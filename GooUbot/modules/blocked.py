__MODULE__ = "blocked"
__HELP__ = """
<blockquote><b>Blocked</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}getblock</code>
Cek jumlah user yang diblokir.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}unblockall</code>
Unblock semua user di daftar blocked.</blockquote>
"""

from pyrogram.raw.functions.contacts import GetBlocked

from GooUbot import *


@PY.UBOT("getblock")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    status = await message.reply(f"{prs}Processing...")
    try:
        result = await client.invoke(GetBlocked(offset=0, limit=100))
        total = len(result.blocked)
        if total:
            await status.edit(f"{brhsl}Diblokir: <code>{total}</code> user")
        else:
            await status.edit(f"{ggl}Tidak ada yang diblokir.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("unblockall")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Unblocking...")
    try:
        result = await client.invoke(GetBlocked(offset=0, limit=100))
        user_ids = [entry.peer_id.user_id for entry in result.blocked]
        done = 0
        for uid in user_ids:
            try:
                await client.unblock_user(uid)
                done += 1
            except Exception:
                pass
        await status.edit(f"{brhsl}Unblock <code>{done}</code> user.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
