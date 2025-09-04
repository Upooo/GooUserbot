__MODULE__ = "owner"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴏᴡɴᴇʀ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}prem [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪ ᴀᴋꜱᴇꜱ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}unprem [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ᴀᴋꜱᴇꜱ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}getprem [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʟɪꜱᴛ ᴜꜱᴇʀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}seles [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪ ᴀᴋꜱᴇꜱ ꜱᴇʟʟᴇʀ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}unseles [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ᴀᴋꜱᴇꜱ ꜱᴇʟʟᴇʀ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}getseles [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʟɪꜱᴛ ᴜꜱᴇʀ ꜱᴇʟʟᴇʀ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}addadmin [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪ ᴀᴋꜱᴇꜱ ᴀᴅᴍɪɴ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}deladmin [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ᴀᴋꜱᴇꜱ ᴀᴅᴍɪɴ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}getadmin [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇʟɪʜᴀᴛ ʟɪꜱᴛ ᴜꜱᴇʀ ᴀᴅᴍɪɴ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}addultra [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴇʀɪ ᴀᴋꜱᴇꜱ ꜱᴜᴘᴇʀᴜʟᴛʀᴀ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ : <code>{0}rmultra [reply/id/username]</code>
🦠 ᴋᴇᴛ : ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜꜱ ᴀᴋꜱᴇꜱ ꜱᴜᴘᴇʀᴜʟᴛʀᴀ ᴜꜱᴇʀʙᴏᴛ.</b></blockquote>
"""

from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone
from GooUbot.config import OWNER_ID
from GooUbot import *

@PY.UBOT("prem")
@PY.BOT("prem")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user = message.from_user
    seller_id = await get_list_from_vars(bot.me.id, "SELER_USERS")
    if user.id not in seller_id:
        return
    user_id, get_bulan = await extract_user_and_reason(message)
    msg = await message.reply(f"<blockquote><b>{prs} ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b></blockquote>")
    if not user_id:
        return await msg.edit(f"<blockquote><b>{ggl} {message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ - ʙᴜʟᴀɴ</b></blockquote>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)
    if not get_bulan:
        get_bulan = 1

    prem_users = await get_list_from_vars(bot.me.id, "PREM_USERS")

    if user.id in prem_users:
        return await msg.edit(f"""
<blockquote>
<b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ꜱᴜᴅᴀʜ ᴘʀᴇᴍɪᴜᴍ</b>
<b>ᴇxᴘɪʀᴇᴅ: {get_bulan} ʙᴜʟᴀɴ</b></blockquote>
"""
        )

    try:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(user_id, expired)
        await add_to_vars(bot.me.id, "PREM_USERS", user.id)
        await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴇxᴘɪʀᴇᴅ: {get_bulan} ʙᴜʟᴀɴ</b>
<b>ꜱɪʟᴀʜᴋᴀɴ ʙᴜᴋᴀ @{bot.me.username} ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ</b></blockquote>
"""
        )
        return await bot.send_message(
            OWNER_ID,
            f"• ɪᴅ-ꜱᴇʟʟᴇʀ: `{message.from_user.id}`\n\n• ɪᴅ-ᴄᴜꜱᴛᴏᴍᴇʀ: `{user_id}`",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "ꜱᴇʟʟᴇʀ",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton(
                            "ᴄᴜꜱᴛᴏᴍᴇʀ", callback_data=f"profil {user_id}"
                        ),
                    ],
                ]
            ),
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unprem")
@PY.BOT("unprem")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    msg = await message.reply(f"<blockquote><b>{prs} ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<blockquote><b>{ggl} {message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b></blockquote>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    prem_users = await get_list_from_vars(bot.me.id, "PREM_USERS")

    if user.id not in prem_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴀꜰᴛᴀʀ</ci></b></blockquote>
"""
        )
    try:
        await remove_from_vars(bot.me.id, "PREM_USERS", user.id)
        await rem_expired_date(user_id)
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ</ci></b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)
        

@PY.UBOT("getprem")
@PY.BOT("getprem")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    text = ""
    count = 0
    user = message.from_user
    seller_id = await get_list_from_vars(bot.me.id, "SELER_USERS")
    if user.id not in seller_id:
        return
    prem = await get_list_from_vars(bot.me.id, "PREM_USERS")
    prem_users = []

    for user_id in prem:
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"<blockquote><b>{userlist}\n</blockquote></b>"
    if not text:
        await message.reply_text("<blockquote><b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b></blockquote>")
    else:
        await message.reply_text(text)


@PY.UBOT("seles")
@PY.BOT("seles")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    msg = await message.reply("<blockquote><b>ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<blockquote><b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b><blockquote>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ꜱᴜᴅᴀʜ ʀᴇꜱᴇʟʟᴇʀ</ci></b></blockquote>
"""
        )

    try:
        await add_to_vars(bot.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ʀᴇꜱᴇʟʟᴇʀ</ci></b>
<b>ꜱɪʟᴀʜᴋᴀɴ ʙᴜᴋᴀ @{bot.me.username}</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unseles")
@PY.BOT("unseles")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    msg = await message.reply("<blockquote><b>ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<blockquote><b>{message.text} ᴜsᴇʀ_ɪᴅ/ᴜsᴇʀɴᴀᴍᴇ</b><blockquote>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    seles_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if user.id not in seles_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴀꜰᴛᴀʀ</ci></b></blockquote>
"""
        )

    try:
        await remove_from_vars(bot.me.id, "SELER_USERS", user.id)
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛᴇʟᴀʜ ᴅɪ ʜᴀᴘᴜꜱ ᴅᴀʀɪ ᴅᴀᴛᴀʙᴀꜱᴇ</ci></b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getseles")
@PY.BOT("getseles")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply("<blockquote><b>ꜱᴇᴅᴀɴɢ ᴍᴇᴍᴘʀᴏꜱᴇꜱ...</b></blockquote>")
    seles_users = await get_list_from_vars(bot.me.id, "SELER_USERS")

    if not seles_users:
        return await Sh.edit("<blockquote><b>ᴅᴀꜰᴛᴀʀ ꜱᴇʟʟᴇʀ ᴋᴏꜱᴏɴɢ</b></blockquote>")

    seles_list = []
    for user_id in seles_users:
        try:
            user = await client.get_users(int(user_id))
            seles_list.append(
                f"<blockquote>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | `{user.id}`</blockquote>"
            )
        except:
            continue

    if seles_list:
        response = (
            "<blockquote><b>📋 ᴅᴀꜰᴛᴀʀ ʀᴇꜱᴇʟʟᴇʀ:</b></blockquote>\n\n"
            + "\n".join(seles_list)
            + f"\n\n<blockquote><b>ᴛᴏᴛᴀʟ ʀᴇꜱᴇʟʟᴇʀ: {len(seles_list)}</b></blockquote>"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit("<blockquote><b>ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀꜰᴛᴀʀ ꜱᴇʟʟᴇʀ</b></blockquote>")


@PY.UBOT("time")
@PY.BOT("time")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Tm = await message.reply("<blockquote><b>ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b></blockquote>")
    bajingan = message.command
    if len(bajingan) != 3:
        return await Tm.edit(f"<blockquote><b>ɢᴜɴᴀᴋᴀɴ /time ᴜꜱᴇʀ_ɪᴅ ʜᴀʀɪ</b></blockquote>")
    user_id = int(bajingan[1])
    get_day = int(bajingan[2])
    print(user_id , get_day)
    try:
        get_id = (await client.get_users(user_id)).id
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"""
<blockquote><b>💬 ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b></blockquote>
<blockquote><b>ɴᴀᴍᴇ : {user.mention}
ɪᴅ : {get_id}</b></blockquote>
<blockquote><b>ᴅɪ ᴀᴋᴛɪꜰᴋᴀɴ ꜱᴇʟᴀᴍᴀ: {get_day} ʜᴀʀɪ</b></blockquote>
"""
    )


@PY.UBOT("cek")
@PY.BOT("cek")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply("<blockquote><b>ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await Sh.edit("<blockquote><b>ᴘᴇɴɢɢᴜɴᴀ ᴛɪᴅᴀᴋ ᴛᴇᴍᴜᴋᴀɴ</b></blockquote>")
    try:
        get_exp = await get_expired_date(user_id)
        sh = await client.get_users(user_id)
    except Exception as error:
        return await Sh.ediit(error)
    if get_exp is None:
        await Sh.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: {sh.mention}</b>
<b>ɪᴅ: `{user_id}`</b>
<b>ᴘʟᴀɴ : ɴᴏɴᴇ</b>
<b>ᴘʀᴇꜰɪx : .</b>
<b>ᴇxᴘɪʀᴇᴅ : ɴᴏɴᴀᴋᴛɪꜰ</b></blockquote>
""")
    else:
        SH = await ubot.get_prefix(user_id)
        exp = get_exp.strftime("%d-%m-%Y")
        if user_id in await get_list_from_vars(bot.me.id, "ULTRA_PREM"):
            status = "SuperUltra"
        else:
            status = "Premium"
        await Sh.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: {sh.mention}</b>
<b>ɪᴅ: `{user_id}`</b>
<b>ᴘʟᴀɴ : {status}</b>
<b>ᴘʀᴇꜰɪx : {' '.join(SH)}</b>
<b>ᴇxᴘɪʀᴇᴅ : {exp}</b></blockquote>
"""
        )


@PY.UBOT("addadmin")
@PY.BOT("addadmin")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    msg = await message.reply("<blockquote><b>ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<blockquote><b>{message.text} user_id/username</b></blockquote>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

    if user.id in admin_users:
        return await msg.edit(f"""
<blockquote><b>💬 ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b></blockquote>
<blockquote><b>ɴᴀᴍᴇ : [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ : {user.id}</b></blockquote>
<blockquote><b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ : ꜱᴜᴅᴀʜ ᴅᴀʟᴀᴍ ᴅᴀꜰᴛᴀʀ</b></blockquote>
"""
        )

    try:
        await add_to_vars(bot.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
<blockquote><b>💬 ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b></blockquote>
<blockquote><b>ɴᴀᴍᴇ : [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ : {user.id}</b></blockquote>
<blockquote><b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ : ᴀᴅᴍɪɴ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("unadmin")
@PY.BOT("deladmin")
async def _(client, message):
    user = message.from_user
    if user.id != OWNER_ID:
        return
    msg = await message.reply("<blockquote><b>ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<blockquote><b>{message.text} user_id/username</b></blockquote>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

    if user.id not in admin_users:
        return await msg.edit(f"""
<blockquote><b>💬 ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b></blockquote>
<blockquote><b>ɴᴀᴍᴇ : [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ : {user.id}</b></blockquote>
<blockquote><b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ : ᴛɪᴅᴀᴋ ᴅᴀʟᴀᴍ ᴅᴀꜰᴛᴀʀ</b></blockquote>
"""
        )

    try:
        await remove_from_vars(bot.me.id, "ADMIN_USERS", user.id)
        return await msg.edit(f"""
<blockquote><b>💬 ɪɴꜰᴏʀᴍᴀᴛɪᴏɴ</b></blockquote>
<blockquote><b>ɴᴀᴍᴇ : [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})
ɪᴅ : {user.id}</b></blockquote>
<blockquote><b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ : ᴅɪ ᴜɴᴀᴅᴍɪɴ</b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getadmin")
@PY.BOT("getadmin")
async def _(client, message):
    prs = await EMO.PROSES(client)
    ggl = await EMO.GAGAL(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return
    Sh = await message.reply(f"<blockquote><b>{prs} ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b></blockquote>")
    admin_users = await get_list_from_vars(bot.me.id, "ADMIN_USERS")

    if not admin_users:
        return await Sh.edit(f"<blockquote><b><s>{ggl}ᴅᴀꜰᴛᴀʀ ᴀᴅᴍɪɴ ᴋᴏꜱᴏɴɢ.</s></b></blockquote>")

    admin_list = []
    for user_id in admin_users:
        try:
            user = await client.get_users(int(user_id))
            admin_list.append(
                f"<blockquote><b>👤 [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | {user.id}</b></blockquote>"
            )
        except:
            continue

    if admin_list:
        response = (
            "<blockquote><b>📋 ᴅᴀꜰᴛᴀʀ ᴀᴅᴍɪɴ :</b></blockquote>\n\n"
            + "\n".join(admin_list)
            + f"\n\n<blockquote><b>ᴛᴏᴛᴀʟ ᴀᴅᴍɪɴ :</b></blockquote> {len(admin_list)}"
        )
        return await Sh.edit(response)
    else:
        return await Sh.edit(f"<blockquote><b>{ggl} ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴀᴍʙɪʟ ᴅᴀꜰᴛᴀʀ ᴀᴅᴍɪɴ.</b></blockquote>")

@PY.UBOT("addultra")
@PY.BOT("addultra")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴀᴜ ɴɢᴀᴘᴀɪɴ ᴊɪɴɢ?</b></blockquote>")
    msg = await message.reply(f"<blockquote><b>{prs} ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<blockquote><b>{ggl} {message.text} user_id/username</b></blockquote>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    ultra_users = await get_list_from_vars(bot.me.id, "ULTRA_PREM")

    if user.id in ultra_users:
        return await msg.edit(f"""
<blockquote>
<b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ꜱᴜᴅᴀʜ ꜱᴜᴘᴇʀᴜʟᴛʀᴀ</b>
</blockquote>
"""
        )
    try:
        await add_to_vars(bot.me.id, "ULTRA_PREM", user.id)
        return await msg.edit(f"""
<blockquote>
<b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ʙᴇʀʜᴀꜱɪʟ ꜱᴜᴘᴇʀᴜʟᴛʀᴀ</b>
</blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)

@PY.UBOT("rmultra")
@PY.BOT("rmultra")
async def _(client, message):
    prs = await EMO.PROSES(client)
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    user = message.from_user
    if user.id != OWNER_ID:
        return await message.reply_text(f"<blockquote><b>{ggl} ᴍᴀᴜ ɴɢᴀᴘᴀɪɴ ᴊɪɴɢ?</b></blockquote>")
    msg = await message.reply(f"<blockquote><b>{prs} ᴘʀᴏᴄᴇꜱꜱɪɴɢ...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit(
            f"<blockquote><b>{ggl}{message.text} user_id/username</b></blockquote>"
        )

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    ultra_users = await get_list_from_vars(bot.me.id, "ULTRA_PREM")

    if user.id not in ultra_users:
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ᴛɪᴅᴀᴋ ᴛᴇʀᴅᴀꜰᴛᴀʀ</ci></b></blockquote>
"""
        )
    try:
        await remove_from_vars(bot.me.id, "ULTRA_PREM", user.id)
        return await msg.edit(f"""
<blockquote><b>ɴᴀᴍᴇ: [{user.first_name} {user.last_name or ''}](tg://user?id={user.id})</b>
<b>ɪᴅ: `{user.id}`</b>
<b>ᴋᴇᴛᴇʀᴀɴɢᴀɴ: ʙᴇʀʜᴀꜱɪʟ ᴅɪ ʜᴀᴘᴜꜱ ᴅᴀʀɪ ꜱᴜᴘᴇʀᴜʟᴛʀᴀ</ci></b></blockquote>
"""
        )
    except Exception as error:
        return await msg.edit(error)
