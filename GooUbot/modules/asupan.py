__MODULE__ = "asupan"
__HELP__ = """
<blockquote><b>Asupan</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}asupan</code> — video random
<code>{0}cewek</code> — foto cewek random
<code>{0}cowok</code> — foto cowok random</blockquote>
"""

import random

from pyrogram.enums import MessagesFilter

from GooUbot import *


@PY.UBOT("asupan")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Mencari video...")
    try:
        items = []
        async for msg in client.search_messages("@AsupanNyaSaiki", filter=MessagesFilter.VIDEO):
            items.append(msg)
        if not items:
            return await status.edit(f"{ggl}Tidak ditemukan.")
        await random.choice(items).copy(message.chat.id, reply_to_message_id=message.id)
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("cewek")
@PY.TOP_CMD
async def photo_cewek(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Mencari...")
    try:
        items = []
        async for msg in client.search_messages("@cewekepepmabar", filter=MessagesFilter.PHOTO):
            items.append(msg)
        if not items:
            return await status.edit(f"{ggl}Tidak ditemukan.")
        await random.choice(items).copy(message.chat.id, reply_to_message_id=message.id)
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("cowok")
@PY.TOP_CMD
async def photo_cowok(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    status = await message.reply(f"{prs}Mencari...")
    try:
        items = []
        async for msg in client.search_messages("@cowokepepmabar", filter=MessagesFilter.PHOTO):
            items.append(msg)
        if not items:
            return await status.edit(f"{ggl}Tidak ditemukan.")
        await random.choice(items).copy(message.chat.id, reply_to_message_id=message.id)
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
