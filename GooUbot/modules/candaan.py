from pyrogram import Client
import requests
import os
from PIL import Image, ImageDraw, ImageFont, ImageOps
from pyrogram import Client
from pyrogram.types import User, Chat
from GooUbot import *

__MODULE__ = "havefun"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʜᴀᴠᴇ ꜰᴜɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}artinama [nama]</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴊᴇʟᴀꜱᴋᴀɴ ᴀʀᴛɪ ɴᴀᴍᴀ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekkhodam</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋʜᴏᴅᴀᴍ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekganteng</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ɢᴀɴᴛᴇɴɢ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekcantik</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴄᴀɴᴛɪᴋ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekkontol</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋᴏɴᴛᴏʟ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekmemek</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴍᴇᴍᴇᴋ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}tf</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴛꜰ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekimut</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ɪᴍᴜᴛ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}ceksempak</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ꜱᴇᴍᴘᴀᴋ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekagama</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴀɢᴀᴍᴀ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}ceksange</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ꜱᴀɴɢᴇ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekbh</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ʙʜ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cekkesadaran</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋᴇꜱᴀᴅᴀʀᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ.</b></blockquote>
"""

AGAMA_LIST = [
    "Islam", "Kristen", "Katolik", "Hindu", "Buddha", "Konghucu",
    "Atheis", "Animisme", "Yahudi", "Kejawen", "Pemuja Bot"
]

@PY.UBOT("cekagama")
@PY.TOP_CMD
async def cek_agama(client, message: Message):
    if not message.reply_to_message or not message.reply_to_message.from_user:
        return await message.reply_text(
            "<b>❗ Harap reply ke pesan seseorang untuk mendeteksi agamanya (becandaan ya 🤭)</b>"
        )

    target_user = message.reply_to_message.from_user
    user_id = target_user.id
    nama = target_user.first_name

    # Cek apakah itu owner bot
    if user_id in DEVS:
        return await message.reply_text("⛔ <b>ITU OWNER GUA GAUSAH DI CEK CEK KONTOL!</b>")

    agama = random.choice(AGAMA_LIST)

    hasil = f"""
<blockquote><b>📿 HASIL DETEKSI AGAMA

Nama : {nama}
Agama : {agama}

✅ Selamat ya, agamanya cocok kok.
📝 Note: Maaf ya {nama}, ini cuma becandaan 😁</b></blockquote>
"""
    await message.reply_text(hasil)
@PY.UBOT("cekkodam")
@PY.TOP_CMD
async def cekkhodam(client, message):
    try:
        SAIKO_SAHABAT = 6244458400
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋʜᴏᴅᴀᴍ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit(f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ᴋʜᴏᴅᴀᴍ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama} (ᴏᴡɴᴇʀ)
ᴋʜᴏᴅᴀᴍ : ʜᴀʀɪᴍᴀᴜ ᴘᴜᴛɪʜ
ᴊɪʀ ᴋᴏᴅᴀᴍ ᴏᴡɴᴇʀ ᴇᴍᴀɴɢ ᴘᴀʟɪɴɢ ʙᴇꜱᴛ</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
""")
        # elif user_id == SAIKO_SAHABAT:
        #     return await message.edit("Et dah sahabat owner gua itu, jelas ganteng lah tot!")
        
        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ᴋʜᴏᴅᴀᴍ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ᴋʜᴏᴅᴀᴍ : {random.choice(['lonte gurun', 'dugong', 'macan yatim', 'buaya darat', 'kanjut terbang', 'kuda kayang', 'janda salto', 'lonte alas', 'jembut singa', 'gajah terbang', 'kuda cacat', 'jembut pink', 'sabun bolong'])}
ɴɢᴇʀɪ ʙᴇᴛ ᴊɪʀ ᴋʜᴏᴅᴀᴍɴʏᴀ</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("cekganteng|cekgtg")
@PY.TOP_CMD
async def cekgtg(client, message):
    try:
        SAIKO_SAHABAT = 6244458400
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ɢᴀɴᴛᴇɴɢ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit("<b>OWNER GUA JELAS GANTENG BANGET LAH ANJING!</b>")

        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ɢᴀɴᴛᴇɴɢ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ɢᴀɴᴛᴇɴɢ : {random.choice(['ʟᴜᴍᴀʏᴀɴ', 'ᴊᴇʟᴇᴋ', 'ᴛɪᴘɪꜱ', 'ʙᴀɴɢᴇᴛ', 'ᴏᴋ ʟᴀʜ', 'ᴊᴇʟᴇᴋ ᴅɪᴋɪᴛ', 'ɢᴀɴᴛᴇɴɢ ᴅɪᴋɪᴛ'])}</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("cekcantik|cekcntk")
@PY.TOP_CMD
async def cekcantik(client, message):
    try:
        PIRAEPEP = 1760398550
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴄᴀɴᴛɪᴋ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit("<b>⛔ OWNER GUA COWO JING MASA CANTIK!</b>")
        elif user_id == PIRAEPEP:
            return await message.edit("<b>PIRA MAH UDAH FIX CANTIK CUY!</b>")

        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ᴄᴀɴᴛɪᴋ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ᴄᴀɴᴛɪᴋ : {random.choice(['ʟᴜᴍᴀʏᴀɴ', 'ᴊᴇʟᴇᴋ', 'ᴛɪᴘɪꜱ', 'ʙᴀɴɢᴇᴛ', 'ᴏᴋ ʟᴀʜ', 'ᴊᴇʟᴇᴋ ᴅɪᴋɪᴛ', 'ᴄᴀɴᴛɪᴋ ʙᴀɴɢᴇᴛ ᴊɪɴɢ'])}</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("cekkontol|cekkntl")
@PY.TOP_CMD
async def cekkntl(client, message):
    try:
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋᴏɴᴛᴏʟ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit(f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ᴋᴏɴᴛᴏʟ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama} (ᴏᴡɴᴇʀ)
ᴡᴀʀɴᴀ ᴋᴏɴᴛᴏʟ : pink
ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : normal
ᴜᴋᴜʀᴀɴ ᴋᴏɴᴛᴏʟ : 23cm
ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : gede ber otot
<b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
""")
        # elif user_id == SAIKO_SAHABAT:
        #     return await message.edit("Et dah sahabat owner gua itu, jelas ganteng lah tot!")
        
        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ᴋᴏɴᴛᴏʟ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ᴡᴀʀɴᴀ ᴋᴏɴᴛᴏʟ : {random.choice(['irenk', 'pink', 'rainbow', 'hitam cok', 'kuning'])}
ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {random.choice(['irenk', 'pink', 'rainbow', 'hitam cok', 'kuning'])}
ᴜᴋᴜʀᴀɴ ᴋᴏɴᴛᴏʟ : {random.choice(['10cm', '12cm', '13cm', '14cm', '15cm', '16cm', '17cm', '18cm', '19cm', '20cm', '21cm', '22cm', '23cm', '24cm', '25cm', '26cm', '27cm', '28cm', '29cm', '30cm'])}
ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {random.choice(['bengkok', 'bengkok dikit', 'lurus', 'panjang kecil', 'lebar', 'tumpul'])}
</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("cekmemek|cekmmk")
@PY.TOP_CMD
async def cekmmk(client, message):
    try:
        SAIKO_SAHABAT = 6244458400
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴍᴇᴍᴇᴋ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit("<b>OWNER GUA GA PUNYA MEMEK TOLOL! KAN DIA COWO.</b>")
        # elif user_id == SAIKO_SAHABAT:
        #     return await message.edit("Et dah sahabat owner gua itu, jelas ganteng lah tot!")
        
        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ᴍᴇᴍᴇᴋ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ᴡᴀʀɴᴀ ᴍᴇᴍᴇᴋ : {random.choice(['irenk', 'pink', 'rainbow', 'hitam cok', 'kuning'])}
ᴡᴀʀɴᴀ ᴊᴇᴍʙᴜᴛ : {random.choice(['irenk', 'pink', 'rainbow', 'hitam cok', 'kuning'])}
ᴜᴋᴜʀᴀɴ ʟᴏʙᴀɴɢ : {random.choice(['16 inc', '10 inc', '15 inc', '6 inc', '1 inc', '3 inc'])}
ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {random.choice(['berjembut', 'dah jebol', 'bau trasi', 'berlendir', 'lebar itam', 'sempit'])}
</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("artinama")
async def _(client, message):
    if len(message.command) < 2:
        await message.reply_text("<blockquote><b>ɢᴜɴᴀᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ :</b> <code>.artinama nama</blockquote>")
        return

    nama = " ".join(message.command[1:])
    api_url = f"https://api.siputzx.my.id/api/primbon/artinama?nama={nama}"

    try:
        response = requests.get(api_url).json()

        if response.get("status"):
            nama_res = response["data"]["nama"].title()
            arti_res = response["data"]["arti"]
            catatan_res = response["data"].get("catatan", "")

            reply_text = (
                f"<blockquote><b>🔍 ᴀʀᴛɪ ɴᴀᴍᴀ : {nama_res}\n\n</b></blockquote>"
                f"<blockquote><b>📖 {arti_res}\n</b></blockquote>"
            )

            if catatan_res:
                reply_text += f"<blockquote><b>\n💡 {catatan_res}</b></blockquote>"

            await message.reply_text(reply_text)
        else:
            await message.reply_text(f"<blockquote><b>❌ ᴍᴀᴀꜰ, ᴀʀᴛɪ ɴᴀᴍᴀ {nama} ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ.</b></blockquote>")
    except Exception as e:
        await message.reply_text(f"<blockquote><b>⚠️ ᴛᴇʀᴊᴀᴅɪ ᴋᴇꜱᴀʟᴀʜᴀɴ ꜱᴀᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀᴛᴀ :</b>\n<code>{str(e)}</code></blockquote>")
        
@PY.UBOT("tf|transfer")
@PY.TOP_CMD
async def fake_transfer(client, message):
    if not message.reply_to_message:
        return await message.reply("❗ ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ɪɴɢɪɴ ᴋᴀᴍᴜ ᴛʀᴀɴꜱꜰᴇʀ.")
    
    target = message.reply_to_message.from_user
    if not target:
        return await message.reply("❗ ɢᴀɢᴀʟ ᴍᴇɴᴅᴀᴘᴀᴛᴋᴀɴ ɪɴꜰᴏʀᴍᴀꜱɪ ᴘᴇɴɢɢᴜɴᴀ.")

    # Ambil nominal dari argumen
    text_split = message.text.split()
    if len(text_split) < 2:
        return await message.reply("💸 ꜰᴏʀᴍᴀᴛ ꜱᴀʟᴀʜ!\nɢᴜɴᴀᴋᴀɴ : <code>.transfer 1000</code> (balas pesan seseorang)")

    nominal_input = text_split[1]
    try:
        nominal = int(nominal_input.replace(".", "").replace(",", ""))
        nominal_str = f"Rp {nominal:,}".replace(",", ".") + ",-"
    except:
        return await message.reply("💸 ɴᴏᴍɪɴᴀʟ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. ᴄᴏɴᴛᴏʜ : `.transfer 5000`")

    hasil = f"""
<blockquote><b>💳 ʟᴀᴘᴏʀᴀɴ ᴛʀᴀɴꜱꜰᴇʀ :

ᴛʀᴀɴꜱꜰᴇʀ ᴋᴇ : {target.first_name}
ɴᴏᴍɪɴᴀʟ : {nominal_str}

✅ ᴛʀᴀɴꜱꜰᴇʀ ʙᴇʀʜᴀꜱɪʟ, ꜱɪʟᴀʜᴋᴀɴ ᴄᴇᴋ ᴍᴜᴛᴀꜱɪ ʀᴇᴋᴇɴɪɴɢ ᴀɴᴅᴀ.</b></blockquote><b>
"""
    await message.reply(hasil)

@PY.UBOT("cekimut|cekcute")
@PY.TOP_CMD
async def cekimut(client, message):
    try:
        SAIKO_SAHABAT = 6244458400
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ɪᴍᴜᴛ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit(f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ɪᴍᴜᴛ :</b></blockquote>
<blockquote><>
ɴᴀᴍᴀ : nathann. (ᴏᴡɴᴇʀ)
ɪᴍᴜᴛ : banget lah geloo
</blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
""")
        # elif user_id == SAIKO_SAHABAT:
        #     return await message.edit("Et dah sahabat owner gua itu, jelas ganteng lah tot!")
        
        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ɪᴍᴜᴛ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ɪᴍᴜᴛ : {random.choice(['lumayan', 'b aja', 'ok lah', 'najis', 'imut anet'])}
</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("cekbh")
@PY.TOP_CMD
async def cekmmk(client, message):
    try:
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ʙʜ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit("<b>⛔ OWNER GUA GA MAKE BH TOLOL! KAN DIA COWO.</b>")
        
        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ʙʜ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ᴡᴀʀɴᴀ ʙʜ : {random.choice(['merah', 'pink', 'kuning', 'rainbow', 'orange', 'biru', 'hitam', 'hijau', 'maroon','navi'])}
ᴜᴋᴜʀᴀɴ ʙʜ : {random.choice(['32b', '32c', '34b', '43c', '35b', '35c', '30b', '30c', '28b', '28c', '26b', '26c', 'gamake bh'])}
ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {random.choice(['jarang make', 'ga di cuci', 'lumutan', 'bau', 'suka di cium', 'jarang ganti', 'tali copot 1'])}
</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("ceksempak|cekcangcut")
@PY.TOP_CMD
async def ceksmpk(client, message):
    try:
        SAIKO_SAHABAT = 6244458400
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴄᴇʟᴀɴᴀ ᴅᴀʟᴀᴍ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit("GAUSAH CEK CEK OWNER GUA MEMEK!")
        
        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ꜱᴇᴍᴘᴀᴋ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ᴡᴀʀɴᴀ ꜱᴇᴍᴘᴀᴋ : {random.choice(['merah', 'pink', 'kuning', 'rainbow', 'orange', 'biru', 'hitam', 'hijau', 'maroon','navi'])}
ᴜᴋᴜʀᴀɴ ꜱᴇᴍᴘᴀᴋ : {random.choice(['gamake sempak', 'L', 'XL', 'XXL', 'S', 'XXS', 'M', 'XS', 'XXXL', 'pake sarung'])}
ᴄɪʀɪ ᴄɪʀɪɴʏᴀ : {random.choice(['jarang make', 'ga di cuci', 'lumutan', 'bau', 'suka di cium', 'jarang ganti', 'tali copot 1'])}
</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("cekkesadaran")
@PY.TOP_CMD
async def cekksdran(client, message):
    try:
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ ᴋᴇꜱᴀᴅᴀʀᴀɴ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit("⛔ ITU OWNER GUA YA JELAS SADAR LAH, KALO GA MAH GUA GABAKAL JADI!")

        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ ᴋᴇꜱᴀᴅᴀʀᴀɴ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
ᴋᴇꜱᴀᴅᴀʀᴀɴ : {random.choice(['stres akut','gila akut', 'gila dikit', 'stres', 'hampir mati', 'pengan bundir', 'ga kuat', 'kena mental', 'waras', 'ga waras', 'sadar dikit', 'oleng', 'mabok', 'TINGGI NICH'])}</b></blockquote>
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")

@PY.UBOT("ceksange")
@PY.TOP_CMD
async def cekksnge(client, message):
    try:
        if not message.reply_to_message:
            return await message.edit("📌 ʙᴀʟᴀꜱ ᴘᴇꜱᴀɴ ꜱᴇꜱᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴄᴇᴋ sᴀɴɢᴇ!")

        replied_user = message.reply_to_message.from_user
        nama = replied_user.first_name
        user_id = replied_user.id

        if user_id in DEVS:
            return await message.edit("⛔ DIA SIBUK NGODING, GA ADA WAKTU BUAT SANGE.")

        hasil = f"""
<blockquote><b>ʜᴀsɪʟ ᴄᴇᴋ sᴀɴɢᴇ :</b></blockquote>
<blockquote><b>
ɴᴀᴍᴀ : {nama}
sᴀɴɢᴇ : {random.choice(['90%', '80%', '99%', '70%', '60%', '10%', '0%', '5%', '10%', '20%', '30%', '40%', '5s0%'])}</b></blockquote>
ᴅᴀꜱᴀʀ sᴀɴɢᴇᴀɴ ᴋᴏɴᴛᴏʟ
<blockquote><b>ɴᴇxᴛ ᴄᴇᴋ sɪᴀᴘᴀ ʟᴀɢɪ?</b></blockquote>
"""
        await message.edit(hasil)

    except Exception as e:
        await message.edit(f"❌ Error: {e}")
