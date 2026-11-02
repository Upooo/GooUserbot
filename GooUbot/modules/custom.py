__MODULE__ = "custom"
__HELP__ = """
<blockquote><b>Custom Text</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}text</code> [pong/owner/ubot] [value|none]
Ubah label text tampilan.
Contoh: <code>{0}text pong none</code></blockquote>

<blockquote><b>Perintah:</b> <code>{0}lihatemoji</code> (reply)
Tampilkan format custom emoji dari pesan.</blockquote>
"""

from pyrogram.enums import ParseMode

from GooUbot import *


def extract_emojis_from_entities(message):
    emojis = []
    for entity in message.entities or []:
        emoji = message.text[entity.offset : entity.offset + entity.length]
        emojis.append(emoji)
    return emojis


@PY.UBOT("text")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...", quote=True)

    if len(message.command) < 3:
        return await status.edit(
            f"{ggl}<code>{message.command[0]} [pong/owner/ubot] [value]</code>"
        )

    query_mapping = {
        "pong": "STRING_PONG",
        "owner": "STRING_OWNER",
        "ubot": "STRING_UBOT",
        "devs": "STRING_DEVS",
    }

    mapping = message.command[1].lower()
    value = " ".join(message.command[2:])

    if mapping not in query_mapping:
        return await status.edit(f"{ggl}Query tidak dikenal.")

    if value.lower() == "none":
        value = False

    await set_vars(client.me.id, query_mapping[mapping], value)
    await status.edit(f"{brhsl}Text <b>{mapping}</b> di-set ke: <code>{value}</code>")


@PY.UBOT("lihatemoji")
@PY.TOP_CMD
async def extract_emoji(client, message):
    ggl = await EMO.GAGAL(client)

    if not message.reply_to_message or not message.reply_to_message.entities:
        return await message.reply(f"{ggl}Reply ke pesan yang ada custom emoji.")

    try:
        custom_emoji_ids = [
            getattr(entity, "custom_emoji_id", None)
            for entity in message.reply_to_message.entities
        ]
        emojis = extract_emojis_from_entities(message.reply_to_message)

        formatted = "".join(
            f"<emoji id={emoji_id}>{emoji}</emoji>" if emoji_id else emoji
            for emoji_id, emoji in zip(custom_emoji_ids, emojis)
        )

        await message.reply(formatted, parse_mode=ParseMode.DISABLED)
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
