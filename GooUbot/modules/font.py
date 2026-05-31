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

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}font</code>
🦠 ᴋᴇᴛ : ʀᴇᴘʟʏ ᴛᴇxᴛ ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ꜰᴏɴᴛ.</blockquote>
"""

# ---------------- FONT COMMAND ----------------
@PY.UBOT("font")
@PY.TOP_CMD
async def font_cmd(client, message):
    if message.reply_to_message and message.reply_to_message.text:
        text = message.reply_to_message.text
    else:
        if len(message.command) < 2:
            return await message.reply("reply / kasih text dulu")
        text = message.text.split(None, 1)[1]

    try:
        x = await client.get_inline_bot_results(
            bot.me.username,
            f"get_font {text}"
        )
        return await message.reply_inline_bot_result(
            x.query_id,
            x.results[0].id
        )
    except Exception as error:
        return await message.reply(f"Error: {error}")


# ---------------- INLINE ----------------
@PY.INLINE("^get_font")
async def font_inline(client, inline_query):
    text = inline_query.query.split(None, 1)[1]

    buttons = []

    # halaman 1 fonts
    for name, style in query_fonts[0].items():
        buttons.append(
            InlineKeyboardButton(
                name,
                callback_data=f"font|{style}|{text}"
            )
        )

    markup = InlineKeyboardMarkup([buttons])

    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            InlineQueryResultArticle(
                title="Font Generator",
                input_message_content=InputTextMessageContent(
                    "pilih font dibawah"
                ),
                reply_markup=markup
            )
        ],
    )


# ---------------- CALLBACK FONT ----------------
@PY.CALLBACK("^font")
async def font_callback(client, callback_query):
    try:
        _, style, text = callback_query.data.split("|", 2)

        result = gens_font(style, text)

        return await callback_query.edit_message_text(result)

    except Exception as error:
        return await callback_query.answer(f"Error: {error}", True)


# ---------------- NEXT PAGE ----------------
@PY.CALLBACK("^next_font")
async def next_page(client, callback_query):
    buttons = []

    for name, style in query_fonts[1].items():
        buttons.append(
            InlineKeyboardButton(
                name,
                callback_data=f"font|{style}|test"
            )
        )

    markup = InlineKeyboardMarkup([buttons])

    return await callback_query.edit_message_reply_markup(markup)


# ---------------- PREV PAGE ----------------
@PY.CALLBACK("^prev_font")
async def prev_page(client, callback_query):
    buttons = []

    for name, style in query_fonts[0].items():
        buttons.append(
            InlineKeyboardButton(
                name,
                callback_data=f"font|{style}|test"
            )
        )

    markup = InlineKeyboardMarkup([buttons])

    return await callback_query.edit_message_reply_markup(markup)