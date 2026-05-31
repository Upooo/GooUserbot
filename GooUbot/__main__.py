import asyncio
import signal

import tornado.ioloop
import tornado.platform.asyncio

from GooUbot import *
from GooUbot.core.database.userbot import *


UBOT_START_TIMEOUT = 10


# ==========================
# SHUTDOWN
# ==========================

async def shutdown(sig):
    print(
        f"[INFO] "
        f"Received signal "
        f"{sig.name}. "
        f"Shutting down..."
    )

    tasks = [
        task
        for task in asyncio.all_tasks()
        if task is not asyncio.current_task()
    ]

    for task in tasks:
        task.cancel()

    print(
        f"[INFO] "
        f"Cancelling "
        f"{len(tasks)} "
        f"tasks..."
    )

    await asyncio.gather(
        *tasks,
        return_exceptions=True,
    )

    try:
        await bot.stop()
    except Exception as e:
        print(
            f"[ERROR] "
            f"Failed stopping bot: {e}"
        )


# ==========================
# USERBOT STARTUP
# ==========================

async def start_userbots():
    userbots = await get_userbots()

    for userbot_data in userbots:

        userbot = Ubot(
            **userbot_data
        )

        try:
            await asyncio.wait_for(
                userbot.start(),
                timeout=UBOT_START_TIMEOUT,
            )

        except asyncio.TimeoutError:

            await remove_ubot(
                int(userbot_data["name"])
            )

            print(
                "[INFO] "
                f"{userbot_data['name']} "
                "timeout "
                "while starting"
            )

        except Exception as e:

            await remove_ubot(
                int(userbot_data["name"])
            )

            print(
                "[ERROR] "
                f"{userbot_data['name']} "
                f"failed: {e}"
            )


# ==========================
# MAIN
# ==========================

async def main():

    await bot.start()

    await start_userbots()

    # safer cleanup
    await bash(
        "rm -f ./*.session*"
    )

    await asyncio.gather(
        loadPlugins(),
        installPeer(),
        expiredUserbots(),
        return_exceptions=True,
    )

    loop = asyncio.get_running_loop()

    for sig in (
        signal.SIGINT,
        signal.SIGTERM,
    ):
        loop.add_signal_handler(
            sig,
            lambda s=sig:
            asyncio.create_task(
                shutdown(s)
            )
        )

    # keep alive forever
    await asyncio.Future()


# ==========================
# ENTRYPOINT
# ==========================

if __name__ == "__main__":

    tornado.platform.asyncio.AsyncIOMainLoop().install()

    loop = (
        tornado.ioloop
        .IOLoop.current()
        .asyncio_loop
    )

    loop.run_until_complete(
        main()
    )


# import asyncio
# import signal
# from GooUbot.core.database.userbot import *
# import tornado.ioloop
# import tornado.platform.asyncio
# from pyrogram import Client
# from GooUbot import *

# async def shutdown(signal, loop):
#     print(f"Received exit signal {signal.name}...")
#     tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]

#     [task.cancel() for task in tasks]

#     print("Cancelling outstanding tasks")
#     await asyncio.gather(*tasks, return_exceptions=True)
#     loop.stop()

# async def main():
#     await bot.start()
#     for _ubot in await get_userbots():
#         ubot_ = Ubot(**_ubot)
#         try:
#             await asyncio.wait_for(ubot_.start(), timeout=10)
#         except asyncio.TimeoutError:
#             await remove_ubot(int(_ubot["name"]))
#             print(f"[ɪɴғᴏ]: {int(_ubot['name'])} ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇʀᴇsᴘᴏɴᴇ")
#         except Exception:
#             await remove_ubot(int(_ubot["name"]))
#             print(f"[ɪɴғᴏ]: {int(_ubot['name'])} ʙᴇʀʜᴀsɪʟ ᴅɪ ʜᴀᴘᴜs")
#     await bash("rm -rf *session*")
#     await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots())
#     stop_event = asyncio.Event()
#     loop = asyncio.get_running_loop()
#     for s in (signal.SIGINT, signal.SIGTERM):
#         loop.add_signal_handler(
#             s, lambda: asyncio.create_task(shutdown(s, loop))
#         )

#     try:
#         await stop_event.wait()
#     except asyncio.CancelledError:
#         pass
#     finally:
#         await bot.stop()

# if __name__ == "__main__":
#     tornado.platform.asyncio.AsyncIOMainLoop().install()
#     loop = tornado.ioloop.IOLoop.current().asyncio_loop
#     loop.run_until_complete(main())
