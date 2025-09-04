__MODULE__ = "carbon"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴀʀʙᴏɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}carbon</code>
🦠 ᴋᴇᴛ : ᴍᴇᴍʙᴜᴀᴛ ᴛᴇxᴛ ᴄᴀʀʙᴏɴᴀʀᴀ.</b></blockquote>
"""

import asyncio

from io import BytesIO
from GooUbot import *

async def make_carbon(code):
    url = "https://carbonara.solopov.dev/api/cook"
    async with aiosession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@PY.UBOT("carbon")
@PY.TOP_CMD
async def carbon_func(client, message):
    text = (
        message.text.split(None, 1)[1]
        if len(
            message.command,
        )
        != 1
        else None
    )
    if message.reply_to_message:
        text = message.reply_to_message.text or message.reply_to_message.caption
    if not text:
        return await message.delete()
    ex = await message.reply("memproꜱeꜱ...")
    carbon = await make_carbon(text)
    await ex.edit("uploading...")
    await asyncio.gather(
        ex.delete(),
        client.send_photo(
            message.chat.id,
            carbon,
            caption=f"carboniꜱed by :{client.me.mention}",
        ),
    )
    carbon.close()

@PY.UBOT("font")
@PY.TOP_CMD
async def _(client, message):
    if message.reply_to_message:
        if message.reply_to_message.text:
            query = id(message)
        else:
            return await message.reply("harap reply ke text")
    else:
        if len(message.command) < 2:
            return await message.reply(f"{message.text} [reply/text]")
        else:
            query = id(message)
    try:
        x = await client.get_inline_bot_results(bot.me.username, f"get_font {query}")
        return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        return await message.reply(error)


@PY.INLINE("^get_font")
async def _(client, inline_query):
    get_id = int(inline_query.query.split(None, 1)[1])
    buttons = InlineKeyboard(row_width=3)
    keyboard = []
    for X in query_fonts[0]:
        keyboard.append(
            InlineKeyboardButton(X, callback_data=f"get {get_id} {query_fonts[0][X]}")
        )
    buttons.add(*keyboard)
    buttons.row(InlineKeyboardButton("►", callback_data=f"next {get_id}"))
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get font!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(
                        "silahkan pilih salah satu font dibawah"
                    ),
                )
            )
        ],
    )


@PY.CALLBACK("^get")
async def _(client, callback_query):
    try:
        q = int(callback_query.data.split()[1])
        m = [obj for obj in get_objects() if id(obj) == q][0]
        new = str(callback_query.data.split()[2])
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = m.text.split(None, 1)[1]
        get_new_font = gens_font(new, text)
        return await callback_query.edit_message_text(get_new_font)
    except Exception as error:
        return await callback_query.answer(f"Error: {error}", True)


@PY.CALLBACK("^next")
async def _(client, callback_query):
    try:
        get_id = int(callback_query.data.split()[1])
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in query_fonts[1]:
            keyboard.append(
                InlineKeyboardButton(
                    X, callback_data=f"get {get_id} {query_fonts[1][X]}"
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("◄", callback_data=f"prev {get_id}"))
        return await callback_query.edit_message_reply_markup(reply_markup=buttons)
    except Exception as error:
        return await callback_query.answer(f"Error: {error}", True)


@PY.CALLBACK("^prev")
async def _(client, callback_query):
    try:
        get_id = int(callback_query.data.split()[1])
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in query_fonts[0]:
            keyboard.append(
                InlineKeyboardButton(
                    X, callback_data=f"get {get_id} {query_fonts[0][X]}"
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("►", callback_data=f"next {get_id}"))
        return await callback_query.edit_message_reply_markup(reply_markup=buttons)
    except Exception as error:
        return await callback_query.answer(f"❌ Error: {error}", True)
