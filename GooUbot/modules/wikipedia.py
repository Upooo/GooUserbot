__MODULE__ = "wiki"
__HELP__ = """
<blockquote><b>Wikipedia</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}wiki</code> [topik]
Cari ringkasan Wikipedia (ID).</blockquote>
"""

import aiohttp
from bs4 import BeautifulSoup

from GooUbot import *


async def wikipedia(query):
    try:
        url = f"https://id.wikipedia.org/wiki/{query.replace(' ', '_')}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=20) as response:
                if response.status != 200:
                    return {"status": response.status}
                html = await response.text()
                soup = BeautifulSoup(html, "html.parser")
                title = soup.find(id="firstHeading").get_text().strip()
                paragraphs = soup.select("#mw-content-text .mw-parser-output > p")
                content = "\n".join(
                    p.get_text().strip() for p in paragraphs if p.get_text().strip()
                )
                return {"status": 200, "judul": title, "isi": content}
    except Exception as e:
        return {"status": 500, "error": str(e)}


@PY.UBOT("wiki|wikipedia")
@PY.TOP_CMD
async def wiki_handler(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [topik]</code>")

    query = message.text.split(None, 1)[1]
    status = await message.reply(f"{prs}Mencari...")

    res = await wikipedia(query)
    if res.get("status") != 200:
        return await status.edit(f"{ggl}Tidak ditemukan.")

    caption = f"<b>{res['judul']}</b>\n\n{res['isi']}"
    if len(caption) > 3500:
        caption = caption[:3500] + "..."

    await status.edit(caption, disable_web_page_preview=True)
