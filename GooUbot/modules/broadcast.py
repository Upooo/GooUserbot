__MODULE__ = "bc"
__HELP__ = """
<blockquote><b>Broadcast</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}bc</code> [all/pc/gc] [teks/reply]
Kirim siaran ke peer sesuai type.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}stopg</code>
Stop broadcast yang sedang jalan.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}cfd</code> [all/pc/gc] (reply)
Forward siaran.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}send</code> [chat] [teks/reply]
Kirim pesan ke target tertentu.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}autobc</code> [on/off/text/delay/list/remove/limit]
Broadcast otomatis berulang.</blockquote>
"""

import asyncio
import random
from gc import get_objects

from pyrogram.enums import ChatType
from pyrogram.errors import FloodWait
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

from GooUbot import *
from GooUbot.config import BLACKLIST_CHAT
from .limit import limit_cmd

gcast_progress = []
AG = []
LT = []

# Minimal delay antar chat biar lebih aman dari flood
SAFE_DELAY = 0.8


@PY.UBOT("bc|gks")
@PY.IDOL("cbc|cgks")
@PY.TOP_CMD
async def gcast_handler(client, message):
    if client.me.id in gcast_progress:
        return await message.reply("Broadcast masih berjalan. Pakai <code>.stopg</code>")

    gcast_progress.append(client.me.id)

    prs = await EMO.PROSES(client)
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)

    status = await message.reply(f"{prs}Processing...")
    command, text = extract_type_and_msg(message)

    if command not in ("gc", "pc", "all") or not text:
        gcast_progress.remove(client.me.id)
        return await status.edit(
            f"{ggl}<code>{message.command[0]} [all/pc/gc] [teks/reply]</code>"
        )

    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID") or []

    done = failed = 0
    for chat_id in chats:
        if client.me.id not in gcast_progress:
            await status.edit(f"{sks}Broadcast dibatalkan.")
            return

        if chat_id in blacklist or chat_id in (BLACKLIST_CHAT or []):
            continue

        try:
            if message.reply_to_message:
                await text.copy(chat_id)
            else:
                await client.send_message(chat_id, text)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                if message.reply_to_message:
                    await text.copy(chat_id)
                else:
                    await client.send_message(chat_id, text)
                done += 1
            except Exception:
                failed += 1
        except (Exception, ChannelPrivate):
            failed += 1

        await asyncio.sleep(SAFE_DELAY)

    if client.me.id in gcast_progress:
        gcast_progress.remove(client.me.id)

    await status.edit(
        f"<blockquote>{bcs}<b>Broadcast selesai</b>\n"
        f"{sks}Berhasil: <code>{done}</code>\n"
        f"{ggl}Gagal: <code>{failed}</code>\n"
        f"Type: <code>{command}</code></blockquote>"
    )


@PY.UBOT("stopg")
@PY.IDOL("cstopg")
@PY.TOP_CMD
async def stopg_handler(client, message):
    sks = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if client.me.id in gcast_progress:
        gcast_progress.remove(client.me.id)
        return await message.reply(f"{sks}Broadcast di-stop.")
    return await message.reply(f"{ggl}Tidak ada broadcast yang berjalan.")


@PY.UBOT("bcfd|cfd")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    bcs = await EMO.BROADCAST(client)

    status = await message.reply(f"{prs}Processing...")
    command, text = extract_type_and_msg(message)

    if command not in ("gc", "pc", "all") or not message.reply_to_message:
        return await status.edit(
            f"{ggl}<code>{message.command[0]} [all/pc/gc]</code> + reply"
        )

    chats = await get_data_id(client, command)
    blacklist = await get_list_from_vars(client.me.id, "BL_ID") or []

    done = failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in (BLACKLIST_CHAT or []):
            continue
        try:
            await message.reply_to_message.forward(chat_id)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                await message.reply_to_message.forward(chat_id)
                done += 1
            except Exception:
                failed += 1
        except Exception:
            failed += 1
        await asyncio.sleep(SAFE_DELAY)

    await status.edit(
        f"<blockquote>{bcs}<b>Forward selesai</b>\n"
        f"{brhsl}Berhasil: <code>{done}</code>\n"
        f"{ggl}Gagal: <code>{failed}</code></blockquote>"
    )


@PY.BOT("broadcast|bacot|bcast|bc|cfd")
@PY.ADMIN
async def _(client, message):
    status = await message.reply("Processing broadcast...", quote=True)
    send = get_message(message)
    if not send:
        return await status.edit("Balas atau ketik pesan dulu.")

    users = await get_list_from_vars(client.me.id, "SAVED_USERS") or []
    done = 0
    for chat_id in users:
        try:
            if message.reply_to_message:
                await send.forward(chat_id)
            else:
                await client.send_message(chat_id, send)
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            try:
                if message.reply_to_message:
                    await send.forward(chat_id)
                else:
                    await client.send_message(chat_id, send)
                done += 1
            except Exception:
                pass
        except Exception:
            pass
        await asyncio.sleep(SAFE_DELAY)

    await status.edit(f"Broadcast terkirim ke <code>{done}</code> user.")


@PY.UBOT("send")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)

    if message.reply_to_message:
        chat_id = message.chat.id if len(message.command) < 2 else message.command[1]
        try:
            if client.me.id != bot.me.id and message.reply_to_message.reply_markup:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"get_send {id(message)}"
                )
                return await client.send_inline_bot_result(
                    chat_id, x.query_id, x.results[0].id
                )
            return await message.reply_to_message.copy(chat_id)
        except Exception as e:
            return await message.reply(f"{ggl}<code>{e}</code>")

    if len(message.command) < 3:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [chat] [teks]</code>"
        )

    chat_id, chat_text = message.text.split(None, 2)[1:]
    try:
        if "_" in chat_id:
            msg_id, to_chat = chat_id.split("_")
            return await client.send_message(
                to_chat, chat_text, reply_to_message_id=int(msg_id)
            )
        return await client.send_message(chat_id, chat_text)
    except Exception as e:
        return await message.reply(f"{ggl}<code>{e}</code>")


@PY.INLINE("^get_send")
async def _(client, inline_query):
    try:
        _id = int(inline_query.query.split()[1])
    except (IndexError, ValueError):
        return

    m = next((obj for obj in get_objects() if id(obj) == _id), None)
    if not m or not m.reply_to_message:
        return

    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            InlineQueryResultArticle(
                title="Send",
                reply_markup=m.reply_to_message.reply_markup,
                input_message_content=InputTextMessageContent(
                    m.reply_to_message.text or ""
                ),
            )
        ],
    )


@PY.UBOT("autobc")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    bcs = await EMO.BROADCAST(client)
    mng = await EMO.MENUNGGU(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...")
    type_, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type_ == "on":
        if not auto_text_vars:
            return await status.edit(f"{ggl}Set text dulu: <code>.autobc text - pesan</code>")

        if client.me.id in AG:
            return await status.delete()

        AG.append(client.me.id)
        await status.edit(f"{brhsl}Auto broadcast aktif.")

        done = 0
        while client.me.id in AG:
            delay = int(await get_vars(client.me.id, "DELAY_GCAST") or 1)
            delay = max(delay, 1)
            blacklist = await get_list_from_vars(client.me.id, "BL_ID") or []
            txt = random.choice(auto_text_vars)

            group = 0
            async for dialog in client.get_dialogs():
                if client.me.id not in AG:
                    break
                if dialog.chat.type not in (ChatType.GROUP, ChatType.SUPERGROUP):
                    continue
                if dialog.chat.id in blacklist or dialog.chat.id in (BLACKLIST_CHAT or []):
                    continue
                try:
                    await client.send_message(dialog.chat.id, txt)
                    group += 1
                except FloodWait as e:
                    await asyncio.sleep(e.value)
                    try:
                        await client.send_message(dialog.chat.id, txt)
                        group += 1
                    except Exception:
                        pass
                except Exception:
                    pass
                await asyncio.sleep(SAFE_DELAY)

            if client.me.id not in AG:
                return

            done += 1
            await message.reply(
                f"{bcs}Auto BC putaran {done}\n"
                f"{brhsl}Sukses {group} grup\n"
                f"{mng}Tunggu {delay} menit",
                quote=True,
            )
            await asyncio.sleep(60 * delay)

    elif type_ == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await status.edit(f"{brhsl}Auto broadcast off.")
        return await status.delete()

    elif type_ == "text":
        if not value:
            return await status.edit(f"{ggl}<code>.autobc text - pesan</code>")
        await add_auto_text(client, value)
        return await status.edit(f"{brhsl}Text disimpan.")

    elif type_ == "delay":
        try:
            minutes = int(value)
            if minutes < 1:
                raise ValueError
        except (TypeError, ValueError):
            return await status.edit(f"{ggl}<code>.autobc delay - [menit]</code>")
        await set_vars(client.me.id, "DELAY_GCAST", minutes)
        return await status.edit(f"{brhsl}Delay: {minutes} menit")

    elif type_ == "remove":
        if not value:
            return await status.edit(f"{ggl}<code>.autobc remove - [angka/all]</code>")
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await status.edit(f"{brhsl}Semua text dihapus.")
        try:
            idx = int(value) - 1
            auto_text_vars.pop(idx)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await status.edit(f"{brhsl}Text ke-{idx + 1} dihapus.")
        except Exception as e:
            return await status.edit(f"{ggl}<code>{e}</code>")

    elif type_ == "list":
        if not auto_text_vars:
            return await status.edit(f"{ggl}Belum ada text.")
        txt = "<b>Daftar auto BC text</b>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}. {x}\n"
        txt += f"\nHapus: <code>.autobc remove [angka/all]</code>"
        return await status.edit(txt)

    elif type_ == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await status.edit(f"{brhsl}Auto cek limit off.")
            return await status.delete()
        if value == "on":
            if client.me.id in LT:
                return await status.delete()
            LT.append(client.me.id)
            await status.edit(f"{brhsl}Auto cek limit on.")
            while client.me.id in LT:
                try:
                    await limit_cmd(client, message)
                except Exception:
                    pass
                await asyncio.sleep(1200)
            return
        return await status.edit(f"{ggl}<code>.autobc limit - on/off</code>")

    else:
        return await status.edit(
            f"{ggl}<code>.autobc [on/off/text/delay/list/remove/limit]</code>"
        )


async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)
