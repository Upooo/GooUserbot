import importlib

from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from GooUbot import bot, ubot, logger
from GooUbot.config import LOGS_MAKER_UBOT
from GooUbot.core.helpers import PY
from GooUbot.modules import loadModule

HELP_COMMANDS = {}


async def loadPlugins() -> None:
    modules = loadModule()

    for module in modules:
        try:
            imported_module = importlib.import_module(f"GooUbot.modules.{module}")
            module_name = getattr(imported_module, "__MODULE__", "")
            module_name = module_name.replace(" ", "_").lower()

            if not module_name:
                continue

            if module_name in HELP_COMMANDS:
                logger.warning(f"Duplicate module: {module_name}")

            HELP_COMMANDS[module_name] = imported_module
            logger.info(f"Loaded module: {module}")

        except Exception as e:
            logger.error(f"Failed loading {module}: {e}")

    logger.info(f"{bot.me.full_name} loaded {len(HELP_COMMANDS)} modules")

    username = f"@{bot.me.username}" if bot.me.username else "No Username"

    message_text = f"""
<blockquote><b><u>{bot.me.mention} started :</u></b></blockquote>

<blockquote>
<b>ID :</b> <code>{bot.me.id}</code>
<b>Nama :</b> <b>{bot.me.full_name}</b>
<b>Total Modul :</b> <code>{len(HELP_COMMANDS)}</code>
<b>Total Pengguna :</b> <code>{len(ubot._ubot)}</code>
<b>Username :</b> {username}
</blockquote>
"""

    keyboard = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Store", url="https://t.me/n0thinghre"),
                InlineKeyboardButton("Owner", url="https://t.me/nathanidol"),
            ],
            [
                InlineKeyboardButton(
                    "Userbot",
                    url=f"https://t.me/{bot.me.username}" if bot.me.username else "https://t.me",
                )
            ],
        ]
    )

    for chat_id in LOGS_MAKER_UBOT:
        try:
            await bot.send_message(chat_id, message_text, reply_markup=keyboard)
        except Exception as e:
            logger.error(f"Failed sending startup log to {chat_id}: {e}")


@PY.CALLBACK("0_cls")
async def close_callback(client, callback_query: CallbackQuery) -> None:
    try:
        await callback_query.message.delete()
    except Exception:
        pass
