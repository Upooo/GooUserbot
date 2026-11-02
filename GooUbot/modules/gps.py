__MODULE__ = "gmaps"
__HELP__ = """
<blockquote><b>GPS / Maps</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}gps</code> [lokasi]
Cari koordinat lokasi via OpenStreetMap.</blockquote>
"""

from geopy.geocoders import Nominatim

from GooUbot import *


@PY.UBOT("gps|maps")
@PY.TOP_CMD
async def gps(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [lokasi]</code>")

    query = message.text.split(None, 1)[1]
    status = await message.reply(f"{prs}Mencari lokasi...")

    try:
        geolocator = Nominatim(user_agent="GooUserbot")
        loc = geolocator.geocode(query)
        if not loc:
            return await status.edit(f"{ggl}Lokasi tidak ditemukan.")

        await message.reply_location(latitude=loc.latitude, longitude=loc.longitude)
        await status.delete()
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
