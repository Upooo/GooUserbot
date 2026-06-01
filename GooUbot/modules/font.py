from uuid import uuid4

from GooUbot import *
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)

__MODULE__ = "font"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜰᴏɴᴛ--</b></blockquote>

<blockquote>
<b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}font</code>
🦠 ᴋᴇᴛ : reply text / kasih text buat ubah font.
</blockquote>
"""

# ==========================================================
# CACHE
# ==========================================================

FONT_CACHE = {}


def save_font_text(text: str):
    key = str(uuid4())[:8]
    FONT_CACHE[key] = text

    # anti memory leak kecil
    if len(FONT_CACHE) > 500:
        FONT_CACHE.pop(next(iter(FONT_CACHE)))

    return key


# ==========================================================
# BUILD BUTTONS
# ==========================================================

def build_font_markup(page: int, text_id: str):
    rows = []
    temp = []

    fonts = list(query_fonts[page].items())

    for name, style in fonts:
        temp.append(
            InlineKeyboardButton(
                text=name,
                callback_data=f"font|{style}|{text_id}"
            )
        )

        # 2 tombol per row
        if len(temp) == 2:
            rows.append(temp)
            temp = []

    if temp:
        rows.append(temp)

    nav_buttons = []

    if page > 0:
        nav_buttons.append(
            InlineKeyboardButton(
                "⬅️ Prev",
                callback_data=f"fontpage|{page-1}|{text_id}"
            )
        )

    if page < len(query_fonts) - 1:
        nav_buttons.append(
            InlineKeyboardButton(
                "Next ➡️",
                callback_data=f"fontpage|{page+1}|{text_id}"
            )
        )

    if nav_buttons:
        rows.append(nav_buttons)

    return InlineKeyboardMarkup(rows)


# ==========================================================
# COMMAND
# ==========================================================

@PY.UBOT("font")
@PY.TOP_CMD
async def font_cmd(client, message):
    text = None

    # reply text
    if (
        message.reply_to_message
        and message.reply_to_message.text
    ):
        text = message.reply_to_message.text

    # arg text
    elif len(message.command) > 1:
        text = message.text.split(None, 1)[1]

    if not text:
        return await message.reply_text(
            "Reply text atau kasih text dulu."
        )

    text_id = save_font_text(text)

    markup = build_font_markup(
        page=0,
        text_id=text_id
    )

    await message.reply_text(
        "Pilih font dibawah 👇",
        reply_markup=markup
    )


# ==========================================================
# FONT CALLBACK
# ==========================================================

@PY.CALLBACK("^font\\|")
async def font_callback(client, callback_query):
    try:
        # jawab callback biar gak loading terus
        await callback_query.answer()

        _, style, text_id = (
            callback_query.data.split("|", 2)
        )

        text = FONT_CACHE.get(text_id)

        if not text:
            return await callback_query.edit_message_text(
                "⚠️ Text expired, coba ulang command."
            )

        result = gens_font(style, text)

        await callback_query.edit_message_text(
            result
        )

    except Exception as error:
        await callback_query.answer(
            str(error),
            show_alert=True
        )


# ==========================================================
# PAGE CALLBACK
# ==========================================================

@PY.CALLBACK("^fontpage\\|")
async def font_page(client, callback_query):
    try:
        await callback_query.answer()

        _, page, text_id = (
            callback_query.data.split("|", 2)
        )

        page = int(page)

        markup = build_font_markup(
            page=page,
            text_id=text_id
        )

        await callback_query.edit_message_reply_markup(
            reply_markup=markup
        )

    except Exception as error:
        await callback_query.answer(
            str(error),
            show_alert=True
        )
