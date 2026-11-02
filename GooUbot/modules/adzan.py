__MODULE__ = "adzan"
__HELP__ = """
<blockquote><b>Adzan</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}adzan</code> [nama kota]
Jadwal shalat wilayah.</blockquote>
"""

import requests

from GooUbot import *


@PY.UBOT("adzan")
@PY.TOP_CMD
async def adzan(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [nama kota]</code>")

    city = message.text.split(None, 1)[1]
    status = await message.reply(f"{prs}Mengambil jadwal...")

    url = f"http://muslimsalat.com/{city}.json?key=bd099c5825cbedb9aa934e255a81a5fc"
    try:
        req = requests.get(url, timeout=15)
        req.raise_for_status()
        result = req.json()
        item = result["items"][0]

        text = f"""
<blockquote><b>Jadwal Shalat • {city}</b>
Tanggal: <code>{item['date_for']}</code>
Wilayah: {result.get('query', city)} | {result.get('country', '-')}

Terbit: <code>{item['shurooq']}</code>
Subuh: <code>{item['fajr']}</code>
Zuhur: <code>{item['dhuhr']}</code>
Ashar: <code>{item['asr']}</code>
Maghrib: <code>{item['maghrib']}</code>
Isya: <code>{item['isha']}</code></blockquote>
""".strip()
        await status.edit(text)
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
