from GooUbot import *
import random
import requests
from pyrogram.enums import ChatAction, ParseMode
from pyrogram import filters
from pyrogram.types import Message

__MODULE__ = "goo ai"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ goo ai--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}gooai</code> [nama/peristiwa]
🦠 ᴋᴇᴛ : ᴍᴇʀᴀᴍᴀʟ sᴇsᴜᴀᴛᴜ ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ɴᴀᴍᴀ ᴀᴛᴀᴜ ᴘᴇʀɪsᴛɪᴡᴀ ʏᴀɴɢ ᴅɪʙᴇʀɪᴋᴀɴ.</b></blockquote>
"""


@PY.UBOT("gooai")
@PY.TOP_CMD
async def chat_gpt(client, message):
    try:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)

        if len(message.command) < 2:
            await message.reply_text(
                "<emoji id=5019523782004441717>❌</emoji>mohon gunakan format\ncontoh : .gooai namaku alfsefyy"
            )
        else:
            prs = await message.reply_text(f"<emoji id=5192886773948107844>😮‍💨</emoji>Min Goo lagi nyarii...")
            a = message.text.split(' ', 1)[1]
            response = requests.get(f'https://api.siputzx.my.id/api/ai/dukun?content={a}')

            try:
                if "data" in response.json():
                    x = response.json()["data"]                  
                    await prs.edit(
                      f"<blockquote>{x}</blockquote>"
                    )
                else:
                    await message.reply_text("No 'results' key found in the response.")
            except KeyError:
                await message.reply_text("Error accessing the response.")
    except Exception as e:
        await message.reply_text(f"{e}")
