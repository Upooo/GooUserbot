__MODULE__ = "reaction"
__HELP__ = """
<blockquote><b>Reaction</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}react</code> [chat] [emoji]
React ke history chat target.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}stopreact</code>
Stop proses react.</blockquote>
"""

import asyncio

from GooUbot import *

reaction_progress = []


@PY.UBOT("react")
@PY.TOP_CMD
async def react_command(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) != 3:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [chat] [emoji]</code>"
        )

    if client.me.id in reaction_progress:
        return await message.reply(f"{ggl}React masih jalan. Pakai <code>.stopreact</code>")

    reaction_progress.append(client.me.id)
    chat_id = message.command[1]
    emoji = message.command[2]
    status = await message.reply(f"{prs}Reacting...")

    try:
        async for msg in client.get_chat_history(chat_id):
            if client.me.id not in reaction_progress:
                break
            try:
                await client.send_reaction(
                    chat_id=msg.chat.id,
                    message_id=msg.id,
                    emoji=emoji,
                )
            except Exception:
                pass
            await asyncio.sleep(0.6)
        await status.edit(f"{brhsl}React selesai.")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
    finally:
        if client.me.id in reaction_progress:
            reaction_progress.remove(client.me.id)


@PY.UBOT("stopreact")
@PY.TOP_CMD
async def stopreact_command(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if client.me.id in reaction_progress:
        reaction_progress.remove(client.me.id)
        await message.reply(f"{brhsl}React di-stop.")
    else:
        await message.reply(f"{ggl}Tidak ada react yang berjalan.")
