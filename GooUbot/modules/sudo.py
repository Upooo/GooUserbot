__MODULE__ = "sudo"
__HELP__ = """
<blockquote><b>Sudo</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}addsudo</code> [user]
Tambah user ke sudo list.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}delsudo</code> [user]
Hapus user dari sudo list.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}sudolist</code>
Lihat daftar sudo aktif.</blockquote>
"""

from GooUbot import *


@PY.UBOT("addsudo")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    msg = await message.reply(f"{prs}Processing...")
    user_id = await extract_user(message)

    if not user_id:
        return await msg.edit(
            f"{ggl}<code>{message.command[0]}</code> [@user / id / reply]"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as e:
        return await msg.edit(f"{ggl}<code>{e}</code>")

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USER", "ID_NYA") or []

    if user.id in sudo_users:
        return await msg.edit(f"{ggl}{user.mention} sudah ada di sudo.")

    try:
        await add_to_vars(client.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(f"{brhsl}{user.mention} ditambahkan ke sudo.")
    except Exception as e:
        return await msg.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("delsudo")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    msg = await message.reply(f"{prs}Processing...")
    user_id = await extract_user(message)

    if not user_id:
        return await msg.edit(
            f"{ggl}<code>{message.command[0]}</code> [@user / id / reply]"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as e:
        return await msg.edit(f"{ggl}<code>{e}</code>")

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USER", "ID_NYA") or []

    if user.id not in sudo_users:
        return await msg.edit(f"{ggl}{user.mention} bukan sudo.")

    try:
        await remove_from_vars(client.me.id, "SUDO_USER", user.id, "ID_NYA")
        return await msg.edit(f"{brhsl}{user.mention} dihapus dari sudo.")
    except Exception as e:
        return await msg.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("sudolist")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)

    msg = await message.reply(f"{prs}Processing...")
    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USER", "ID_NYA") or []

    if not sudo_users:
        return await msg.edit(f"{ggl}Sudo list kosong.")

    lines = []
    for uid in sudo_users:
        try:
            user = await client.get_users(int(uid))
            lines.append(f"• {user.mention} — <code>{user.id}</code>")
        except Exception:
            lines.append(f"• <code>{uid}</code>")

    text = "<blockquote><b>Sudo List</b></blockquote>\n" + "\n".join(lines)
    return await msg.edit(text)
