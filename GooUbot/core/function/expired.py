import asyncio
from datetime import datetime
from pytz import timezone
from pyrogram.types import InlineKeyboardMarkup

from GooUbot import *

async def expiredUserbots() -> None:
    while True:
        for X in ubot._ubot:
            try:
                today = datetime.now(timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
                expired = (await get_expired_date(X.me.id)).strftime("%d-%m-%Y")

                if today == expired:
                    await X.unblock_user(bot.me.username)
                    await remove_ubot(X.me.id)
                    await remove_all_vars(X.me.id)
                    await rem_expired_date(X.me.id)
                    ubot._get_my_id.remove(X.me.id)
                    ubot._ubot.remove(X)
                    await X.log_out()

                    await bot.send_message(
                        X.me.id,
                        MSG.EXP_MSG_UBOT(X),
                        reply_markup=InlineKeyboardMarkup(BTN.EXP_UBOT()),
                    )
            except Exception:
                print(f"[INFO] - {X.me.id} - EXPIRED END")
        await asyncio.sleep(60)
