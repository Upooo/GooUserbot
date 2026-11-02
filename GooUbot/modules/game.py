__MODULE__ = "game"
__HELP__ = """
<blockquote><b>Game</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}game</code>
Game random dari @gamee.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}catur</code>
Catur via GameFactoryBot.</blockquote>
"""

import random

from GooUbot import *


@PY.UBOT("catur")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    try:
        x = await client.get_inline_bot_results("GameFactoryBot")
        msg = message.reply_to_message or message
        await client.send_inline_bot_result(
            message.chat.id,
            x.query_id,
            x.results[0].id,
            reply_to_message_id=msg.id,
        )
    except Exception as error:
        await message.reply(f"{ggl}<code>{error}</code>")


@PY.UBOT("game")
@PY.TOP_CMD
async def game_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    try:
        x = await client.get_inline_bot_results("gamee")
        if not x.results:
            return await message.reply(f"{ggl}Tidak ada game tersedia.")
        msg = message.reply_to_message or message
        idx = random.randint(0, len(x.results) - 1)
        await client.send_inline_bot_result(
            message.chat.id,
            x.query_id,
            x.results[idx].id,
            reply_to_message_id=msg.id,
        )
    except Exception as error:
        await message.reply(f"{ggl}<code>{error}</code>")
