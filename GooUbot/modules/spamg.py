__MODULE__ = "spam"
__HELP__ = """
<blockquote><b>Spam</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}spam</code> [jumlah] [teks/reply]
<code>{0}setdelay</code> [detik] — delay antar pesan
<code>{0}stopspam</code> — stop spam</blockquote>
"""

import asyncio

from GooUbot import *

spam_progress = []


async def spam_msg(client, message, send):
    delay = await get_vars(client.me.id, "SPAM") or 1
    delay = max(int(delay), 1)
    await asyncio.sleep(delay)
    if message.reply_to_message:
        await send.copy(message.chat.id)
    else:
        await client.send_message(message.chat.id, send)


@PY.UBOT("spam")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if client.me.id in spam_progress:
        return await message.reply(f"{ggl}Spam masih jalan. Pakai <code>.stopspam</code>")

    status = await message.reply(f"{prs}Processing...")
    count, msg = extract_type_and_msg(message)

    try:
        count = int(count)
    except Exception:
        return await status.edit(
            f"{ggl}<code>{message.command[0]} [jumlah] [teks/reply]</code>"
        )

    if count < 1 or count > 100:
        return await status.edit(f"{ggl}Jumlah 1-100.")

    if not msg:
        return await status.edit(
            f"{ggl}<code>{message.command[0]} [jumlah] [teks/reply]</code>"
        )

    spam_progress.append(client.me.id)
    try:
        for _ in range(count):
            if client.me.id not in spam_progress:
                return await status.edit(f"{brhsl}Spam dibatalkan.")
            await spam_msg(client, message, msg)
        await status.edit(f"{brhsl}Spam selesai ({count}x).")
    finally:
        if client.me.id in spam_progress:
            spam_progress.remove(client.me.id)


@PY.UBOT("setdelay")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2 or not message.command[1].isdigit():
        return await message.reply(f"{ggl}<code>{message.command[0]} [detik]</code>")

    delay = max(int(message.command[1]), 1)
    await set_vars(client.me.id, "SPAM", delay)
    await message.reply(f"{brhsl}Delay spam: <code>{delay}</code> detik")


@PY.UBOT("stopspam")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if client.me.id in spam_progress:
        spam_progress.remove(client.me.id)
        await message.reply(f"{brhsl}Spam di-stop.")
    else:
        await message.reply(f"{ggl}Tidak ada spam yang berjalan.")
