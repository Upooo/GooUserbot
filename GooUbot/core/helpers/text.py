from GooUbot import (
    bot,
    ubot,
)


class MSG:

    @staticmethod
    def EXP_MSG_UBOT(client):

        full_name = (
            f"{client.me.first_name} "
            f"{client.me.last_name or ''}"
        ).strip()

        return f"""
<blockquote>
<b>⚠️ Masa Aktif Berakhir</b>
</blockquote>

<blockquote>
<b>Nama:</b> <a href="tg://user?id={client.me.id}">{full_name}</a>
<b>ID:</b> <code>{client.me.id}</code>

Masa aktif userbot lu udah habis. 
Kalau masih mau lanjut pakai layanan, silakan perpanjang akses terlebih dahulu.
</blockquote>
""".strip()

    @staticmethod
    def START(message):

        full_name = (
            f"{message.from_user.first_name} "
            f"{message.from_user.last_name or ''}"
        ).strip()

        return f"""
<blockquote>
<b>👋 Halo, <a href="tg://user?id={message.from_user.id}">{full_name}</a></b>
</blockquote>

<blockquote>
Gua <b>{bot.me.mention}</b>, bot multi-client yang bisa bantu lu pasang userbot Telegram dengan lebih cepat dan praktis.

Sebelum mulai, pastiin lu udah baca syarat, risiko, dan kebijakan penggunaan userbot di Telegram. Kalau udah paham dan siap lanjut, tinggal pilih tombol di bawah.
</blockquote>

<blockquote>
<b>Belum punya akses?</b>
Hubungi: @gooteam
</blockquote>
""".strip()

    @staticmethod
    async def UBOT(count):

        count = int(count)

        userbot = ubot._ubot[count]

        full_name = (
            f"{userbot.me.first_name} "
            f"{userbot.me.last_name or ''}"
        ).strip()

        total = len(ubot._ubot)

        return f"""
<blockquote>
<b>📦 Userbot {count + 1}/{total}</b>

<b>Akun:</b>
<a href="tg://user?id={userbot.me.id}">
{full_name}
</a>

<b>ID:</b>
<code>{userbot.me.id}</code>
</blockquote>
""".strip()

    @staticmethod
    def POLICY():

        return """
<blockquote>
<b>📌 Informasi Penggunaan Userbot</b>
</blockquote>

<blockquote>
Banyak yang nanya apakah aman pasang userbot di akun tertentu.

Secara umum, lebih disarankan menggunakan akun yang sudah cukup lama dipakai dan punya aktivitas normal. Akun yang masih baru atau minim aktivitas biasanya lebih sensitif terhadap aktivitas otomatis.

Walaupun begitu, tidak ada jaminan akun benar-benar aman karena semuanya tetap bergantung pada cara penggunaan, intensitas spam, automation, dan perilaku akun masing-masing.
</blockquote>

<blockquote>
<b>Catatan:</b> Gunakan secara wajar dan pahami risikonya sebelum memakai userbot.
</blockquote>
""".strip()

# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# from GooUbot import *


# class MSG:     
#     def EXP_MSG_UBOT(X):
#         return f"""
# <b><blockquote>Notif Expired!</b>
# <b>Nama :</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
# <b>Id :</b> <code>{X.me.id} </code>
# <b>Pesan : Masa aktif lu udah abis cuy.</blockquote></b>
# """

#     def START(message):
#         return f"""
# <b><blockquote>👋🏻 Hey, <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>❕</blockquote>
# <blockquote>Gua {bot.me.mention}, sebuah bot multi client yang bisa bantuin lu buat masang userbot di akun telegram lu dengan mudah dan cepat, gua siap jadi asisten pribadi lu.

# Sebelum lu pasang, lu harus baca Syarat dan Kententuan telegram dulu tentang resiko penggunaan userbot. Kalo lu udah baca dan pengen lanjutin masang, tinggal pilih tombol di bawah.</blockquote>
# <blockquote>Belum ada akses? Beli di : @gooteam</blockquote></b>"""

#     async def UBOT(count):
#         return f"""
# <blockquote><b>⌬ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
# <b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
# <b> ╰ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
# """

#     def POLICY():
#         return """
# <blockquote><b>ʙᴜᴀᴛ ʏᴀɴɢ ɴᴀɴʏᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴀᴍᴀɴ ʙᴜᴀᴛ ᴅɪ ᴘᴀsᴀɴɢ ᴅɪ ᴀᴋᴜɴ ɪᴅ ᴀᴡᴀʟᴀɴ ʙᴇʀᴀᴘᴀ ʏᴀ??</b></blockquote>
# <blockquote><b>ɢɪɴɪ ᴜɴᴛᴜᴋ ᴘᴇɴɢɢᴜɴᴀ ᴜsᴇʀʙᴏᴛ ɪᴛᴜ ᴊᴀɴɢᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴅ ᴀᴡᴀʟᴀɴ 𝟼-𝟽 ᴋᴀʀɴᴀ sᴀɴɢᴀᴛ ʀᴀᴡᴀɴ ᴊɪᴋᴀ ᴅɪ ᴘᴀsᴀɴɢ ᴜsᴇʀʙᴏᴛ.
# ᴜɴᴛᴜᴋ ᴘᴇᴍᴀᴋᴀɪᴀɴ ᴜsᴇʀʙᴏᴛ ʙɪᴀsᴀ ᴅɪ ᴘᴀᴋᴀɪ ᴅɪ ᴀᴋᴜɴ ʟᴀᴍᴀ ᴀᴛᴀᴜ ʙɪᴀsᴀ ɪᴅ ᴀᴡᴀʟᴀɴ 𝟷-𝟻,
# sᴇᴍᴜᴀ ᴘᴇɴɢɢᴜɴᴀ ᴅᴀʀɪ ɪᴅ ᴛᴇʀsᴇʙᴜᴛ sᴜᴅᴀʜ ᴛᴇʀʙɪʟᴀɴɢ ᴀᴍᴀɴ ᴛᴀᴘɪ sᴇᴍᴜᴀ ᴛᴇʀɢᴀɴᴛᴜɴɢ ᴘᴇᴍᴀᴋᴀɪᴀɴ ᴋᴀʟɪᴀɴ.</b></blockquote>
# """
