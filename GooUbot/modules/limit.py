__MODULE__ = "limit"
__HELP__ = """
<blockquote><b>Limit Checker</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}limit</code>
Cek apakah akun kena batasan spam / limit dari Telegram.</blockquote>
"""

from asyncio import sleep

from pyrogram.raw.functions.messages import DeleteHistory, StartBot

from GooUbot import *


@PY.UBOT("limit")
@PY.IDOL("climit")
@PY.TOP_CMD
async def limit_cmd(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    msg = await message.reply(f"{prs}Mengecek status limit...")

    try:
        await client.unblock_user("SpamBot")
        bot_info = await client.resolve_peer("SpamBot")
        response = await client.invoke(
            StartBot(
                bot=bot_info,
                peer=bot_info,
                random_id=client.rnd_id(),
                start_param="start",
            )
        )
        await sleep(1.5)

        status = await client.get_messages(
            "SpamBot", response.updates[1].message.id + 1
        )

        if not status or not getattr(status, "text", None):
            await msg.edit(f"{ggl}Gagal membaca balasan SpamBot.")
            return

        text = status.text or ""
        # Heuristic: short reply usually means clean account
        limited = len(text) > 100

        if limited:
            result = (
                f"{ggl}<b>Status:</b> akun bermasalah / kena batasan\n"
                f"<b>Detail:</b> cek @SpamBot untuk info lengkap"
            )
        else:
            result = (
                f"{brhsl}<b>Status:</b> akun aman\n"
                f"<b>Limit:</b> tidak terdeteksi"
            )

        await msg.edit(
            f"<blockquote>{result}\n"
            f"<b>Userbot:</b> {bot.me.mention}</blockquote>"
        )

        try:
            await client.invoke(DeleteHistory(peer=bot_info, max_id=0, revoke=True))
        except Exception:
            pass

    except Exception as e:
        logger.error(f"limit check failed: {e}")
        await msg.edit(f"{ggl}Gagal cek limit:\n<code>{e}</code>")
