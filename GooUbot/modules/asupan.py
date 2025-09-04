import random
from pyrogram.enums import MessagesFilter
from GooUbot import *

__MODULE__ = "asupan"
__HELP__ = """
<blockquote><b>--ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴀsᴜᴘᴀɴ--</b></blockquote>

<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}asupan</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ᴠɪᴅᴇᴏ ᴀꜱᴜᴘᴀɴ ʀᴀɴᴅᴏᴍ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cewek</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ꜰᴏᴛᴏ ᴄᴇᴡᴇ ʀᴀɴᴅᴏᴍ.</b></blockquote>
<blockquote><b>🚦 ᴘᴇʀɪɴᴛᴀʜ :</b> <code>{0}cowok</code>
🦠 ᴋᴇᴛ : ᴍᴇɴɢɪʀɪᴍ ꜰᴏᴛᴏ ᴄᴏᴡᴏ ʀᴀɴᴅᴏᴍ.</b></blockquote>
"""


@PY.UBOT("asupan")
@PY.TOP_CMD
async def video_asupan(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"<blockquote><b>{prs} ᴍᴇɴᴄᴀʀɪ ᴠɪᴅᴇᴏ ᴀꜱᴜᴘᴀɴ...</b></blockquote>")
    try:
        asupannya = []
        async for asupan in client.search_messages(
            "@AsupanNyaSaiki", filter=MessagesFilter.VIDEO
        ):
            asupannya.append(asupan)
        video = random.choice(asupannya)
        await video.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)


@PY.UBOT("cewek")
@PY.TOP_CMD
async def photo_cewek(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"<blockquote><b>{prs} ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b></blockquote>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@cewekepepmabar", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)

@PY.UBOT("cowok")
@PY.TOP_CMD
async def photo_cewek(client, message):
    prs = await EMO.PROSES(client)
    y = await message.reply_text(f"<blockquote><b>{prs} ᴍᴇɴᴄᴀʀɪ ᴀʏᴀɴɢ...</b></blockquote>")
    try:
        ayangnya = []
        async for ayang in client.search_messages(
            "@cowokepepmabar", filter=MessagesFilter.PHOTO
        ):
            ayangnya.append(ayang)
        photo = random.choice(ayangnya)
        await photo.copy(message.chat.id, reply_to_message_id=message.id)
        await y.delete()
    except Exception as error:
        await y.edit(error)
