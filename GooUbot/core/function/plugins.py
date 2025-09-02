import importlib
from platform import python_version

from pyrogram import __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

from GooUbot import *
from GooUbot.config import LOGS_MAKER_UBOT
from GooUbot.modules import loadModule
from GooUbot.core.helpers import PY

HELP_COMMANDS = {}

async def loadPlugins() -> None:
    modules = loadModule()
    for mod in modules:
        imported = importlib.import_module(f"GooUbot.modules.{mod}")
        module_name = getattr(imported, "__MODULE__", "").replace(" ", "_").lower()
        if module_name:
            HELP_COMMANDS[module_name] = imported

    print(f"[{bot.me.full_name} - ᴘʟᴜɢɪɴꜱ ʙᴇʀʜᴀꜱɪʟ ᴅɪ ᴍᴜᴀᴛ")
    for chat_id in LOGS_MAKER_UBOT:
        try:
            await bot.send_message(
                chat_id,
                f"""<blockquote><b><u>» {bot.me.mention} sᴛᴀʀᴛᴇᴅ :</u></b>

<b>ɪᴅ :</b> <code>{bot.me.id}</code>
<b>ɴᴀᴍᴇ :</b> <b>{bot.me.full_name}</b>
<b>ᴛᴏᴛᴀʟ ᴍᴏᴅᴜʟᴇs :</b> <code>{len(HELP_COMMANDS)}</code>
<b>ᴛᴏᴛᴀʟ ᴘᴇɴɢɢᴜɴᴀ :</b> <code>{len(ubot._ubot)}</code>
<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{bot.me.username}
</blockquote>""",
                reply_markup=InlineKeyboardMarkup([
                    [
                        
                        InlineKeyboardButton("📦 ꜱᴛᴏʀᴇ", url="https://t.me/+op4OV4pI2Kk4ZGU1"),
                        InlineKeyboardButton("👑 ᴏᴡɴᴇʀ", url="https://t.me/nathanidol"),
                    ],
                    [
                        InlineKeyboardButton("🤖 ᴜsᴇʀʙᴏᴛ", url=f"https://t.me/{bot.me.username}"),
                    ],
                ]),
            )
        except Exception as e:
            print(f"GAGAL KIRIM KE {chat_id} : {e}")

@PY.CALLBACK("0_cls")
async def close_callback(client, callback_query: CallbackQuery) -> None:
    await callback_query.message.delete()
