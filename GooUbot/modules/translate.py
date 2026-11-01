__MODULE__ = "translate"
__HELP__ = """
<blockquote><b>Translate</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}tr</code> [reply/text]
Terjemahkan ke bahasa yang di-set.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}tts</code> [reply/text]
Text-to-speech.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}setlang</code>
Ubah bahasa translate/TTS.</blockquote>
"""

import os
from gc import get_objects

import gtts
from gpytranslate import Translator
from pykeyboard import InlineKeyboard
from pyrogram.types import InlineKeyboardButton, InlineQueryResultArticle, InputTextMessageContent

from GooUbot import *


@PY.UBOT("tts")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Processing...")

    if message.reply_to_message:
        language = client._translate.get(client.me.id, "id")
        words = message.reply_to_message.text or message.reply_to_message.caption
    else:
        if len(message.command) < 2:
            return await status.edit(f"{ggl}<code>{message.command[0]} [reply/text]</code>")
        language = client._translate.get(client.me.id, "id")
        words = message.text.split(None, 1)[1]

    if not words:
        return await status.edit(f"{ggl}Tidak ada teks.")

    path = f"tts_{client.me.id}.ogg"
    try:
        speech = gtts.gTTS(words, lang=language)
        speech.save(path)
        rep = message.reply_to_message or message
        await client.send_voice(
            chat_id=message.chat.id,
            voice=path,
            reply_to_message_id=rep.id,
        )
        await status.delete()
    except Exception as error:
        await status.edit(f"{ggl}<code>{error}</code>")
    finally:
        if os.path.exists(path):
            os.remove(path)


@PY.UBOT("tr")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Processing...")
    trans = Translator()

    if message.reply_to_message:
        dest = client._translate.get(client.me.id, "id")
        to_translate = message.reply_to_message.text or message.reply_to_message.caption
    else:
        if len(message.command) < 2:
            return await status.edit(f"{ggl}<code>{message.command[0]} [reply/text]</code>")
        dest = client._translate.get(client.me.id, "id")
        to_translate = message.text.split(None, 1)[1]

    if not to_translate:
        return await status.edit(f"{ggl}Tidak ada teks.")

    try:
        source = await trans.detect(to_translate)
        translation = await trans(to_translate, sourcelang=source, targetlang=dest)
        rep = message.reply_to_message or message
        await status.delete()
        await client.send_message(
            message.chat.id,
            translation.text,
            reply_to_message_id=rep.id,
        )
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("setlang")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    query = id(message)
    try:
        x = await client.get_inline_bot_results(bot.me.username, f"ubah_bahasa {query}")
        return await message.reply_inline_bot_result(x.query_id, x.results[0].id)
    except Exception as error:
        return await message.reply(f"{ggl}<code>{error}</code>")


@PY.INLINE("^ubah_bahasa")
async def _(client, inline_query):
    buttons = InlineKeyboard(row_width=3)
    keyboard = []
    for lang in lang_code_translate:
        keyboard.append(
            InlineKeyboardButton(
                Fonts.smallcap(lang.lower()),
                callback_data=f"set_bahasa {int(inline_query.query.split()[1])} {lang}",
            )
        )
    buttons.add(*keyboard)
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            InlineQueryResultArticle(
                title="Pilih bahasa",
                reply_markup=buttons,
                input_message_content=InputTextMessageContent(
                    "Pilih bahasa translate / TTS:"
                ),
            )
        ],
    )


@PY.CALLBACK("^set_bahasa")
async def _(client, callback_query):
    data = callback_query.data.split()
    try:
        m = [obj for obj in get_objects() if id(obj) == int(data[1])][0]
        m._client._translate[m._client.me.id] = lang_code_translate[data[2]]
        await callback_query.edit_message_text(
            f"Bahasa diubah ke: <b>{Fonts.smallcap(data[2].lower())}</b>"
        )
    except Exception as error:
        await callback_query.edit_message_text(f"<code>{error}</code>")
