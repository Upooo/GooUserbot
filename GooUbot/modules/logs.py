__MODULE__ = "logs"
__HELP__ = """
<blockquote><b>Logs & PM Permit</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}logs</code> [on/off]
Aktif/nonaktif fitur log pesan.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}setlogs</code> [chat_id]
Set manual grup log.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}pmpermit</code> [on/off]
Aktif/nonaktif PM security.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}ok</code> / <code>{0}terima</code>
Izinkan seseorang PM.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}no</code> / <code>{0}tolak</code>
Tolak & blokir pengirim PM.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}setpm</code> [limit/text/pic] [value]
Contoh: <code>{0}setpm limit 5</code></blockquote>
"""

import os
import pytz
from datetime import datetime
from gc import get_objects

from pyrogram.enums import ChatType
from pyrogram.types import (
    ChatPrivileges,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InlineQueryResultPhoto,
    InlineQueryResultVideo,
    InputTextMessageContent,
)
from pykeyboard import InlineKeyboard

from GooUbot import (
    PY,
    ubot,
    bot,
    EMO,
    logger,
    get_vars,
    set_vars,
    get_pm_id,
    add_pm_id,
    remove_pm_id,
)
from GooUbot.config import DEVS, OWNER_ID

FLOOD = {}
MSG_ID = {}

PM_TEXT = """
<blockquote>Halo {mention}, ada yang bisa dibantu?

Ini PM Security. Tunggu majikan membalas ya.
Jangan spam — kalau spam akan diblokir otomatis.

Peringatan: {warn}</blockquote>
"""


@PY.NO_CMD_UBOT("PMPERMIT", ubot)
async def _(client, message):
    user = message.from_user
    if not user:
        return

    # Skip owner / devs
    protected = set(DEVS or [])
    protected.add(OWNER_ID)
    protected.add(client.me.id)
    if user.id in protected:
        return

    pm_on = await get_vars(client.me.id, "PMPERMIT")
    if not pm_on:
        return

    if user.id in MSG_ID:
        await delete_old_message(message, MSG_ID.get(user.id, 0))

    allowed = await get_pm_id(client.me.id)
    if user.id in allowed:
        return

    FLOOD[user.id] = FLOOD.get(user.id, 0) + 1
    pm_limit = await get_vars(client.me.id, "PM_LIMIT") or "5"

    try:
        limit = int(pm_limit)
    except (TypeError, ValueError):
        limit = 5
        await set_vars(client.me.id, "PM_LIMIT", "5")

    if FLOOD[user.id] > limit:
        del FLOOD[user.id]
        try:
            await message.reply("Sudah diingatkan jangan spam. Kamu diblokir.")
            await client.block_user(user.id)
        except Exception as e:
            logger.warning(f"PM block failed: {e}")
        return

    pm_msg = await get_vars(client.me.id, "PM_TEXT") or PM_TEXT

    if "~>" in pm_msg:
        try:
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
        except Exception as e:
            logger.warning(f"PM inline failed: {e}")
        return

    try:
        pm_pic = await get_vars(client.me.id, "PM_PIC")
        rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
        peringatan = f"{FLOOD[user.id]} / {limit}"
        caption = pm_msg.format(mention=rpk, warn=peringatan)

        if pm_pic:
            try:
                msg = await message.reply_photo(pm_pic, caption=caption)
            except Exception:
                msg = await message.reply(caption)
        else:
            msg = await message.reply(caption)

        MSG_ID[user.id] = msg.id
    except Exception as e:
        logger.warning(f"PM reply failed: {e}")


@PY.UBOT("setpm")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 3:
        return await message.reply(f"{ggl}<code>{message.command[0]} [limit/text/pic] [value]</code>")

    query = {"limit": "PM_LIMIT", "text": "PM_TEXT", "pic": "PM_PIC"}
    key = message.command[1].lower()

    if key not in query:
        return await message.reply(f"{ggl}Query tidak valid. Pakai: limit / text / pic")

    value_str = message.text.split(None, 2)[2]
    if value_str.lower() == "none":
        value_str = False

    await set_vars(client.me.id, query[key], value_str)
    return await message.reply(f"{brhsl}PM Permit berhasil di-set.")


@PY.UBOT("pmpermit")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [on/off]</code>")

    option = message.command[1].lower()
    if option not in ("on", "off"):
        return await message.reply(f"{ggl}Pakai <code>on</code> atau <code>off</code>.")

    value = option == "on"
    await set_vars(client.me.id, "PMPERMIT", value)
    status = "diaktifkan" if value else "dinonaktifkan"
    await message.reply(f"{brhsl}PM Permit berhasil {status}.")


@PY.INLINE("pm_pr")
async def _(client, inline_query):
    get_id = inline_query.query.split()
    try:
        m = [obj for obj in get_objects() if id(obj) == int(get_id[1])][0]
    except (IndexError, ValueError):
        return

    pm_msg = await get_vars(m._client.me.id, "PM_TEXT") or PM_TEXT
    pm_limit = await get_vars(m._client.me.id, "PM_LIMIT") or 5
    pm_pic = await get_vars(m._client.me.id, "PM_PIC")
    rpk = f"[{m.from_user.first_name} {m.from_user.last_name or ''}](tg://user?id={m.from_user.id})"
    peringatan = f"{int(get_id[2])} / {pm_limit}"
    buttons, text = await pmpermit_button(pm_msg)

    if pm_pic:
        photo_video = InlineQueryResultVideo if str(pm_pic).endswith(".mp4") else InlineQueryResultPhoto
        media_kw = (
            {"video_url": pm_pic, "thumb_url": pm_pic}
            if str(pm_pic).endswith(".mp4")
            else {"photo_url": pm_pic}
        )
        hasil = [
            photo_video(
                **media_kw,
                title="PM Permit",
                caption=text.format(mention=rpk, warn=peringatan),
                reply_markup=buttons,
            )
        ]
    else:
        hasil = [
            InlineQueryResultArticle(
                title="PM Permit",
                reply_markup=buttons,
                input_message_content=InputTextMessageContent(
                    text.format(mention=rpk, warn=peringatan)
                ),
            )
        ]

    await client.answer_inline_query(inline_query.id, cache_time=0, results=hasil)


@PY.UBOT("ok|terima")
@PY.TOP_CMD
@PY.PRIVATE
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    allowed = await get_pm_id(client.me.id)

    if user.id not in allowed:
        await add_pm_id(client.me.id, user.id)
        FLOOD.pop(user.id, None)
        return await message.reply(f"{brhsl}{rpk} diterima.")
    return await message.reply(f"{brhsl}{rpk} sudah diterima sebelumnya.")


@PY.UBOT("no|tolak")
@PY.TOP_CMD
@PY.PRIVATE
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    allowed = await get_pm_id(client.me.id)

    if user.id in allowed:
        await remove_pm_id(client.me.id, user.id)

    try:
        await message.reply(f"{ggl}{rpk} ditolak dan diblokir.")
        await client.block_user(user.id)
    except Exception as e:
        logger.warning(f"Reject PM failed: {e}")


async def pmpermit_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    for part in m.split("~>", 1)[1].split():
        name, url = part.split(":", 1)
        keyboard.append(InlineKeyboardButton(name.replace("_", " "), url=url))
    buttons.add(*keyboard)
    text = m.split("~>", 1)[0]
    return buttons, text


async def delete_old_message(message, msg_id):
    try:
        await message._client.delete_messages(message.chat.id, msg_id)
    except Exception:
        pass


async def send_log(client, message, is_dm=False):
    log_channel_id = await get_vars(client.me.id, "LOG_CHANNEL_ID")
    if not log_channel_id:
        return

    user = message.from_user
    if not user:
        return

    zona = pytz.timezone("Asia/Jakarta")
    waktu = datetime.now(zona).strftime("%Y-%m-%d %H:%M:%S")
    msg_type = "text" if not message.media else str(message.media).split(".")[-1]
    user_name = f"{user.first_name} {user.last_name or ''}".strip()
    msg_text = message.text or message.caption or "-"
    chat_title = getattr(message.chat, "title", None) or "Private"

    if is_dm:
        log_text = f"""
<blockquote><b>Private Message</b></blockquote>
<blockquote><b>From:</b> {user_name}
<b>User ID:</b> <code>{user.id}</code></blockquote>
<blockquote><b>Message:</b> {msg_text}
<b>Type:</b> {msg_type}</blockquote>
<blockquote><b>Time:</b> {waktu}</blockquote>
""".strip()
        buttons = [[InlineKeyboardButton("Open", url=f"tg://openmessage?user_id={user.id}&message_id={message.id}")]]
    else:
        log_text = f"""
<blockquote><b>Group Notification</b></blockquote>
<blockquote><b>Group:</b> {chat_title}
<b>Chat ID:</b> <code>{message.chat.id}</code></blockquote>
<blockquote><b>From:</b> {user_name}
<b>User ID:</b> <code>{user.id}</code></blockquote>
<blockquote><b>Message:</b> {msg_text}
<b>Type:</b> {msg_type}</blockquote>
<blockquote><b>Time:</b> {waktu}</blockquote>
""".strip()
        msg_link = getattr(message, "link", None)
        buttons = [[InlineKeyboardButton("Open", url=msg_link)]] if msg_link else []

    media_path = None
    try:
        if message.media:
            media_path = await client.download_media(message)
            kwargs = {
                "chat_id": int(log_channel_id),
                "caption": log_text,
                "reply_markup": InlineKeyboardMarkup(buttons) if buttons else None,
            }
            if message.photo:
                await bot.send_photo(**kwargs, photo=media_path)
            elif message.video:
                await bot.send_video(**kwargs, video=media_path)
            elif message.audio:
                await bot.send_audio(**kwargs, audio=media_path)
            elif message.voice:
                await bot.send_voice(**kwargs, voice=media_path)
            elif message.sticker:
                await bot.send_sticker(
                    int(log_channel_id),
                    sticker=media_path,
                    reply_markup=InlineKeyboardMarkup(buttons) if buttons else None,
                )
            else:
                await bot.send_document(**kwargs, document=media_path)
        else:
            await bot.send_message(
                int(log_channel_id),
                log_text,
                reply_markup=InlineKeyboardMarkup(buttons) if buttons else None,
                disable_web_page_preview=True,
            )
    except Exception as e:
        logger.error(f"Failed sending log: {e}")
    finally:
        if media_path and os.path.exists(media_path):
            try:
                os.remove(media_path)
            except OSError:
                pass


@PY.UBOT("logs")
@PY.TOP_CMD
async def logs_toggle(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [on/off]</code>")

    command = message.command[1].lower()
    if command not in ("on", "off"):
        return await message.reply(f"{ggl}Pakai <code>on</code> atau <code>off</code>.")

    value = command == "on"

    if value:
        log_group_id = await get_vars(client.me.id, "LOG_CHANNEL_ID")
        if not log_group_id:
            try:
                created = await client.create_supergroup(
                    title=f"Logs • {bot.me.first_name}",
                    description="Grup log otomatis. Jangan keluar/hapus.",
                )
                group_id = created.id
                await client.add_chat_members(group_id, bot.me.username)
                await client.promote_chat_member(
                    chat_id=group_id,
                    user_id=bot.me.id,
                    privileges=ChatPrivileges(
                        can_manage_chat=True,
                        can_post_messages=True,
                        can_edit_messages=True,
                        can_delete_messages=True,
                        can_invite_users=True,
                        can_pin_messages=True,
                        can_change_info=True,
                    ),
                )
                await set_vars(client.me.id, "LOG_CHANNEL_ID", group_id)
            except Exception as e:
                return await message.reply(f"{ggl}Gagal buat grup log:\n<code>{e}</code>")

    await set_vars(client.me.id, "ON_LOGS", value)
    status = "aktif" if value else "nonaktif"
    return await message.reply(f"{brhsl}Logs {status}.")


@PY.UBOT("setlogs")
@PY.TOP_CMD
async def set_logs_group(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [chat_id]</code>")

    try:
        chat_id = int(message.command[1])
        await client.get_chat_member(chat_id, client.me.id)
        await set_vars(client.me.id, "LOG_CHANNEL_ID", chat_id)
        await message.reply(f"{brhsl}Grup logs di-set ke <code>{chat_id}</code>")
    except Exception as e:
        await message.reply(f"{ggl}Gagal set grup logs:\n<code>{e}</code>")


@PY.NO_CMD_UBOT("LOGS_GROUP", ubot)
async def logs_group(client, message):
    if not await get_vars(client.me.id, "ON_LOGS"):
        return

    me = client.me
    is_mention = (
        message.reply_to_message
        and message.reply_to_message.from_user
        and message.reply_to_message.from_user.id == me.id
    ) or (me.username and f"@{me.username}".lower() in (message.text or "").lower())

    if not is_mention:
        return

    await send_log(client, message, is_dm=False)


@PY.NO_CMD_UBOT("LOGS_PRIVATE", ubot)
async def logs_private(client, message):
    if message.chat.type != ChatType.PRIVATE:
        return
    if not await get_vars(client.me.id, "ON_LOGS"):
        return
    await send_log(client, message, is_dm=True)
