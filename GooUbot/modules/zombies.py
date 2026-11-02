__MODULE__ = "zombies"
__HELP__ = """
<blockquote><b>Zombies</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}zombies</code>
Kick akun terhapus (deleted account) dari grup.</blockquote>
"""

from GooUbot import *


@PY.UBOT("zombies")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    status = await message.reply(f"{prs}Memeriksa anggota...")
    deleted_users = []

    async for member in client.get_chat_members(message.chat.id):
        if member.user and member.user.is_deleted:
            deleted_users.append(member.user.id)

    if not deleted_users:
        return await status.edit(f"{ggl}Tidak ada akun terhapus.")

    banned = 0
    for uid in deleted_users:
        try:
            await message.chat.ban_member(uid)
            banned += 1
        except Exception:
            pass

    await status.edit(f"{brhsl}Mengeluarkan <code>{banned}</code> akun terhapus.")
