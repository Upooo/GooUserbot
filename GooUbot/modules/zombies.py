__MODULE__ = "zombies"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴢᴏᴍʙɪᴇꜱ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}zombies</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴇʟᴜᴀʀᴋᴀɴ ᴀᴋᴜɴ ᴛᴇʀʜᴀᴘᴜꜱ ᴅᴀʀɪ ɢʀᴏᴜᴘ.</b></blockquote>
"""

from pyrogram import *
from pyrogram.enums import *
from pyrogram.errors import *
from pyrogram.types import *

from GooUbot import *

@PY.UBOT("zombies")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    chat_id = message.chat.id
    deleted_users = []
    banned_users = 0
    Tm = await message.reply("sedang memeriksa")
    async for i in client.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                banned_users += 1
                await message.chat.ban_member(deleted_user)
            except Exception:
                pass
        if client.me.is_premium:
            await Tm.edit(f"<blockquote><b>{brhsl}berhasil mengeluarkan {banned_users} akun terhapus</b></blockquote>")
        else:
            await Tm.edit(f"<blockquote><b>berhasil mengeluarkan {banned_users} akun terhapus</b></blockquote>")
    else:
        if client.me.is_premium:
            await Tm.edit(f"{ggl}tidak ada akun terhapus di group ini")
        else:
            await Tm.edit(f"tidak ada akun terhapus di group ini")
