__MODULE__ = "done"
__HELP__ = """
<blockquote><b>Done / Receipt</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}done</code> [item], [harga], [pembayaran]
Buat konfirmasi transaksi.
Contoh: <code>{0}done Premium 1bln, 25k, QRIS</code></blockquote>
"""

from datetime import datetime

from GooUbot import *


@PY.UBOT("done")
@PY.TOP_CMD
async def done_command(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    args = message.text.split(None, 1)
    if len(args) < 2 or "," not in args[1]:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} item, harga, pembayaran</code>"
        )

    parts = [p.strip() for p in args[1].split(",", 2)]
    if len(parts) < 2:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} item, harga, pembayaran</code>"
        )

    name_item = parts[0]
    price = parts[1]
    payment = parts[2] if len(parts) > 2 else "-"
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    text = f"""
<blockquote><b>Transaction Success</b>
Barang: {name_item}
Harga: {price}
Waktu: {time}
Payment: {payment}

Terima kasih sudah order.</blockquote>
""".strip()

    status = await message.reply(f"{prs}Processing...")
    await status.edit(text)
