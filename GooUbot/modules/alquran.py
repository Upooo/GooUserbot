__MODULE__ = "alquran"
__HELP__ = """
<blockquote><b>Al-Qur'an</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}alquran</code> [surah] [ayat]
Contoh: <code>{0}alquran 1 2</code></blockquote>
"""

import aiohttp
from bs4 import BeautifulSoup

from GooUbot import *


async def fetch_quran(surah, ayat):
    url = f"https://kalam.sindonews.com/ayat/{ayat}/{surah}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, timeout=20) as res:
            if res.status != 200:
                raise Exception("Ayat tidak ditemukan.")
            text = await res.text()
            soup = BeautifulSoup(text, "html.parser")
            content = soup.select_one(
                "body > main > div > div.content.clearfix > div.news > section > div.list-content.clearfix"
            )
            if not content:
                raise Exception("Gagal parse halaman.")

            surah_name = content.select_one("div.ayat-title > h1").get_text(strip=True)
            arab = content.select_one("div.ayat-detail > div.ayat-arab").get_text(strip=True)
            latin = content.select_one("div.ayat-detail > div.ayat-latin").get_text(strip=True)
            terjemahan = content.select_one(
                "div.ayat-detail > div.ayat-detail-text"
            ).get_text(strip=True)
            audio = f"https://raw.githubusercontent.com/AyGemuy/quran-json/main/Audio/{surah:03}/{ayat:03}.mp3"

            return {
                "surah": surah_name,
                "arab": arab,
                "latin": latin,
                "terjemahan": terjemahan,
                "audio": audio,
            }


@PY.UBOT("alquran")
@PY.TOP_CMD
async def send_quran(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 3:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [surah] [ayat]</code>\n"
            f"Contoh: <code>{message.command[0]} 1 2</code>"
        )

    if not message.command[1].isdigit() or not message.command[2].isdigit():
        return await message.reply(f"{ggl}Surah dan ayat harus angka.")

    surah = int(message.command[1])
    ayat = int(message.command[2])
    status = await message.reply(f"{prs}Mengambil ayat...")

    try:
        result = await fetch_quran(surah, ayat)
        text = f"""
<blockquote>{result['arab']}

<b>{result['latin']}</b>

Arti: {result['terjemahan']}

({result['surah']})</blockquote>
""".strip()
        await status.edit(text)
        await client.send_audio(
            chat_id=message.chat.id,
            audio=result["audio"],
            caption=f"({result['surah']})",
            title="Quran Audio",
            file_name="quran.mp3",
            reply_to_message_id=message.id,
        )
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
