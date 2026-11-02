__MODULE__ = "bl"
__HELP__ = """
<blockquote><b>Blacklist Broadcast</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}addbl</code> — tambah chat ini ke blacklist BC
<code>{0}unbl</code> — hapus dari blacklist
<code>{0}listbl</code> — lihat daftar
<code>{0}rallbl</code> — hapus semua blacklist</blockquote>
"""

from GooUbot import *


@PY.UBOT("addbl")
@PY.IDOL("caddbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...")
    try:
        chat_id = message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID") or []

        if chat_id in blacklist:
            return await status.edit(
                f"{ggl}<b>{message.chat.title}</b> sudah di blacklist."
            )

        await add_to_vars(client.me.id, "BL_ID", chat_id)
        await status.edit(f"{brhsl}<b>{message.chat.title}</b> ditambah ke blacklist.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("unbl")
@PY.IDOL("cunbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...")
    try:
        arg = get_arg(message)
        chat_id = int(arg) if arg and arg.lstrip("-").isdigit() else message.chat.id
        blacklist = await get_list_from_vars(client.me.id, "BL_ID") or []

        if chat_id not in blacklist:
            return await status.edit(f"{ggl}Chat tidak ada di blacklist.")

        await remove_from_vars(client.me.id, "BL_ID", chat_id)
        await status.edit(f"{brhsl}Dihapus dari blacklist.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("listbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...")
    blacklist = await get_list_from_vars(client.me.id, "BL_ID") or []

    if not blacklist:
        return await status.edit(f"{ggl}Blacklist kosong.")

    lines = []
    for chat_id in blacklist:
        try:
            chat = await client.get_chat(chat_id)
            lines.append(f"• {chat.title} — <code>{chat.id}</code>")
        except Exception:
            lines.append(f"• <code>{chat_id}</code>")

    text = (
        f"<blockquote><b>Blacklist Broadcast</b></blockquote>\n"
        + "\n".join(lines)
        + f"\n\nTotal: <code>{len(blacklist)}</code>"
    )
    await status.edit(text)


@PY.UBOT("rallbl")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...")
    blacklists = await get_list_from_vars(client.me.id, "BL_ID") or []

    if not blacklists:
        return await status.edit(f"{ggl}Blacklist sudah kosong.")

    for chat_id in list(blacklists):
        await remove_from_vars(client.me.id, "BL_ID", chat_id)

    await status.edit(f"{brhsl}Semua blacklist dihapus.")
