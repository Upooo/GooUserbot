from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from GooUbot import *


class MSG:     
    def EXP_MSG_UBOT(X):
        return f"""
<blockquote><b>❏ ᴘᴇᴍʙᴇʀɪᴛᴀʜᴜᴀɴ</b>
<b>├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ ɪᴅ:</b> <code>{X.me.id}</code>
<b>╰ ᴍᴀsᴀ ᴀᴋᴛɪꜰ ᴛᴇʟᴀʜ ʜᴀʙɪs</b></blockquote>
"""

    def START(message):
        return f"""
<blockquote><b>👋🏻 ʜᴀʟᴏ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a></b>❕</blockquote>

<blockquote><b>{bot.me.mention} ᴀᴅᴀʟᴀʜ ʙᴏᴛ ʏᴀɴɢ ᴅᴀᴘᴀᴛ ᴍᴇᴍʙᴜᴀᴛ ᴜꜱᴇʀʙᴏᴛ ᴅᴇɴɢᴀɴ ᴍᴜᴅᴀʜ.</b>
<b>ʙᴏᴛ ɪɴɪ ᴅɪ ᴋᴇᴍʙᴀɴɢɪɴ ꜱᴀᴍᴀ : <a href=tg://user?id={OWNER_ID}>ᴛᴇᴀᴍ ɪᴅᴏʟ</a>, ᴋᴀʟᴏ ᴀᴅᴀ ᴇʀᴏʀ ᴀᴛᴀᴜ ᴘʀᴏʙʟᴇᴍ ʟᴀɴɢꜱᴜɴɢ ᴅᴍ ᴏᴡɴᴇʀ ɴʏᴀ ᴀᴊᴀ.</b></blockquote>

<blockquote><b>👉 ꜱᴇᴋᴀʀᴀɴɢ, ᴛɪɴɢɢᴀʟ ᴘɪʟɪʜ ʟᴀʟᴜ ᴛᴇᴋᴀɴ ᴛᴏᴍʙᴏʟ ᴅɪ ʙᴀᴡᴀʜ ɪɴɪ❗</b></blockquote>
"""

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 sɪʟᴀʜᴋᴀɴ ᴍᴇʟᴀᴋᴜᴋᴀɴ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴛᴇʀʟᴇʙɪʜ ᴅᴀʜᴜʟᴜ</b></blockquote>
<blockquote><b>silahkan chat owner saya
OWNER BOT : <a href=tg://openmessage?user_id={OWNER_ID}>nathann.</a></b></blockquote>

<blockquote><b>🛍 ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ᴋᴏɴꜰɪʀᴍᴀsɪ ᴜɴᴛᴜᴋ ᴋɪʀɪᴍ ʙᴜᴋᴛɪ ᴘᴇᴍʙᴀʏᴀʀᴀɴ ᴀɴᴅᴀ</b></blockquote>
"""

    async def UBOT(count):
        return f"""
<blockquote><b>⌬ ᴜsᴇʀʙᴏᴛ ᴋᴇ</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ ᴀᴋᴜɴ:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ╰ ɪᴅ:</b> <code>{ubot._ubot[int(count)].me.id}</code></blockquote>
"""

    def POLICY():
        return """
<blockquote><b>ʙᴜᴀᴛ ʏᴀɴɢ ɴᴀɴʏᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴ ᴜsᴇʀʙᴏᴛ ʏᴀɴɢ ᴀᴍᴀɴ ʙᴜᴀᴛ ᴅɪ ᴘᴀsᴀɴɢ ᴅɪ ᴀᴋᴜɴ ɪᴅ ᴀᴡᴀʟᴀɴ ʙᴇʀᴀᴘᴀ ʏᴀ??</b></blockquote>
<blockquote><b>ɢɪɴɪ ᴜɴᴛᴜᴋ ᴘᴇɴɢɢᴜɴᴀ ᴜsᴇʀʙᴏᴛ ɪᴛᴜ ᴊᴀɴɢᴀɴ ᴘᴇɴɢɢᴜɴᴀ ɪᴅ ᴀᴡᴀʟᴀɴ 𝟼-𝟽 ᴋᴀʀɴᴀ sᴀɴɢᴀᴛ ʀᴀᴡᴀɴ ᴊɪᴋᴀ ᴅɪ ᴘᴀsᴀɴɢ ᴜsᴇʀʙᴏᴛ.
ᴜɴᴛᴜᴋ ᴘᴇᴍᴀᴋᴀɪᴀɴ ᴜsᴇʀʙᴏᴛ ʙɪᴀsᴀ ᴅɪ ᴘᴀᴋᴀɪ ᴅɪ ᴀᴋᴜɴ ʟᴀᴍᴀ ᴀᴛᴀᴜ ʙɪᴀsᴀ ɪᴅ ᴀᴡᴀʟᴀɴ 𝟷-𝟻,
sᴇᴍᴜᴀ ᴘᴇɴɢɢᴜɴᴀ ᴅᴀʀɪ ɪᴅ ᴛᴇʀsᴇʙᴜᴛ sᴜᴅᴀʜ ᴛᴇʀʙɪʟᴀɴɢ ᴀᴍᴀɴ ᴛᴀᴘɪ sᴇᴍᴜᴀ ᴛᴇʀɢᴀɴᴛᴜɴɢ ᴘᴇᴍᴀᴋᴀɪᴀɴ ᴋᴀʟɪᴀɴ.</b></blockquote>
"""
