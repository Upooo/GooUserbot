import importlib

from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)

from GooUbot import bot, ubot
from GooUbot.config import (
    LOGS_MAKER_UBOT,
)
from GooUbot.core.helpers import PY
from GooUbot.modules import (
    loadModule,
)


HELP_COMMANDS = {}


async def loadPlugins() -> None:

    modules = loadModule()

    for module in modules:

        try:
            imported_module = (
                importlib.import_module(
                    f"GooUbot.modules.{module}"
                )
            )

            module_name = getattr(
                imported_module,
                "__MODULE__",
                "",
            )

            module_name = (
                module_name
                .replace(" ", "_")
                .lower()
            )

            if not module_name:
                continue

            if module_name in HELP_COMMANDS:
                print(
                    "[WARNING] "
                    f"Duplicate module: "
                    f"{module_name}"
                )

            HELP_COMMANDS[
                module_name
            ] = imported_module

            print(
                "[INFO] "
                f"Loaded module: "
                f"{module}"
            )

        except Exception as e:
            print(
                "[ERROR] "
                f"Failed loading "
                f"{module}: {e}"
            )

    print(
        "[INFO] "
        f"{bot.me.full_name} "
        f"loaded "
        f"{len(HELP_COMMANDS)} "
        "modules"
    )

    username = (
        f"@{bot.me.username}"
        if bot.me.username
        else "No Username"
    )

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
                InlineKeyboardButton(
                    "Store",
                    url="https://t.me/n0thinghre",
                ),
                InlineKeyboardButton(
                    "Owner",
                    url="https://t.me/nathanidol",
                ),
            ],
            [
                InlineKeyboardButton(
                    "Userbot",
                    url=(
                        f"https://t.me/"
                        f"{bot.me.username}"
                    )
                    if bot.me.username
                    else "https://t.me",
                )
            ],
        ]
    )

    for chat_id in LOGS_MAKER_UBOT:

        try:
            await bot.send_message(
                chat_id,
                message_text,
                reply_markup=keyboard,
            )

        except Exception as e:
            print(
                "[ERROR] "
                f"Failed sending "
                f"startup log to "
                f"{chat_id}: {e}"
            )


@PY.CALLBACK("0_cls")
async def close_callback(
    client,
    callback_query: CallbackQuery,
) -> None:

    try:
        await callback_query.message.delete()

    except Exception:
        pass


# import importlib
# from platform import python_version

# from pyrogram import __version__
# from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

# from GooUbot import *
# from GooUbot.config import LOGS_MAKER_UBOT
# from GooUbot.modules import loadModule
# from GooUbot.core.helpers import PY

# HELP_COMMANDS = {}

# async def loadPlugins() -> None:
#     modules = loadModule()
#     for mod in modules:
#         imported = importlib.import_module(f"GooUbot.modules.{mod}")
#         module_name = getattr(imported, "__MODULE__", "").replace(" ", "_").lower()
#         if module_name:
#             HELP_COMMANDS[module_name] = imported

#     print(f"[{bot.me.full_name} - PLUGINS BERHASIL DI MUAT")
#     for chat_id in LOGS_MAKER_UBOT:
#         try:
#             await bot.send_message(
#                 chat_id,
#                 f"""<blockquote><b><u>{bot.me.mention} started :</u></b></blockquote>
# <blockquote><b>ID :</b> <code>{bot.me.id}</code>
# <b>Nama :</b> <b>{bot.me.full_name}</b>
# <b>Total Modul :</b> <code>{len(HELP_COMMANDS)}</code>
# <b>Total Pengguna :</b> <code>{len(ubot._ubot)}</code>
# <b>Username :</b> @{bot.me.username}</blockquote>""",
#                 reply_markup=InlineKeyboardMarkup([
#                     [
                        
#                         InlineKeyboardButton("Store", url="https://t.me/gootoko"),
#                         InlineKeyboardButton("Owner", url="https://t.me/goofounder"),
#                     ],
#                     [
#                         InlineKeyboardButton("Userbot", url=f"https://t.me/{bot.me.username}"),
#                     ],
#                 ]),
#             )
#         except Exception as e:
#             print(f"GAGAL KIRIM KE {chat_id} : {e}")

# @PY.CALLBACK("0_cls")
# async def close_callback(client, callback_query: CallbackQuery) -> None:
#     await callback_query.message.delete()
