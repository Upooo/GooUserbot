__MODULE__ = "control"
__HELP__ = """
<blockquote><b>Control</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}create</code> [group/channel] [nama]
Buat grup atau channel.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}createbot</code> [nama] [usernameBot]
Request bot baru ke @BotFather.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}prefix</code> [simbol...]
Set prefix command.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}emoji</code> [query] [emoji premium]
Set custom emoji (butuh Premium).
Query: pong, owner, ubot, proses, gcast, sukses, gagal, group, catatan, waktu, alasan, afk, menunggu</blockquote>
"""

import asyncio

from GooUbot import *


@PY.UBOT("create")
@PY.TOP_CMD
async def _(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 3:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [group/channel] [nama]</code>"
        )

    group_type = message.command[1].lower()
    group_name = " ".join(message.command[2:])
    status = await message.reply(f"{prs}Processing...")

    desc = f"Welcome to my {'group' if group_type == 'group' else 'channel'}"

    try:
        if group_type == "group":
            created = await client.create_supergroup(group_name, desc)
        elif group_type == "channel":
            created = await client.create_channel(group_name, desc)
        else:
            return await status.edit(f"{ggl}Type harus <code>group</code> atau <code>channel</code>.")

        chat = await client.get_chat(created.id)
        await status.edit(
            f"{brhsl}Berhasil buat {group_type}: [{group_name}]({chat.invite_link})",
            disable_web_page_preview=True,
        )
    except Exception as e:
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...", quote=True)
    if len(message.command) < 2:
        return await status.edit(f"{ggl}<code>{message.command[0]} [simbol...]</code>")

    ub_prefix = []
    for prefix in message.command[1:]:
        ub_prefix.append("" if prefix.lower() == "none" else prefix)

    try:
        client.set_prefix(message.from_user.id, ub_prefix)
        await set_pref(message.from_user.id, ub_prefix)
        parsed = " ".join(ub_prefix) if any(ub_prefix) else "(none)"
        return await status.edit(f"{brhsl}Prefix: <code>{parsed}</code>")
    except Exception as error:
        return await status.edit(f"{ggl}<code>{error}</code>")


@PY.UBOT("emoji")
@PY.TOP_CMD
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    status = await message.reply(f"{prs}Processing...", quote=True)

    if not client.me.is_premium:
        return await status.edit(f"{ggl}Butuh Telegram Premium.")

    if len(message.command) < 3:
        return await status.edit(
            f"{ggl}<code>{message.command[0]} [query] [emoji]</code>"
        )

    query_mapping = {
        "pong": "EMOJI_PING",
        "owner": "EMOJI_MENTION",
        "ubot": "EMOJI_USERBOT",
        "proses": "EMOJI_PROSES",
        "gcast": "EMOJI_BROADCAST",
        "sukses": "EMOJI_BERHASIL",
        "gagal": "EMOJI_GAGAL",
        "catatan": "EMOJI_KETERANGAN",
        "group": "EMOJI_GROUP",
        "menunggu": "EMOJI_MENUNGGU",
        "alasan": "EMOJI_ALASAN",
        "waktu": "EMOJI_WAKTU",
        "afk": "EMOJI_AFKA",
    }

    mapping = message.command[1].lower()
    value = message.command[2]

    if mapping not in query_mapping:
        return await status.edit(f"{ggl}Query tidak dikenal. Cek <code>.help control</code>")

    emoji_id = None
    if message.entities:
        for entity in message.entities:
            if getattr(entity, "custom_emoji_id", None):
                emoji_id = entity.custom_emoji_id
                break

    if not emoji_id:
        return await status.edit(f"{ggl}Kirim custom emoji premium.")

    await set_vars(client.me.id, query_mapping[mapping], emoji_id)
    await status.edit(
        f"{brhsl}Emoji <b>{mapping}</b> di-set ke <emoji id={emoji_id}>{value}</emoji>"
    )


@PY.UBOT("createbot")
@PY.TOP_CMD
async def create_bot_command(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)

    args = message.text.split(maxsplit=2)
    if len(args) < 3:
        return await message.reply(
            f"{ggl}<code>{message.command[0]} [nama] [usernameBot]</code>"
        )

    bot_name = args[1]
    bot_username = args[2]

    if not bot_username.endswith("Bot"):
        return await message.reply(f"{ggl}Username harus diakhiri <code>Bot</code>.")

    try:
        await client.send_message("BotFather", "/newbot")
        await asyncio.sleep(2)
        await client.send_message("BotFather", bot_name)
        await asyncio.sleep(2)
        await client.send_message("BotFather", bot_username)

        await message.reply(
            f"{brhsl}Request dikirim ke @BotFather\n"
            f"Nama: <code>{bot_name}</code>\n"
            f"Username: @{bot_username}\n"
            f"Cek chat BotFather untuk lanjut."
        )
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
