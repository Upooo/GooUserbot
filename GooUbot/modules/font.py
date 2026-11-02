__MODULE__ = "font"
__HELP__ = """
<blockquote><b>Font</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}font</code> [teks/reply]
Ubah teks ke berbagai style font.</blockquote>
"""

from uuid import uuid4

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from GooUbot import *
from GooUbot.core.helpers.font_help import gens_font, query_fonts

FONT_CACHE = {}


def save_font_text(text: str):
    key = str(uuid4())[:8]
    FONT_CACHE[key] = text
    if len(FONT_CACHE) > 500:
        FONT_CACHE.pop(next(iter(FONT_CACHE)))
    return key


def build_font_markup(page: int, text_id: str):
    rows = []
    temp = []

    for name, style in query_fonts[page].items():
        temp.append(
            InlineKeyboardButton(text=name, callback_data=f"font|{style}|{text_id}")
        )
        if len(temp) == 2:
            rows.append(temp)
            temp = []
    if temp:
        rows.append(temp)

    nav = []
    if page > 0:
        nav.append(
            InlineKeyboardButton("Prev", callback_data=f"fontpage|{page-1}|{text_id}")
        )
    if page < len(query_fonts) - 1:
        nav.append(
            InlineKeyboardButton("Next", callback_data=f"fontpage|{page+1}|{text_id}")
        )
    if nav:
        rows.append(nav)

    return InlineKeyboardMarkup(rows)


@PY.UBOT("font")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)

    text = None
    if message.reply_to_message and message.reply_to_message.text:
        text = message.reply_to_message.text
    elif len(message.command) > 1:
        text = message.text.split(None, 1)[1]

    if not text:
        return await message.reply(f"{ggl}<code>{message.command[0]} [teks/reply]</code>")

    text_id = save_font_text(text)
    await message.reply(
        "Pilih font:",
        reply_markup=build_font_markup(page=0, text_id=text_id),
    )


@PY.CALLBACK("^font\\|")
async def font_callback(client, callback_query):
    try:
        await callback_query.answer()
        _, style, text_id = callback_query.data.split("|", 2)
        text = FONT_CACHE.get(text_id)
        if not text:
            return await callback_query.edit_message_text("Text expired. Ulangi command.")
        result = gens_font(style, text)
        await callback_query.edit_message_text(result)
    except Exception as e:
        await callback_query.answer(str(e), show_alert=True)


@PY.CALLBACK("^fontpage\\|")
async def font_page(client, callback_query):
    try:
        await callback_query.answer()
        _, page, text_id = callback_query.data.split("|", 2)
        await callback_query.edit_message_reply_markup(
            reply_markup=build_font_markup(int(page), text_id)
        )
    except Exception as e:
        await callback_query.answer(str(e), show_alert=True)
