__MODULE__ = "alive"
__HELP__ = """
<blockquote><b>Alive & Help</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}alive</code>
Cek status akun userbot.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}help</code>
Buka menu bantuan.
<code>{0}help [module]</code> untuk detail module tertentu.</blockquote>
"""

import importlib
import os
import re
import sys
from datetime import datetime
from time import time

from pyrogram.raw.functions import Ping
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
)

from GooUbot import *
from GooUbot.config import OWNER_ID
from GooUbot.core.function.plugins import HELP_COMMANDS


@PY.UBOT("alive")
@PY.TOP_CMD
async def _(client, message):
    try:
        x = await client.get_inline_bot_results(
            bot.me.username, f"alive {message.id} {client.me.id}"
        )
        await message.reply_inline_bot_result(x.query_id, x.results[0].id, quote=True)
    except Exception as error:
        await message.reply(f"<code>{error}</code>")


@PY.INLINE("^alive")
async def _(client, inline_query):
    get_id = inline_query.query.split()
    if len(get_id) < 3:
        return

    for my in ubot._ubot:
        if int(get_id[2]) != my.me.id:
            continue

        try:
            peer = my._get_my_peer.get(my.me.id, {})
            users = len(peer.get("pm", []))
            group = len(peer.get("gc", []))
        except Exception:
            try:
                total = await my.get_dialogs_count()
            except Exception:
                total = 0
            users = total
            group = total

        get_exp = await get_expired_date(my.me.id)
        exp = get_exp.strftime("%d-%m-%Y") if get_exp else "-"

        ultra = await get_list_from_vars(client.me.id, "ULTRA_PREM")
        status = "SuperUltra" if my.me.id in ultra else "Premium"

        start = datetime.now()
        try:
            await my.invoke(Ping(ping_id=0))
            ping = round((datetime.now() - start).total_seconds() * 1000, 2)
        except Exception:
            ping = "-"

        uptime = await get_time((time() - start_time))
        psr = await EMO.PASIR(client)

        msg = f"""
<blockquote><b>{bot.me.mention}</b>
ᚗ status: <b>{status}</b>
ᚗ {psr}expired: <code>{exp}</code>
ᚗ dc_id: <code>{my.me.dc_id}</code>
ᚗ ping: <code>{ping} ms</code>
ᚗ peers: <code>{users}</code> users · <code>{group}</code> groups
ᚗ uptime: <code>{uptime}</code></blockquote>
""".strip()

        button = BTN.ALIVE(get_id)
        await client.answer_inline_query(
            inline_query.id,
            cache_time=30,
            results=[
                InlineQueryResultArticle(
                    title="Alive",
                    reply_markup=InlineKeyboardMarkup(button),
                    input_message_content=InputTextMessageContent(msg),
                )
            ],
        )
        break


@PY.CALLBACK("alv_cls")
async def _(client, callback_query):
    get_id = callback_query.data.split()
    if len(get_id) < 3:
        return
    if callback_query.from_user.id != int(get_id[2]):
        return await callback_query.answer("Bukan buat kamu.", show_alert=True)

    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for my in ubot._ubot:
        if callback_query.from_user.id == my.me.id:
            try:
                await my.delete_messages(
                    unPacked.chat_id, [int(get_id[1]), unPacked.message_id]
                )
            except Exception:
                pass
            break


@PY.CALLBACK("reboot")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    admin_users = await get_list_from_vars(client.me.id, "ADMIN_USERS")

    if user_id not in admin_users and user_id != OWNER_ID:
        return await callback_query.answer("Tidak ada akses.", show_alert=True)

    await callback_query.answer("Restarting...", show_alert=True)
    logger.info(f"Restart requested by {user_id}")
    os.execl(sys.executable, sys.executable, "-m", "GooUbot")


@PY.CALLBACK("update")
async def _(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id != OWNER_ID:
        return await callback_query.answer("Owner only.", show_alert=True)

    try:
        import subprocess

        out = subprocess.check_output(["git", "pull"], stderr=subprocess.STDOUT).decode("UTF-8")
    except Exception as e:
        return await callback_query.answer(f"Gagal pull: {e}", show_alert=True)

    if "Already up to date" in out:
        return await callback_query.answer("Sudah versi terbaru.", show_alert=True)

    await callback_query.answer("Updating & restart...", show_alert=True)
    logger.info("Git pull success, restarting...")
    os.execl(sys.executable, sys.executable, "-m", "GooUbot")


@PY.UBOT("help")
async def user_help(client, message):
    arg = get_arg(message)
    if not arg:
        try:
            x = await client.get_inline_bot_results(bot.me.username, "user_help")
            await message.reply_inline_bot_result(x.query_id, x.results[0].id)
        except Exception as error:
            await message.reply(f"<code>{error}</code>")
        return

    module = arg.lower().replace(" ", "_")
    if module in HELP_COMMANDS:
        prefix = await ubot.get_prefix(client.me.id)
        await message.reply(
            HELP_COMMANDS[module].__HELP__.format(next(p for p in prefix)),
            quote=True,
        )
    else:
        await message.reply(f"Module <code>{arg}</code> tidak ditemukan.")


@PY.INLINE("^user_help")
async def user_help_inline(client, inline_query):
    if not HELP_COMMANDS:
        modules = loadModule()
        for mod in modules:
            try:
                imported = importlib.import_module(f"GooUbot.modules.{mod}")
                name = getattr(imported, "__MODULE__", "").replace(" ", "_").lower()
                if name:
                    HELP_COMMANDS[name] = imported
            except Exception:
                continue

    prefixes = await ubot.get_prefix(inline_query.from_user.id)
    msg = f"""
<blockquote><b>Help Menu</b>
User: <a href="tg://user?id={inline_query.from_user.id}">{inline_query.from_user.first_name}</a>
Prefix: <code>{' '.join(prefixes)}</code>
Modules: <code>{len(HELP_COMMANDS)}</code></blockquote>
""".strip()

    results = [
        InlineQueryResultArticle(
            title="Help Menu",
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELP_COMMANDS, "help")
            ),
            input_message_content=InputTextMessageContent(msg),
        )
    ]
    await client.answer_inline_query(inline_query.id, cache_time=30, results=results)


@PY.CALLBACK("^close_user")
async def close_usernya(client, callback_query):
    unPacked = unpackInlineMessage(callback_query.inline_message_id)
    for x in ubot._ubot:
        if callback_query.from_user.id == x.me.id:
            try:
                await x.delete_messages(unPacked.chat_id, unPacked.message_id)
            except Exception:
                pass
            break


@PY.CALLBACK("help_(.*?)")
async def help_callback(client, callback_query):
    data = callback_query.data
    mod_match = re.match(r"help_module\((.+?)\)", data)
    prev_match = re.match(r"help_prev\((.+?)\)", data)
    next_match = re.match(r"help_next\((.+?)\)", data)
    back_match = re.match(r"help_back", data)

    prefixes = await ubot.get_prefix(callback_query.from_user.id)
    top_text = f"""
<blockquote><b>Help Menu</b>
User: <a href="tg://user?id={callback_query.from_user.id}">{callback_query.from_user.first_name}</a>
Prefix: <code>{' '.join(prefixes)}</code>
Modules: <code>{len(HELP_COMMANDS)}</code></blockquote>
""".strip()

    if mod_match:
        module = mod_match.group(1).replace(" ", "_")
        if module not in HELP_COMMANDS:
            return await callback_query.answer("Module tidak ada.", show_alert=True)
        text = HELP_COMMANDS[module].__HELP__.format(next(p for p in prefixes))
        button = [[InlineKeyboardButton("Kembali", callback_data="help_back")]]
        await callback_query.edit_message_text(
            text=text,
            reply_markup=InlineKeyboardMarkup(button),
            disable_web_page_preview=True,
        )
    elif prev_match:
        page = int(prev_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(page - 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    elif next_match:
        page = int(next_match.group(1))
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(page + 1, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
    elif back_match:
        await callback_query.edit_message_text(
            top_text,
            reply_markup=InlineKeyboardMarkup(
                paginate_modules(0, HELP_COMMANDS, "help")
            ),
            disable_web_page_preview=True,
        )
