__MODULE__ = "kontak"
__HELP__ = """
<blockquote><b>Kontak</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}savekon</code> [user] [nama]
Simpan kontak.
<code>{0}delkon</code> [user] — hapus kontak.</blockquote>
"""

from pyrogram.errors import RPCError
from pyrogram.raw.functions.contacts import AddContact

from GooUbot import *


@PY.UBOT("savekon")
@PY.TOP_CMD
async def save_contact(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    user_id = None
    custom_name = ""

    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
        custom_name = message.text.split(maxsplit=1)[1] if len(message.command) > 1 else ""
    else:
        if len(message.command) < 3:
            return await message.reply(
                f"{ggl}<code>{message.command[0]} [user] [nama]</code>"
            )
        try:
            user = await client.get_users(message.command[1])
            user_id = user.id
            custom_name = " ".join(message.command[2:])
        except Exception as e:
            return await message.reply(f"{ggl}<code>{e}</code>")

    if not custom_name.strip():
        return await message.reply(f"{ggl}Nama kontak wajib diisi.")

    try:
        peer = await client.resolve_peer(user_id)
        response = await client.invoke(
            AddContact(id=peer, first_name=custom_name.strip(), last_name="", phone="")
        )
        if response.users and response.users[0].contact:
            await message.reply(f"{brhsl}Kontak disimpan: <code>{custom_name}</code>")
        else:
            await message.reply(f"{ggl}Gagal simpan kontak.")
    except RPCError as e:
        await message.reply(f"{ggl}<code>{e}</code>")


@PY.UBOT("delkon")
@PY.TOP_CMD
async def delete_contact(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if message.reply_to_message and message.reply_to_message.from_user:
        user_id = message.reply_to_message.from_user.id
    elif len(message.command) > 1:
        try:
            user = await client.get_users(message.command[1])
            user_id = user.id
        except Exception as e:
            return await message.reply(f"{ggl}<code>{e}</code>")
    else:
        return await message.reply(f"{ggl}<code>{message.command[0]} [user/reply]</code>")

    try:
        await client.delete_contacts([user_id])
        await message.reply(f"{brhsl}Kontak dihapus.")
    except RPCError as e:
        await message.reply(f"{ggl}<code>{e}</code>")
