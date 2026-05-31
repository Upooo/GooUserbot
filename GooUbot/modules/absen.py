__MODULE__ = "Absen"

__HELP__ = """
<blockquote><b>📌 Bantuan Menu Absen</b></blockquote>

<blockquote><b>
🚦 Perintah : <code>{0}absen</code>
📝 Keterangan : Memulai sesi absen.
</b></blockquote>

<blockquote><b>
🚦 Perintah : <code>{0}delabsen</code>
📝 Keterangan : Menghapus seluruh daftar absen.
</b></blockquote>
"""

import asyncio
from datetime import datetime

import pytz
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from GooUbot import *

hadir_list = []


# ==========================
# HELPERS
# ==========================

def get_time():
    now = datetime.now(pytz.timezone("Asia/Jakarta"))
    tanggal = now.strftime("%d-%m-%Y")
    jam = now.strftime("%H:%M:%S")
    return tanggal, jam


def is_hadir(user_id):
    return any(user["user_id"] == user_id for user in hadir_list)


def get_hadir_list():
    if not hadir_list:
        return "<blockquote><b>📭 Belum ada peserta yang melakukan absen.</b></blockquote>"

    return "\n".join(
        [
            f"<blockquote><b>👤 {user['mention']}\n🕒 {user['jam']}</b></blockquote>"
            for user in hadir_list
        ]
    )


def build_absen_text():
    tanggal, _ = get_time()

    return f"""
<blockquote><b>📋 Daftar Absen</b></blockquote>

<blockquote><b>
📅 Tanggal : {tanggal}
👥 Total Hadir : {len(hadir_list)}
</b></blockquote>

{get_hadir_list()}
""".strip()


def build_keyboard():
    return InlineKeyboardMarkup(
        [[InlineKeyboardButton("✅ Hadir", callback_data="absen_hadir")]]
    )


# ==========================
# COMMAND
# ==========================

@PY.UBOT("absen")
@PY.TOP_CMD
async def absen_command(c, m):
    ggl = await EMO.GAGAL(c)

    try:
        x = await c.get_inline_bot_results(
            bot.me.username,
            "absen_in"
        )

        if not x.results:
            return await m.reply(
                f"<blockquote><b>{ggl} Tidak ada hasil inline bot.</b></blockquote>"
            )

        await m.reply_inline_bot_result(
            x.query_id,
            x.results[0].id
        )

    except asyncio.TimeoutError:
        await m.reply(
            f"<blockquote><b>{ggl} Timeout saat mengambil inline result.</b></blockquote>"
        )

    except Exception as e:
        await m.reply(
            f"<blockquote><b>{ggl} Terjadi kesalahan:</b>\n<code>{e}</code></blockquote>"
        )


@PY.UBOT("delabsen")
@PY.TOP_CMD
async def clear_absen_command(c, m):
    sks = await EMO.BERHASIL(c)

    hadir_list.clear()

    await m.reply(
        f"<blockquote><b>{sks} Daftar absen berhasil dihapus.</b></blockquote>"
    )


# ==========================
# INLINE
# ==========================

@PY.INLINE("^absen_in")
async def absen_query(c, iq):
    text = build_absen_text()

    await c.answer_inline_query(
        iq.id,
        cache_time=0,
        results=[
            InlineQueryResultArticle(
                title="📋 Absen",
                input_message_content=InputTextMessageContent(text),
                reply_markup=build_keyboard(),
            )
        ],
    )


# ==========================
# CALLBACK
# ==========================

@PY.CALLBACK("absen_hadir")
async def hadir_callback(c, cq):
    user_id = cq.from_user.id

    if is_hadir(user_id):
        return await cq.answer(
            "Lu udah absen sebelumnya.",
            show_alert=True
        )

    _, jam = get_time()

    hadir_list.append(
        {
            "user_id": user_id,
            "mention": cq.from_user.mention,
            "jam": jam,
        }
    )

    await cq.edit_message_text(
        build_absen_text(),
        reply_markup=build_keyboard()
    )

    await cq.answer(
        "Absen berhasil dicatat.",
        show_alert=False
    )


# __MODULE__ = "absen"
# __HELP__ = """
# <blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀʙꜱᴇɴ--</b></blockquote>

# <blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}absen</code>
# 🦠 ᴋᴇᴛ : ᴍᴜʟᴀɪ ᴀʙꜱᴇɴ.</b></blockquote>
# <blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}delabsen</code>
# 🦠 ᴋᴇᴛ : ᴀᴋʜɪʀɪ ᴀʙꜱᴇɴ.</b></blockquote>
# """

# from GooUbot import *
# from pyrogram import Client, filters
# from pyrogram.types import (InlineKeyboardMarkup, InlineQueryResultArticle,                            InputTextMessageContent, InlineKeyboardButton)
# from datetime import datetime
# import pytz

# hadir_list = []

# def get_hadir_list():
#     return "\n".join([f"<blockquote><b>👤 {user['mention']} - {user['jam']}</blockquote></b>" for user in hadir_list])


# @PY.UBOT("absen")
# @PY.TOP_CMD
# async def absen_command(c, m):
#     ggl = await EMO.GAGAL(c)
#     sks = await EMO.BERHASIL(c)
#     prs = await EMO.PROSES(c)
#     user_id = m.from_user.id
#     mention = m.from_user.mention
#     timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
#     jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
#     hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
#     hadir_text = get_hadir_list()
#     try:
#         x = await c.get_inline_bot_results(bot.me.username, "absen_in")
#         if x.results:
#             await m.reply_inline_bot_result(x.query_id, x.results[0].id)
#         else:
#             await m.reply(f"<blockquote><b>{ggl}tidak ada hasil inline bot</b></blockquote>")
#     except asyncio.TimeoutError:
#         await m.reply(f"<blockquote><b>{ggl}waktu habis dalam mendapatkan hasil inline bot</b></blockquote>")
#     except Exception as e:
#         await m.reply(f"<blockquote><b>{ggl}terjadi kesalahan: {e}</b></blockquote>")

# @PY.UBOT("delabsen")
# @PY.TOP_CMD
# async def clear_absen_command(c, m):
#     hadir_list.clear()
#     ggl = await EMO.GAGAL(c)
#     sks = await EMO.BERHASIL(c)
#     prs = await EMO.PROSES(c)
#     await m.reply(f"<blockquote><b>{sks}semua absen berhasil dihapus</b></blockquote>")


# @PY.INLINE("^absen_in")
# async def absen_query(c, iq):
#     user_id = iq.from_user.id
#     mention = iq.from_user.mention
#     timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
#     jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
#     hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
#     hadir_text = get_hadir_list()

#     text = f"<blockquote><b>**absen tanggal:**\n{timestamp}\n\n**list absen:**\n{hadir_text}\n\n</b></blockquote>"
#     buttons = [[InlineKeyboardButton("hadir", callback_data="absen_hadir")]]
#     keyboard = InlineKeyboardMarkup(buttons)
#     await c.answer_inline_query(
#         iq.id,
#         cache_time=0,
#         results=[
#             (
#                 InlineQueryResultArticle(
#                     title="💬",
#                     input_message_content=InputTextMessageContent(text),
#                     reply_markup=keyboard
#                 )
#             )
#         ],
#     )

# @PY.CALLBACK("absen_hadir")
# async def hadir_callback(c, cq):
#     user_id = cq.from_user.id
#     mention = cq.from_user.mention
#     timestamp = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%d-%m-%Y")
#     jam = datetime.now(pytz.timezone('asia/Jakarta')).strftime("%H:%M:%S")
#     if any(user['user_id'] == user_id for user in hadir_list):
#         await cq.answer("anda sudah melakukan absen sebelumnya", show_alert=True)
#     else:
#         hadir_list.append({"user_id": user_id, "mention": mention, "jam": jam})
#         hadir_text = get_hadir_list()
#         text = f"absen tanggal:\n{timestamp}\n\nlist absen:\n{hadir_text}\n\n"
#         buttons = [[InlineKeyboardButton("hadir", callback_data="absen_hadir")]]
#         keyboard = InlineKeyboardMarkup(buttons)
#         await cq.edit_message_text(text, reply_markup=keyboard)
