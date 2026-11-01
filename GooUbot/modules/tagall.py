__MODULE__ = "tagall"
__HELP__ = """
<blockquote><b>Tagall</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}tagall</code> [teks]
Tag anggota grup (5 per pesan, delay aman).</blockquote>

<blockquote><b>Perintah:</b> <code>{0}batal</code>
Batalkan tagall yang sedang jalan.</blockquote>
"""

import asyncio
import random
from random import shuffle

from GooUbot import *

tagallgcid = []

emoji_pool = [
    "😀", "😁", "😂", "🤣", "😊", "😍", "🥰", "😘", "😎", "🥳",
    "🐶", "🐱", "🐰", "🐻", "🐼", "🦁", "🦊", "🦄", "🐸",
    "🍎", "🍕", "🍔", "🍩", "🍦", "🍓", "🍣",
    "🌲", "🌺", "🌞", "🌈", "🌊", "🌻", "🌸",
    "✈️", "🚀", "🚲", "🚗", "⛵",
    "⚽", "🏀", "🎾", "🏈", "🎯", "🏆",
    "🎵", "🎤", "🎧", "🎸",
    "🎉", "🎊", "🎈", "🎁",
    "❤️", "💔", "😢", "😭", "😡",
]


def emoji_random():
    return random.choice(emoji_pool)


@PY.UBOT("tagall")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    if message.chat.id in tagallgcid:
        return await message.reply("Tagall sudah berjalan di chat ini. Pakai <code>.batal</code>")

    tagallgcid.append(message.chat.id)
    text = message.text.split(None, 1)[1] if len(message.command) > 1 else ""

    users = [
        f"<a href=tg://user?id={member.user.id}>{emoji_random()}</a>"
        async for member in message.chat.get_members()
        if not (member.user.is_bot or member.user.is_deleted)
    ]
    shuffle(users)

    m = message.reply_to_message or message
    try:
        for chunk in [users[i : i + 5] for i in range(0, len(users), 5)]:
            if message.chat.id not in tagallgcid:
                break
            await m.reply_text(
                f"{text}\n\n{' '.join(chunk)}".strip(),
                quote=bool(message.reply_to_message),
            )
            await asyncio.sleep(2.5)
    finally:
        if message.chat.id in tagallgcid:
            tagallgcid.remove(message.chat.id)


@PY.UBOT("batal")
@PY.TOP_CMD
@PY.GROUP
async def _(client, message):
    if message.chat.id not in tagallgcid:
        return await message.reply("Tidak ada tagall yang sedang berjalan.")

    try:
        tagallgcid.remove(message.chat.id)
    except ValueError:
        pass
    await message.reply("Tagall dibatalkan.")
