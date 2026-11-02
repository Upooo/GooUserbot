__MODULE__ = "country"
__HELP__ = """
<blockquote><b>Country Info</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}country</code> [nama negara]
Info negara (ibu kota, populasi, dll).</blockquote>
"""

import requests

from GooUbot import *

API_URL = "https://api.siputzx.my.id/api/tools/countryInfo"


@PY.UBOT("country")
@PY.TOP_CMD
async def country_info_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [nama negara]</code>")

    country_name = message.text.split(None, 1)[1]
    status = await message.reply(f"{prs}Mengambil data...")

    try:
        response = requests.get(f"{API_URL}?name={country_name}", timeout=15)
        data = response.json()

        if response.status_code != 200 or not data.get("status"):
            err = data.get("error", "Gagal mengambil data.")
            return await status.edit(f"{ggl}{err}")

        info = data.get("data", {})
        country = info.get("country", country_name)
        capital = info.get("capital", "-")
        region = info.get("region", "-")
        population = f"{info.get('population', 0):,}" if info.get("population") else "-"
        currency = info.get("currency", "-")
        timezone = info.get("timezone", "-")
        calling = info.get("calling_code", "-")

        text = f"""
<blockquote><b>{country}</b>
Ibu kota: {capital}
Wilayah: {region}
Populasi: {population}
Mata uang: {currency}
Timezone: {timezone}
Kode telepon: +{calling}</blockquote>
""".strip()
        await status.edit(text)
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
