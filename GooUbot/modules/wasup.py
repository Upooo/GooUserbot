from GooUbot import *
from datetime import datetime, timedelta

#Callback handler untuk tombol free trial
@PY.CALLBACK("informasi_ubot")
async def free_trial_callback(client, callback_query):
    user_id = callback_query.from_user.id
    
    free_users = await get_list_from_vars(client.me.id, "informasi_ubot")
    if user_id in free_users:
        return await callback_query.answer("ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ ʏᴀ ɴᴀɴᴛɪ ᴀᴋᴜ ᴋɪʀɪᴍ ɪɴꜰᴏʀᴍᴀꜱɪ ᴛᴇɴᴛᴀɴɢ ᴀᴋᴜ.", show_alert=True)

    now = datetime.now(timezone("Asia/Jakarta"))
    expired = now + timedelta(hours=5)

    await set_expired_date(user_id, expired)
    await add_to_vars(client.me.id, "PREM_USERS", user_id)
    await add_to_vars(client.me.id, "FREE_PREM_USERS", user_id)

    await callback_query.answer("ᴛᴜɴɢɢᴜ ʙᴇɴᴛᴀʀ ʏᴀ ɴᴀɴᴛɪ ᴀᴋᴜ ᴋɪʀɪᴍ ɪɴꜰᴏʀᴍᴀꜱɪ ᴛᴇɴᴛᴀɴɢ ᴀᴋᴜ.", show_alert=True)
    
    # Kirim pesan dengan tombol inline    
    await bot.send_message(
        user_id,
        f"""
<blockquote><b>
❏ ɪɴғᴏʀᴍᴀᴛɪᴏɴ
├ ᴏᴡɴᴇʀ : @nathanidol
├ ᴏᴡɴᴇʀ : @nathgood
├ sᴜᴘᴘᴏʀᴛ : @nathsupport
├ ᴜsᴇʀʙᴏᴛ : @GooUbot
├ ᴜsᴇʀʙᴏᴛ : @GooUbot
╰ ᴍᴜꜱɪᴄ ʙᴏᴛ : @reexmusic_bot</b></blockquote>
""",
  )
  
