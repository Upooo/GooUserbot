__MODULE__ = "note"
__HELP__ = """
<blockquote><b>Notes</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}addnote</code> [nama] (reply)
Simpan catatan.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}get</code> [nama]
Ambil catatan.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}delnote</code> [nama]
Hapus catatan.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}listnote</code>
List semua catatan.</blockquote>

<blockquote><b>Callback:</b>
<code>{0}addcb</code> / <code>{0}delcb</code> / <code>{0}listcb</code></blockquote>

<blockquote>Format tombol: <code>| nama - url |</code>
Satu baris pakai <code>#</code></blockquote>
"""

import re

from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from GooUbot import *


@PY.UBOT("addnote|addcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) != 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [nama]</code> + reply")

    args = get_arg(message)
    reply = message.reply_to_message
    query = "notes_cb" if message.command[0] == "addcb" else "notes"

    if not args or not reply:
        return await message.reply(f"{ggl}<code>{message.command[0]} [nama]</code> + reply")

    existing = await get_vars(client.me.id, args, query)
    if existing:
        return await message.reply(f"{ggl}Catatan <code>{args}</code> sudah ada.")

    value = None
    type_mapping = {
        "text": reply.text,
        "photo": reply.photo,
        "voice": reply.voice,
        "audio": reply.audio,
        "video": reply.video,
        "animation": reply.animation,
        "sticker": reply.sticker,
    }

    for media_type, media in type_mapping.items():
        if media:
            send = await reply.copy(client.me.id)
            value = {"type": media_type, "message_id": send.id}
            break

    if not value:
        return await message.reply(f"{ggl}Media/text tidak didukung.")

    await set_vars(client.me.id, args, value, query)
    return await message.reply(f"{brhsl}Catatan <code>{args}</code> disimpan.")


@PY.UBOT("delnote|delcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    args = get_arg(message)

    if not args:
        return await message.reply(f"{ggl}<code>{message.command[0]} [nama]</code>")

    query = "notes_cb" if message.command[0] == "delcb" else "notes"
    data = await get_vars(client.me.id, args, query)

    if not data:
        return await message.reply(f"{ggl}Catatan <code>{args}</code> tidak ditemukan.")

    await remove_vars(client.me.id, args, query)
    try:
        await client.delete_messages(client.me.id, int(data["message_id"]))
    except Exception:
        pass
    return await message.reply(f"{brhsl}Catatan <code>{args}</code> dihapus.")


@PY.UBOT("get")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    msg = message.reply_to_message or message
    args = get_arg(message)

    if not args:
        return await message.reply(f"{ggl}<code>{message.command[0]} [nama]</code>")

    data = await get_vars(client.me.id, args, "notes")
    if not data:
        return await message.reply(f"{ggl}Catatan <code>{args}</code> tidak ditemukan.")

    m = await client.get_messages(client.me.id, int(data["message_id"]))

    if data["type"] == "text" and m.text and re.findall(r"\| ([^|]+) - ([^|]+) \|", m.text):
        try:
            x = await client.get_inline_bot_results(
                bot.me.username, f"get_notes {client.me.id} {args}"
            )
            return await client.send_inline_bot_result(
                message.chat.id,
                x.query_id,
                x.results[0].id,
                reply_to_message_id=msg.id,
            )
        except Exception as error:
            return await message.reply(f"{ggl}<code>{error}</code>")

    return await m.copy(message.chat.id, reply_to_message_id=msg.id)


@PY.UBOT("listnote|listcb")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    query = "notes_cb" if message.command[0] == "listcb" else "notes"
    vars = await all_vars(client.me.id, query)

    if not vars:
        return await message.reply(f"{ggl}Belum ada catatan.")

    lines = [f"• <code>{name}</code> ({data['type']})" for name, data in vars.items()]
    text = (
        f"<blockquote><b>Daftar catatan</b></blockquote>\n"
        + "\n".join(lines)
        + f"\n\nTotal: <code>{len(vars)}</code>"
    )
    return await message.reply(text, quote=True)


@PY.INLINE("^get_notes")
async def _(client, inline_query):
    query = inline_query.query.split()
    if len(query) < 3:
        return

    data = await get_vars(int(query[1]), query[2], "notes")
    if not data:
        return

    for me in ubot._ubot:
        if me.me.id != int(query[1]):
            continue
        m = await me.get_messages(me.me.id, int(data["message_id"]))
        buttons, text = create_inline_keyboard(m.text, f"{int(query[1])}_{query[2]}")
        return await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="Notes",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text),
                )
            ],
        )


@PY.CALLBACK("_gtnote")
async def _(client, callback_query):
    parts = callback_query.data.split()
    if len(parts) < 2:
        return

    _, user_id, *query = parts
    data_key = "notes_cb" if query else "notes"
    query_split = query[0] if query else user_id.split("_")[1]
    owner_id = int(user_id.split("_")[0])

    data = await get_vars(owner_id, query_split, data_key)
    if not data:
        return await callback_query.answer("Catatan tidak ditemukan.", show_alert=True)

    for me in ubot._ubot:
        if me.me.id != owner_id:
            continue
        try:
            m = await me.get_messages(me.me.id, int(data["message_id"]))
            buttons, text = create_inline_keyboard(
                m.text,
                f"{owner_id}_{user_id.split('_')[1]}",
                bool(query),
            )
            return await callback_query.edit_message_text(text, reply_markup=buttons)
        except Exception:
            return await callback_query.answer("Gagal load callback.", show_alert=True)
