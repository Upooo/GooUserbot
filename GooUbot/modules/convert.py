__MODULE__ = "convert"
__HELP__ = """
<blockquote><b>Convert</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}toanime</code> — foto/sticker → anime
<code>{0}toimg</code> — sticker → foto
<code>{0}tosticker</code> — foto → sticker
<code>{0}togif</code> — sticker → gif
<code>{0}toaudio</code> — video → audio
<code>{0}convert</code> [jumlah] [dari] [ke] — konversi mata uang</blockquote>
"""

import asyncio
import os

import requests
from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto

from GooUbot import *

API_URL = "https://api.exchangerate-api.com/v4/latest/"


@PY.UBOT("toanime")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Processing...")

    get_photo = None
    file = "media"

    if message.reply_to_message:
        reply = message.reply_to_message
        if reply.photo:
            file = "foto"
            get_photo = reply.photo.file_id
        elif reply.sticker:
            file = "sticker"
            get_photo = await dl_pic(client, reply)
        elif reply.animation:
            file = "gif"
            get_photo = await dl_pic(client, reply)
        else:
            return await status.edit(f"{ggl}Reply ke foto/sticker/gif.")
    elif len(message.command) >= 2:
        try:
            file = "foto"
            chat = await client.get_chat(message.command[1])
            get_photo = await dl_pic(client, chat.photo.big_file_id)
        except Exception as e:
            return await status.edit(f"{ggl}<code>{e}</code>")
    else:
        return await status.edit(f"{ggl}Reply ke foto atau kasih username.")

    try:
        await client.unblock_user("qq_neural_anime_bot")
        send_photo = await client.send_photo("qq_neural_anime_bot", get_photo)
        await asyncio.sleep(25)
        await send_photo.delete()

        anime_photo = []
        async for anime in client.search_messages(
            "qq_neural_anime_bot", filter=MessagesFilter.PHOTO
        ):
            anime_photo.append(
                InputMediaPhoto(
                    anime.photo.file_id,
                    caption=f"{brhsl}powered by {bot.me.mention}",
                )
            )

        if anime_photo:
            await client.send_media_group(
                message.chat.id, anime_photo, reply_to_message_id=message.id
            )
        else:
            await message.reply(f"{ggl}Gagal convert {file} ke anime.")

        info = await client.resolve_peer("qq_neural_anime_bot")
        await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("toimg")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Processing...")

    if not message.reply_to_message:
        return await status.edit(f"{ggl}Reply ke sticker.")

    try:
        file_io = await dl_pic(client, message.reply_to_message)
        file_io.name = "sticker.png"
        await client.send_photo(
            message.chat.id, file_io, reply_to_message_id=message.id
        )
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("tosticker")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    if not message.reply_to_message or not message.reply_to_message.photo:
        return await message.reply(f"{ggl}Reply ke foto.")

    path = f"sticker_{message.from_user.id}.webp"
    try:
        sticker = await client.download_media(
            message.reply_to_message.photo.file_id, path
        )
        await message.reply_sticker(sticker)
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
    finally:
        if os.path.exists(path):
            os.remove(path)


@PY.UBOT("togif")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Processing...")

    if not message.reply_to_message or not message.reply_to_message.sticker:
        return await status.edit(f"{ggl}Reply ke sticker.")

    path = f"gif_{message.from_user.id}.mp4"
    try:
        file = await client.download_media(message.reply_to_message, path)
        await client.send_animation(
            message.chat.id, file, reply_to_message_id=message.id
        )
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
    finally:
        if os.path.exists(path):
            os.remove(path)


@PY.UBOT("toaudio")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Processing...")

    replied = message.reply_to_message
    if not replied or replied.media != MessageMediaType.VIDEO:
        return await status.edit(f"{ggl}Reply ke video.")

    file = None
    out_file = None
    try:
        file = await client.download_media(
            message=replied, file_name=f"toaudio_{replied.id}"
        )
        out_file = f"{file}.mp3"
        await run_cmd(f"ffmpeg -i {file} -q:a 0 -map a {out_file} -y -loglevel error")
        await client.send_voice(
            message.chat.id, voice=out_file, reply_to_message_id=message.id
        )
        await status.edit(f"{brhsl}Done.")
        await asyncio.sleep(1)
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
    finally:
        for p in (file, out_file):
            if p and os.path.exists(p):
                os.remove(p)


@PY.UBOT("convert")
@PY.TOP_CMD
async def convert_currency(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    args = message.text.split()

    if len(args) != 4:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [jumlah] [dari] [ke]</code>\n"
            f"Contoh: <code>{message.command[0]} 10000 IDR USD</code>"
        )

    try:
        amount = float(args[1])
        from_currency = args[2].upper()
        to_currency = args[3].upper()

        response = requests.get(f"{API_URL}{from_currency}", timeout=15)
        data = response.json()

        if "rates" not in data or to_currency not in data["rates"]:
            return await message.reply(f"{ggl}Mata uang tidak didukung.")

        converted = amount * data["rates"][to_currency]
        await message.reply(
            f"{brhsl}<b>{amount:,.2f} {from_currency}</b> ≈ "
            f"<b>{converted:,.2f} {to_currency}</b>"
        )
    except ValueError:
        await message.reply(f"{ggl}Jumlah harus angka.")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
