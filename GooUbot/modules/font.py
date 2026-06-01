from uuid import uuid4

from GooUbot import *
from pyrogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent
)

__MODULE__ = "font"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ꜰᴏɴᴛ--</b></blockquote>

<blockquote>
<b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}font</code>
🦠 ᴋᴇᴛ : ʀᴇᴘʟʏ text / kasih text buat ubah font.
</blockquote>
"""

# ==========================================================
# CACHE TEXT
# ==========================================================

FONT_CACHE = {}


def save_font_text(text: str):
    key = str(uuid4())[:8]
    FONT_CACHE[key] = text

    # anti memory leak kecil-kecilan
    if len(FONT_CACHE) > 500:
        FONT_CACHE.pop(next(iter(FONT_CACHE)))

    return key


# ==========================================================
# BUILD BUTTONS
# ==========================================================

def build_font_markup(page: int, text_id: str):
    fonts = list(query_fonts[page].items())

    rows = []
    temp = []

    for name, style in fonts:
        temp.append(
            InlineKeyboardButton(
                name,
                callback_data=f"font|{style}|{text_id}"
            )
        )

        if len(temp) == 2:
            rows.append(temp)
            temp = []

    if temp:
        rows.append(temp)

    nav = []

    if page > 0:
        nav.append(
            InlineKeyboardButton(
                "⬅️ Prev",
                callback_data=f"fontpage|{page-1}|{text_id}"
            )
        )

    if page < len(query_fonts) - 1:
        nav.append(
            InlineKeyboardButton(
                "Next ➡️",
                callback_data=f"fontpage|{page+1}|{text_id}"
            )
        )

    if nav:
        rows.append(nav)

    return InlineKeyboardMarkup(rows)


# ==========================================================
# COMMAND
# ==========================================================

@PY.UBOT("font")
@PY.TOP_CMD
async def font_cmd(client, message):
    text = None

    if (
        message.reply_to_message
        and message.reply_to_message.text
    ):
        text = message.reply_to_message.text

    elif len(message.command) > 1:
        text = message.text.split(None, 1)[1]

    if not text:
        return await message.reply(
            "reply text atau kasih text dulu."
        )

    try:
        x = await client.get_inline_bot_results(
            bot.me.username,
            f"get_font {text}"
        )

        await message.reply_inline_bot_result(
            x.query_id,
            x.results[0].id
        )

    except Exception as error:
        await message.reply(
            f"<b>Error:</b> <code>{error}</code>"
        )


# ==========================================================
# INLINE
# ==========================================================

@PY.INLINE("^get_font")
async def font_inline(client, inline_query):
    try:
        parts = inline_query.query.split(None, 1)

        if len(parts) < 2:
            return await client.answer_inline_query(
                inline_query.id,
                results=[],
                cache_time=0
            )

        text = parts[1]
        text_id = save_font_text(text)

        markup = build_font_markup(0, text_id)

        await client.answer_inline_query(
            inline_query.id,
            cache_time=0,
            results=[
                InlineQueryResultArticle(
                    title="Font Generator",
                    description="Klik untuk pilih font",
                    input_message_content=InputTextMessageContent(
                        "Pilih font dibawah 👇"
                    ),
                    reply_markup=markup
                )
            ]
        )

    except Exception as e:
        print(f"INLINE ERROR: {e}")


# ==========================================================
# CALLBACK FONT
# ==========================================================

@PY.CALLBACK("^font\\|")
async def font_callback(client, callback_query):
    try:
        # jawab callback dulu
        await callback_query.answer()

        _, style, text_id = (
            callback_query.data.split("|", 2)
        )

        text = FONT_CACHE.get(text_id)

        if not text:
            return await callback_query.edit_message_text(
                "Text expired, coba ulang command."
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
# PAGE SWITCH
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
            page,
            text_id
        )

        await callback_query.edit_message_reply_markup(
            markup
        )

    except Exception as error:
        await callback_query.answer(
            str(error),
            show_alert=True
        )
