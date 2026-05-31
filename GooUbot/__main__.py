import asyncio
import signal

from GooUbot import *
from GooUbot.core.database.userbot import *


UBOT_START_TIMEOUT = 10


# ==========================
# GLOBAL SHUTDOWN
# ==========================

async def shutdown(sig):
    print(f"[INFO] Signal {sig.name} received. Shutting down...")

    # stop bot
    try:
        await bot.stop()
    except Exception as e:
        print(f"[ERROR] bot stop failed: {e}")

    # stop all userbots
    try:
        for ub in getattr(Ubot, "_ubot", []):
            try:
                await ub.stop()
            except Exception:
                pass
    except Exception:
        pass

    # cancel tasks
    tasks = [
        t for t in asyncio.all_tasks()
        if t is not asyncio.current_task()
    ]

    for t in tasks:
        t.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)


# ==========================
# USERBOT STARTUP
# ==========================

async def start_userbots():
    userbots = await get_userbots()

    tasks = []

    for userbot_data in userbots:

        userbot = Ubot(**userbot_data)

        async def start_one(ub, data):
            try:
                await asyncio.wait_for(
                    ub.start(),
                    timeout=UBOT_START_TIMEOUT,
                )

            except asyncio.TimeoutError:
                await remove_ubot(int(data["name"]))
                print(f"[TIMEOUT] {data['name']} removed")

            except Exception as e:
                await remove_ubot(int(data["name"]))
                print(f"[ERROR] {data['name']} failed: {e}")

        tasks.append(start_one(userbot, userbot_data))

    # 🔥 PARALLEL START (lebih cepat & stabil)
    await asyncio.gather(*tasks, return_exceptions=True)


# ==========================
# MAIN
# ==========================

async def main():

    await bot.start()

    await start_userbots()

    await bash("rm -f ./*.session*")

    # FIXED GATHER USAGE
    await asyncio.gather(
        loadPlugins(),
        installPeer(),
        expiredUserbots(),
        return_exceptions=True
    )

    loop = asyncio.get_running_loop()

    for sig in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(
            sig,
            lambda s=sig: asyncio.create_task(shutdown(s))
        )

    await asyncio.Future()


# ==========================
# ENTRYPOINT
# ==========================

if __name__ == "__main__":

    # 🔥 OPTIONAL: ini boleh dihapus kalau gak pakai tornado fitur khusus
    # tornado.platform.asyncio.AsyncIOMainLoop().install()

    asyncio.run(main())
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
