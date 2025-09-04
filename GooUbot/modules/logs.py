__MODULE__ = "logs"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʟᴏɢꜱ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}logs</code> [on/off]
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴀᴋᴛɪꜰᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴᴏɴᴀᴋᴛɪꜰᴋᴀɴ ꜰɪᴛᴜʀ ʟᴏɢꜱ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}pmpermit</code> [on/off]
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴀᴋᴛɪꜰᴋᴀɴ ᴀᴛᴀᴜ ᴍᴇɴᴏɴᴀᴋᴛɪꜰᴋᴀɴ ꜰɪᴛᴜʀ ᴘᴍᴘᴇʀᴍɪᴛ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}ok</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪᴢɪɴᴋᴀɴ sᴇsᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴘᴍ ᴀɴᴅᴀ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}no</code>
🦠 ᴋᴇᴛ : ᴍᴇɴᴏʟᴀᴋ sᴇsᴇᴏʀᴀɴɢ ᴅᴀʀɪ ᴘᴍ ᴀɴᴅᴀ.</blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}setpm</code> [pic/text/limit]
🦠 ᴋᴇᴛ : ᴍᴇɴɢᴀᴛᴜʀ ᴋᴏɴꜰɪɢᴜʀᴀꜱɪ ᴘᴍᴘᴇʀᴍɪᴛ. 
🧩 ᴄᴏɴᴛᴏʜ: <code>{0}setpm limit 5</code></blockquote>
<blockquote>
🔗 <b>ᴄᴏɴᴛᴏʜ ᴘᴇɴɢɢᴜɴᴀᴀɴ ʙᴜᴛᴛᴏɴ :</b> <a href='https://t.me/'>ᴛᴜᴛᴏʀɪᴀʟ</a>  
🖼️ <b>ᴄᴏɴᴛᴏʜ ᴘᴇɴɢɢᴜɴᴀᴀɴ ɢᴀᴍʙᴀʀ :</b> <a href='https://t.me/'>ᴛᴜᴛᴏʀɪᴀʟ</a>
</blockquote>
"""

import wget
import pytz
import os

from gc import get_objects
from pyrogram.errors.exceptions.not_acceptable_406 import UserRestricted
from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InputTextMessageContent, 
                            InlineKeyboardMarkup, ChatPrivileges, InlineQueryResultVideo)
from datetime import datetime
from pyrogram.enums import ChatType

from GooUbot import (
    PY, ubot, bot, EMO,
    get_vars, set_vars, get_pm_id, add_pm_id, remove_pm_id
)
from GooUbot.config import DEVS

FLOOD = {}
MSG_ID = {}

PM_TEXT = """
<blockquote>🙋🏻‍♂halo {mention} ada yang bisa saya bantu?

perkenalkan saya adalah pm-security disini
silahkan tunggu majikan saya membalas pesan mu ini ya
jangan spam ya atau anda akan di blokir secara otomatis

⚠peringatan: {warn} hati-hati</blockquote>
"""


@PY.NO_CMD_UBOT("PMPERMIT", ubot)
async def _(client, message):
    DEVS = [1825618929, 1831850761]
    user = message.from_user
    if user.id in DEVS:
        return
    pm_on = await get_vars(client.me.id, "PMPERMIT")
    if pm_on:
        if user.id in MSG_ID:
            await delete_old_message(message, MSG_ID.get(user.id, 0))
        check = await get_pm_id(client.me.id)
        if user.id not in check:
            if user.id in FLOOD:
                FLOOD[user.id] += 1
            else:
                FLOOD[user.id] = 1
            pm_limit = await get_vars(client.me.id, "PM_LIMIT") or "5"
            try:
                if FLOOD[user.id] > int(pm_limit):
                    del FLOOD[user.id]
                    await message.reply(
                        "sudah diingatkan jangan spam, sekarang Anda diblokir."
                    )
                    return await client.block_user(user.id)
            except ValueError:
                await set_vars(client.me.id, "PM_LIMIT", "5")
            pm_msg = await get_vars(client.me.id, "PM_TEXT") or PM_TEXT
            if "~>" in pm_msg:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"pm_pr {id(message)} {FLOOD[user.id]}"
                )
                msg = await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=message.id,
                )
                MSG_ID[user.id] = int(msg.updates[0].id)
            else:
                try:
                    pm_pic = await get_vars(client.me.id, "PM_PIC")
                    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
                    peringatan = f"{FLOOD[user.id]} / {pm_limit}"
                    if pm_pic:
                        try:
                            msg = await message.reply_photo(
                                pm_pic, caption=pm_msg.format(mention=rpk, warn=peringatan)
                            )
                        except ValueError:
                            await set_vars(client.me.id, "PM_PIC", "https://telegra.ph//file/be22060c145c058bf4558.jpg")
                    else:
                        msg = await message.reply(
                            pm_msg.format(mention=rpk, warn=peringatan)
                        )
                    MSG_ID[user.id] = msg.id
                except UnboundLocalError:
                    pass

@PY.UBOT("setpm")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 3:
        return await message.reply(
            f"{ggl}{message.text.split()[0]} [query] [value]"
        )
    query = {"limit": "PM_LIMIT", "text": "PM_TEXT", "pic": "PM_PIC"}
    if message.command[1].lower() not in query:
        return await message.reply(f"{ggl}query yang di masukkan tidak valid")
    query_str, value_str = (
        message.text.split(None, 2)[1],
        message.text.split(None, 2)[2],
    )
    value = query[query_str]
    if value_str.lower() == "none":
        value_str = False
    await set_vars(client.me.id, value, value_str)
    return await message.reply(
        f"{brhsl}pmpermit berhasil disetting"
    )


@PY.UBOT("pmpermit")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}{message.text.split()[0]} [on/off]"
        )

    toggle_options = {"off": False, "on": True}
    toggle_option = message.command[1].lower()

    if toggle_option not in toggle_options:
        return await message.reply(f"{ggl}opsi tidak valid. Harap gunakan 'on' atau 'off'.")

    value = toggle_options[toggle_option]
    text = "diaktifkan" if value else "dinonaktifkan"

    await set_vars(client.me.id, "PMPERMIT", value)
    await message.reply(f"{brhsl}pmpermit berhasil {text}")


@PY.INLINE("pm_pr")
async def _(client, inline_query):
    get_id = inline_query.query.split()
    m = [obj for obj in get_objects() if id(obj) == int(get_id[1])][0]
    pm_msg = await get_vars(m._client.me.id, "PM_TEXT") or PM_TEXT
    pm_limit = await get_vars(m._client.me.id, "PM_LIMIT") or 5
    pm_pic = await get_vars(m._client.me.id, "PM_PIC")
    rpk = f"[{m.from_user.first_name} {m.from_user.last_name or ''}](tg://user?id={m.from_user.id})"
    peringatan = f"{int(get_id[2])} / {pm_limit}"
    buttons, text = await pmpermit_button(pm_msg)
    if pm_pic:
        photo_video = InlineQueryResultVideo if pm_pic.endswith(".mp4") else InlineQueryResultPhoto
        photo_video_url = {"video_url": pm_pic, "thumb_url": pm_pic} if pm_pic.endswith(".mp4") else {"photo_url": pm_pic}
        hasil = [
            photo_video(
                **photo_video_url,
                title="Dapatkan tombol!",
                caption=text.format(mention=rpk, warn=peringatan),
                reply_markup=buttons,
            )
        ]
    else:
        hasil = [
            (
                InlineQueryResultArticle(
                    title="Dapatkan tombol!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text.format(mention=rpk, warn=peringatan)),
                )
            )
        ]
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=hasil,
    )


@PY.UBOT("ok|terima")
@PY.TOP_CMD
@PY.PRIVATE
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await add_pm_id(client.me.id, user.id)
        return await message.reply(f"{brhsl}baiklah, {rpk} telah diterima")
    else:
        return await message.reply(f"{brhsl}{rpk} sudah diterima")


@PY.UBOT("no|tolak")
@PY.TOP_CMD
@PY.PRIVATE
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await message.reply(f"{ggl}🙏🏻 maaf ⁣{rpk} anda telah diblokir")
        return await client.block_user(user.id)
    else:
        await remove_pm_id(client.me.id, user.id)
        return await message.reply(
            f"{ggl}🙏🏻 maaf {rpk} anda telah ditolak untuk menghubungi akun ini lagi"
        )

async def pmpermit_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    for X in m.split("~>", 1)[1].split():
        X_parts = X.split(":", 1)
        keyboard.append(InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1]))
    buttons.add(*keyboard)
    text = m.split("~>", 1)[0]

    return buttons, text


async def delete_old_message(message, msg_id):
    try:
        await message._client.delete_messages(message.chat.id, msg_id)
    except:
        pass


async def send_log(client, chat_id, message, message_text, msg):
    try:
        await client.send_message(chat_id, message_text, disable_web_page_preview=True)
        await message.forward(chat_id)
    except Exception as error:
        print(f"{msg} ERROR: GAGAL MENERUSKAN PESAN")


@PY.UBOT("logs")
@PY.TOP_CMD
async def logs_toggle(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl} Gunakan: <code>{message.text.split()[0]} [on/off]</code>")

    query = {"on": True, "off": False}
    command = message.command[1].lower()

    if command not in query:
        return await message.reply(f"{ggl} Opsi tidak valid! Gunakan: on / off")

    value = query[command]

    if value:
        log_group_id = await get_vars(client.me.id, "LOG_CHANNEL_ID")
        if not log_group_id:
            try:
                me = await client.get_me()
                created = await client.create_supergroup(
                    title=f"ʟᴏɢꜱ {bot.me.full_name}",
                    description="Jangan keluar/hapus grup log ini, Powered by: @nathanidol"
                )
                group_id = created.id

                await client.add_chat_members(group_id, f"{bot.me.username}")
                await client.promote_chat_member(
                    chat_id=group_id,
                    user_id=f"{bot.me.username}",
                    privileges=ChatPrivileges(
                        can_manage_chat=True,
                        can_post_messages=True,
                        can_edit_messages=True,
                        can_delete_messages=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_change_info=True
                    )
                )
                await set_vars(client.me.id, "LOG_CHANNEL_ID", group_id)

            except Exception as e:
                await message.reply(f"{ggl} Gagal membuat grup log :\n<code>{e}</code>")

    await set_vars(client.me.id, "ON_LOGS", value)
    return await message.reply(f"{brhsl} Logs berhasil diatur ke: <b>{'Aktif' if value else 'Nonaktif'}</b>")

@PY.UBOT("setlogs")
@PY.TOP_CMD
async def set_logs_group(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}Gunakan: <code>{message.text.split()[0]} [chat_id]</code>")

    try:
        chat_id = int(message.command[1])
        me = await client.get_me()
        member = await client.get_chat_member(chat_id, me.id)

        await set_vars(client.me.id, "LOG_CHANNEL_ID", chat_id)
        await message.reply(f"{brhsl}Berhasil mengatur grup logs ke: <code>{chat_id}</code>")
    except Exception as e:
        await message.reply(f"{ggl}Gagal mengatur grup logs:\n<code>{e}</code>")


async def send_log(client, message, is_dm=False):
    log_channel_id = await get_vars(client.me.id, "LOG_CHANNEL_ID")
    if not log_channel_id:
        return

    user = message.from_user
    zona = pytz.timezone("Asia/Jakarta")
    waktu = datetime.now(zona).strftime("%Y-%m-%d %H:%M:%S")
    msg_type = "text" if not message.media else str(message.media)
    user_name = f"{user.first_name} {user.last_name or ''}" if user else "Tidak diketahui"

    msg_text = message.text or ""
    chat_title = message.chat.title if message.chat else "Unknown Chat"

    if is_dm:
        log_text = f"""
<blockquote><b><u>📨 ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ᴘʀɪᴠᴀᴛᴇ</u></b></blockquote>

<blockquote><b>• ғʀᴏᴍ :</b> {user_name}
<b>• ᴜsᴇʀ ɪᴅ :</b> {user.id}</blockquote>
<blockquote><b>• ᴍᴇssᴀɢᴇ :</b> {msg_text}
<b>• ᴛʏᴘᴇ :</b> {msg_type}</blockquote>

<blockquote><b>• ᴅᴀᴛᴇ :</b> {waktu}</blockquote>
"""
        buttons = [[InlineKeyboardButton("📩 ᴏᴘᴇɴ ᴍᴇssᴀɢᴇ", url=f"tg://openmessage?user_id={user.id}&message_id={message.id}")]]
    else:
        log_text = f"""
<blockquote><b><u>📨 ɴᴏᴛɪғɪᴄᴀᴛɪᴏɴ ɢʀᴏᴜᴘ</u></b></blockquote>

<blockquote><b>• ɢʀᴏᴜᴘ :</b> {chat_title}
<b>• ɢʀᴏᴜᴘ ɪᴅ :</b> {message.chat.id}</blockquote>
<blockquote><b>• ғʀᴏᴍ :</b> {user_name}
<b>• ᴜsᴇʀ ɪᴅ :</b> {user.id}</blockquote>
<blockquote><b>• ᴍᴇssᴀɢᴇ :</b> {msg_text}
<b>• ᴛʏᴘᴇ : {msg_type}</b></blockquote>

<blockquote><b>• ᴅᴀᴛᴇ : {waktu}</b></blockquote>
"""
        msg_link = message.link if hasattr(message, "link") else None
        buttons = [[InlineKeyboardButton("📩 ᴏᴘᴇɴ ᴍᴇssᴀɢᴇ", url=msg_link)]] if msg_link else []

    try:
        if message.media:
            media_path = await client.download_media(message)
            send_kwargs = {
                "chat_id": int(log_channel_id),
                "caption": log_text.strip(),
                "reply_markup": InlineKeyboardMarkup(buttons)
            }

            if message.photo:
                await bot.send_photo(**send_kwargs, photo=media_path)
            elif message.video:
                await bot.send_video(**send_kwargs, video=media_path)
            elif message.audio:
                await bot.send_audio(**send_kwargs, audio=media_path)
            elif message.voice:
                await bot.send_voice(**send_kwargs, voice=media_path)
            elif message.sticker:
                await bot.send_sticker(int(log_channel_id),reply_markup=InlineKeyboardMarkup(buttons), sticker=media_path)
            else:
                await bot.send_document(**send_kwargs, document=media_path)

            os.remove(media_path)
        else:
            await bot.send_message(
                int(log_channel_id), log_text.strip(), reply_markup=InlineKeyboardMarkup(buttons)
            )
    except Exception as e:
        print("❌ Gagal kirim log:", e)


@PY.NO_CMD_UBOT("LOGS_GROUP", ubot)
async def logs_group(client, message):
    on_logs = await get_vars(client.me.id, "ON_LOGS")
    if not on_logs:
        return

    me = await client.get_me()
    is_dm = message.chat.type == ChatType.PRIVATE
    is_mention = (
        message.reply_to_message and
        message.reply_to_message.from_user and
        message.reply_to_message.from_user.id == me.id
    ) or (
        f"@{me.username}".lower() in (message.text or "").lower()
    )

    if not is_dm and not is_mention:
        return

    await send_log(client, message, is_dm=is_dm)

@PY.NO_CMD_UBOT("LOGS_PRIVATE", ubot)
async def logs_private(client, message):
    if message.chat.type != ChatType.PRIVATE:
        return

    on_logs = await get_vars(client.me.id, "ON_LOGS")
    if not on_logs:
        return

    await send_log(client, message, is_dm=True)

