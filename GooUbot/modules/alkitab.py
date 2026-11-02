__MODULE__ = "alkitab"
__HELP__ = """
<blockquote><b>Alkitab</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}alkitab</code> [kata kunci]
Cari ayat Alkitab.</blockquote>
"""

import requests
from bs4 import BeautifulSoup

from GooUbot import *


@PY.UBOT("alkitab")
@PY.TOP_CMD
async def search_alkitab(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [kata kunci]</code>\n"
            f"Contoh: <code>{message.command[0]} kejadian</code>"
        )

    query = message.text.split(None, 1)[1]
    status = await message.reply(f"{prs}Mencari...")

    try:
        url = f"https://alkitab.me/search?q={query}"
        headers = {"User-Agent": "Mozilla/5.0"}
        res = requests.get(url, headers=headers, timeout=15)
        soup = BeautifulSoup(res.text, "html.parser")

        results = []
        for div in soup.find_all("div", class_="vw"):
            p_tag = div.find("p")
            a_tag = div.find("a")
            if p_tag and a_tag:
                results.append(
                    f"<b>{a_tag.get_text(strip=True)}</b>\n{p_tag.get_text(strip=True)}"
                )

        if not results:
            return await status.edit(f"{ggl}Tidak ditemukan.")

        caption = "\n\n────────\n\n".join(results[:10])
        await status.edit(f"<blockquote>{caption}</blockquote>")
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")
