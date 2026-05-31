import asyncio
from datetime import datetime

from pytz import timezone
from pyrogram.types import (
    InlineKeyboardMarkup,
)

from GooUbot import *


CHECK_INTERVAL = 60
JAKARTA_TZ = timezone("Asia/Jakarta")


async def expiredUserbots() -> None:

    while True:

        for userbot in ubot._ubot.copy():

            try:
                expired_date = await get_expired_date(
                    userbot.me.id
                )

                if not expired_date:
                    continue

                today = datetime.now(
                    JAKARTA_TZ
                ).date()

                expired_day = (
                    expired_date.date()
                )

                if today < expired_day:
                    continue

                bot_username = (
                    bot.me.username
                )

                if bot_username:
                    try:
                        await userbot.unblock_user(
                            bot_username
                        )
                    except Exception:
                        pass

                try:
                    await userbot.log_out()
                except Exception:
                    pass

                await remove_ubot(
                    userbot.me.id
                )

                await remove_all_vars(
                    userbot.me.id
                )

                await rem_expired_date(
                    userbot.me.id
                )

                if (
                    userbot.me.id
                    in ubot._get_my_id
                ):
                    ubot._get_my_id.remove(
                        userbot.me.id
                    )

                if (
                    userbot
                    in ubot._ubot
                ):
                    ubot._ubot.remove(
                        userbot
                    )

                try:
                    await bot.send_message(
                        userbot.me.id,
                        MSG.EXP_MSG_UBOT(
                            userbot
                        ),
                        reply_markup=InlineKeyboardMarkup(
                            BTN.EXP_UBOT()
                        ),
                    )
                except Exception:
                    pass

                print(
                    "[INFO] "
                    f"{userbot.me.id} "
                    "expired and removed"
                )

            except Exception as e:
                print(
                    "[ERROR] "
                    f"{userbot.me.id} "
                    f"expired check failed: {e}"
                )

        await asyncio.sleep(
            CHECK_INTERVAL
        )

# import asyncio
# from datetime import datetime
# from pytz import timezone
# from pyrogram.types import InlineKeyboardMarkup

# from GooUbot import *

# async def expiredUserbots() -> None:
#     while True:
#         for X in ubot._ubot:
#             try:
#                 today = datetime.now(timezone("Asia/Jakarta")).strftime("%d-%m-%Y")
#                 expired = (await get_expired_date(X.me.id)).strftime("%d-%m-%Y")

#                 if today == expired:
#                     await X.unblock_user(bot.me.username)
#                     await remove_ubot(X.me.id)
#                     await remove_all_vars(X.me.id)
#                     await rem_expired_date(X.me.id)
#                     ubot._get_my_id.remove(X.me.id)
#                     ubot._ubot.remove(X)
#                     await X.log_out()

#                     await bot.send_message(
#                         X.me.id,
#                         MSG.EXP_MSG_UBOT(X),
#                         reply_markup=InlineKeyboardMarkup(BTN.EXP_UBOT()),
#                     )
#             except Exception:
#                 print(f"[INFO] - {X.me.id} - EXPIRED END")
#         await asyncio.sleep(60)
