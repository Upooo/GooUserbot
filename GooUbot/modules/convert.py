import asyncio
import os

from pyrogram.enums import MessageMediaType, MessagesFilter
from pyrogram.raw.functions.messages import DeleteHistory
from pyrogram.types import InputMediaPhoto

from GooUbot import *

__MODULE__ = "convert"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴠᴇʀᴛ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}toanime</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴘʜᴏᴛᴏ/ꜱᴛɪᴄᴋᴇʀ/ɢɪꜰ ᴍᴇɴᴊᴀᴅɪ ɢᴀᴍʙᴀʀ ᴀɴɪᴍᴇ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}toimg</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ꜱᴛɪᴄᴋᴇʀ/ɢɪꜰ ᴍᴇɴᴊᴀᴅɪ ᴘʜᴏᴛᴏ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}tosticker</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ꜰᴏᴛᴏ ᴍᴇɴᴊᴀᴅɪ ꜱᴛɪᴄᴋᴇʀ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}togif</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ꜱᴛɪᴄᴋᴇʀ ᴍᴇɴᴊᴀᴅɪ ɢɪꜰ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}toaudio</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴠɪᴅᴇᴏ ᴍᴇɴᴊᴀᴅɪ ᴀᴜᴅɪᴏ ᴍᴘ3.</b></blockquote>
"""


@PY.UBOT("toanime")
@PY.TOP_CMD
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    Tm = await message.reply(f"{prs}tunggu sebentar...")
    if message.reply_to_message:
        if len(message.command) < 2:
            if message.reply_to_message.photo:
                file = "foto"
                get_photo = message.reply_to_message.photo.file_id
            elif message.reply_to_message.sticker:
                file = "sticker"
                get_photo = await dl_pic(client, message.reply_to_message)
            elif message.reply_to_message.animation:
                file = "gift"
                get_photo = await dl_pic(client, message.reply_to_message)
            else:
                return await Tm.edit(
                    f"{ggl}mohon balas ke photo/striker/git"
                )
        else:
            if message.command[1] in ["foto", "profil", "photo"]:
                chat = (
                    message.reply_to_message.from_user
                    or message.reply_to_message.sender_chat
                )
                file = "foto profil"
                get = await client.get_chat(chat.id)
                photo = get.photo.big_file_id
                get_photo = await dl_pic(client, photo)
    else:
        if len(message.command) < 2:
            return await Tm.edit(
                f"{ggl}balas ke foto dan saya akan merubah foto anda menjadi anime"
            )
        else:
            try:
                file = "foto"
                get = await client.get_chat(message.command[1])
                photo = get.photo.big_file_id
                get_photo = await dl_pic(client, photo)
            except Exception as error:
                return await Tm.edit(error)
    await Tm.edit("proceꜱꜱing...")
    await client.unblock_user("@qq_neural_anime_bot")
    send_photo = await client.send_photo("@qq_neural_anime_bot", get_photo)
    await asyncio.sleep(30)
    await send_photo.delete()
    await Tm.delete()
    info = await client.resolve_peer("@qq_neural_anime_bot")
    anime_photo = []
    async for anime in client.search_messages(
        "@qq_neural_anime_bot", filter=MessagesFilter.PHOTO
    ):
        anime_photo.append(
            InputMediaPhoto(
                anime.photo.file_id, caption=f"{brhsl}powered by: {bot.me.mention}"
            )
        )
    if anime_photo:
        await client.send_media_group(
            message.chat.id,
            anime_photo,
            reply_to_message_id=message.id,
        )
        return await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))

    else:
        await client.send_message(
            message.chat.id,
            f"{ggl}gagal merubah {file} menjadi gambar anime",
            reply_to_message_id=message.id,
        )
        return await client.invoke(DeleteHistory(peer=info, max_id=0, revoke=True))


@PY.UBOT("toimg")
@PY.TOP_CMD
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    _msg = f"{prs}proceꜱꜱing..."
    Tm = await message.reply(_msg)
  
    try:
        file_io = await dl_pic(client, message.reply_to_message)
        file_io.name = "sticker.png"
        await client.send_photo(
            message.chat.id,
            file_io,
            reply_to_message_id=message.id,
        )
        await Tm.delete()
    except Exception as e:
        await Tm.delete()
        return await client.send_message(
            message.chat.id,
            e,
            reply_to_message_id=message.id,
        )


@PY.UBOT("tosticker")
@PY.TOP_CMD
async def _(client, message):
    try:
        if not message.reply_to_message or not message.reply_to_message.photo:
            return await message.reply_text("reply ke foto untuk mengubah ke sticker")
        sticker = await client.download_media(
            message.reply_to_message.photo.file_id,
            f"sticker_{message.from_user.id}.webp",
        )
        await message.reply_sticker(sticker)
        os.remove(sticker)
    except Exception as e:
        await message.reply_text(str(e))


@PY.UBOT("togif")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    TM = await message.reply(f"{prs}proceꜱꜱing...")
    if not message.reply_to_message.sticker:
        return await TM.edit(f"{ggl}balas ke stiker...")
    await TM.edit(f"{prs}downloading sticker. . .")
    file = await client.download_media(
        message.reply_to_message,
        f"Gift_{message.from_user.id}.mp4",
    )
    try:
        await client.send_animation(
            message.chat.id, file, reply_to_message_id=message.id
        )
        os.remove(file)
        await TM.delete()
    except Exception as error:
        await TM.edit(error)


@PY.UBOT("toaudio")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    ktrng = await EMO.BL_KETERANGAN(client)
    replied = message.reply_to_message
    Tm = await message.reply(f"{prs}tunggu sebentar")
    if not replied:
        return await Tm.edit(f"{ggl}mohon balas ke video")
    if replied.media == MessageMediaType.VIDEO:
        await Tm.edit(f"{prs}downloading video . . ..")
        file = await client.download_media(
            message=replied,
            file_name=f"toaudio_{replied.id}",
        )
        out_file = f"{file}.mp3"
        try:
            await Tm.edit(f"{ktrng}mencoba ekstrak audio. ..")
            cmd = f"ffmpeg -i {file} -q:a 0 -map a {out_file}"
            await run_cmd(cmd)
            await Tm.edit(f"{brhsl}uploading audio . . .")
            await client.send_voice(
                message.chat.id,
                voice=out_file,
                reply_to_message_id=message.id,
            )
            os.remove(file)
            await Tm.delete()
        except Exception as error:
            await Tm.edit(error)
    else:
        return await Tm.edit(f"{ggl}mohon balas ke video")

API_URL = "https://api.exchangerate-api.com/v4/latest/"

@PY.UBOT("convert")
@PY.TOP_CMD
async def convert_currency(client: Client, message: Message):
    args = message.text.split()
    
    if len(args) != 4:
        return await message.reply("❌ Format salah! Gunakan: `/convert [jumlah] [dari] [ke]`.\n\nContoh: `/convert 10000 IDR USD`")

    try:
        amount = float(args[1])
        from_currency = args[2].upper()
        to_currency = args[3].upper()

        # Ambil data nilai tukar terbaru
        response = requests.get(f"{API_URL}{from_currency}")
        data = response.json()

        if "rates" not in data:
            return await message.reply("⚠️ Mata uang tidak ditemukan atau tidak didukung!")

        # Hitung konversi
        if to_currency not in data["rates"]:
            return await message.reply("⚠️ Mata uang tujuan tidak tersedia!")

        converted_amount = amount * data["rates"][to_currency]
        await message.reply(f"💰 **Konversi Mata Uang** 💱\n\n💵 {amount} {from_currency} ≈ **{converted_amount:.2f} {to_currency}**")

    except ValueError:
        await message.reply("❌ Jumlah harus berupa angka!")
    except Exception as e:
        await message.reply(f"⚠️ Terjadi kesalahan: {e}")