__MODULE__ = "purge"
__HELP__ = """
<blockquote><b>Purge</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}purge</code>
Hapus pesan dari yang di-reply sampai sekarang.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}del</code>
Hapus pesan yang di-reply.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}purgeme</code> [jumlah]
Hapus pesan milik sendiri (1-999).</blockquote>
"""

import asyncio

from GooUbot import *


@PY.UBOT("del")
@PY.TOP_CMD
async def _(client, message):
    rep = message.reply_to_message
    try:
        await message.delete()
        if rep:
            await rep.delete()
    except Exception:
        pass


@PY.UBOT("purgeme")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [jumlah]</code>")

    arg = message.command[1].strip()
    if not arg.isdigit():
        return await message.reply(f"{ggl}Argumen harus angka.")

    n = int(arg)
    if n < 1 or n > 999:
        return await message.reply(f"{ggl}Range: 1-999")

    chat_id = message.chat.id
    message_ids = [
        m.id
        async for m in client.search_messages(
            chat_id, from_user=message.from_user.id, limit=n
        )
    ]

    if not message_ids:
        return await message.reply(f"{ggl}Tidak ada pesan ditemukan.")

    for i in range(0, len(message_ids), 100):
        chunk = message_ids[i : i + 100]
        try:
            await client.delete_messages(chat_id=chat_id, message_ids=chunk, revoke=True)
        except Exception as e:
            logger.warning(f"purgeme error: {e}")

    done = await message.reply(f"{brhsl}<code>{len(message_ids)}</code> pesan dihapus.")
    await asyncio.sleep(1.5)
    try:
        await done.delete()
    except Exception:
        pass


@PY.UBOT("purge")
@PY.TOP_CMD
async def _(client, message):
    ggl = await EMO.GAGAL(client)
    brhsl = await EMO.BERHASIL(client)

    if not message.reply_to_message:
        return await message.reply(f"{ggl}Reply pesan yang mau dibersihkan dari situ.")

    chat_id = message.chat.id
    start_id = message.reply_to_message.id
    end_id = message.id

    try:
        await message.delete()
    except Exception:
        pass

    message_ids = list(range(start_id, end_id))
    deleted = 0

    for i in range(0, len(message_ids), 100):
        chunk = message_ids[i : i + 100]
        try:
            await client.delete_messages(chat_id=chat_id, message_ids=chunk, revoke=True)
            deleted += len(chunk)
        except Exception as e:
            logger.warning(f"purge error: {e}")

    status = await client.send_message(chat_id, f"{brhsl}<code>{deleted}</code> pesan dibersihkan.")
    await asyncio.sleep(1.5)
    try:
        await status.delete()
    except Exception:
        pass
