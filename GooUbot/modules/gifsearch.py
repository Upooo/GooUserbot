__MODULE__ = "gif"
__HELP__ = """
<blockquote><b>GIF Search</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}gif</code> [query]
Cari GIF random.</blockquote>
"""

import random

from GooUbot import *


@PY.UBOT("gif")
@PY.TOP_CMD
async def gif_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [query]</code>")

    query = message.text.split(None, 1)[1]
    status = await message.reply(f"{prs}Searching...")

    try:
        x = await client.get_inline_bot_results("gif", query)
        if not x.results:
            return await status.edit(f"{ggl}GIF tidak ditemukan.")

        result = x.results[random.randrange(len(x.results))]
        saved = await client.send_inline_bot_result(
            client.me.id, x.query_id, result.id
        )
        saved_msg = await client.get_messages(
            client.me.id, int(saved.updates[1].message.id)
        )
        await client.send_animation(
            message.chat.id,
            saved_msg.animation.file_id,
            reply_to_message_id=message.id,
        )
        await status.delete()
        try:
            await saved_msg.delete()
        except Exception:
            pass
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
