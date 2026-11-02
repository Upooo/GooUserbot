__MODULE__ = "fun"
__HELP__ = """
<blockquote><b>Fun (Fake Global)</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}giben</code> — fake global ban
<code>{0}gimut</code> — fake global mute
<code>{0}gikik</code> — fake global kick
<code>{0}gikes</code> — fake global broadcast

Hanya untuk bercanda, tidak ban beneran.</blockquote>
"""

import asyncio
import random

from GooUbot import *
from GooUbot.config import OWNER_ID

nyet = ["50", "350", "97", "670", "24", "909", "57", "89", "153", "877"]
babi = ["2", "3", "6", "7", "9"]


async def _fake_global(client, message, action_name):
    ggl = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)

    if message.from_user and message.from_user.id != client.me.id:
        status = await message.reply(f"{action_name}...")
    else:
        status = await message.edit(f"{action_name}...")

    if not user_id:
        return await status.edit(f"{ggl}Reply user atau kasih username/id.")
    if user_id == client.me.id:
        return await status.edit(f"{ggl}Tidak bisa target diri sendiri.")
    if user_id == OWNER_ID:
        return await status.edit(f"{ggl}Tidak bisa target owner.")

    try:
        user = await client.get_users(user_id)
    except Exception:
        return await status.edit(f"{ggl}User tidak ditemukan.")

    done = random.choice(nyet)
    msg = (
        f"**#{action_name}**\n\n"
        f"**Nama:** [{user.first_name}](tg://user?id={user.id})\n"
        f"**User ID:** `{user.id}`"
    )
    if reason:
        msg += f"\n**Alasan:** `{reason}`"
    msg += f"\n**Sukses di:** `{done}` chat"

    await asyncio.sleep(3)
    await status.edit(msg)


@PY.UBOT("giben")
@PY.TOP_CMD
async def giben(client, message):
    await _fake_global(client, message, "GBanned")


@PY.UBOT("gimut")
@PY.TOP_CMD
async def gimut(client, message):
    await _fake_global(client, message, "GMuted")


@PY.UBOT("gikik")
@PY.TOP_CMD
async def gikik(client, message):
    await _fake_global(client, message, "GKicked")


@PY.UBOT("gikes")
@PY.TOP_CMD
async def gikes_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    if not (message.reply_to_message or get_arg(message)):
        return await message.reply(f"{ggl}Reply atau ketik pesan.")

    status = await message.reply("Broadcasting...")
    done = random.choice(nyet)
    fail = random.choice(babi)
    await asyncio.sleep(3)
    await status.edit(
        f"Terkirim ke `{done}` grup, gagal `{fail}` grup."
    )
