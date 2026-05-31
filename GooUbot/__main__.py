import asyncio
import signal

from GooUbot.core.database.userbot import *
from GooUbot import *


# ==========================
# SAFE SHUTDOWN
# ==========================
async def shutdown(sig, loop):
    print(f"Received exit signal {sig.name}...")

    tasks = [
        t for t in asyncio.all_tasks()
        if t is not asyncio.current_task()
    ]

    for task in tasks:
        task.cancel()

    await asyncio.gather(*tasks, return_exceptions=True)

    try:
        await bot.stop()
    except Exception:
        pass

    loop.stop()


# ==========================
# MAIN STARTUP
# ==========================
async def main():
    await bot.start()

    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await asyncio.wait_for(ubot_.start(), timeout=10)
        except Exception:
            await remove_ubot(int(_ubot["name"]))

    await bash("rm -rf *session*")

    await asyncio.gather(
        loadPlugins(),
        installPeer(),
        expiredUserbots(),
    )

    loop = asyncio.get_running_loop()

    for s in (signal.SIGINT, signal.SIGTERM):
        loop.add_signal_handler(
            s,
            lambda s=s: asyncio.create_task(shutdown(s, loop))
        )

    # keep alive
    await asyncio.Event().wait()


# ==========================
# ENTRYPOINT FIXED
# ==========================
if __name__ == "__main__":
    asyncio.run(main())

# import asyncio
# import signal

# from GooUbot.core.database.userbot import *
# from GooUbot import *


# async def shutdown(sig, loop):
#     print(f"Received exit signal {sig.name}...")

#     tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
#     [task.cancel() for task in tasks]

#     await asyncio.gather(*tasks, return_exceptions=True)
#     loop.stop()


# async def main():
#     await bot.start()

#     for _ubot in await get_userbots():
#         ubot_ = Ubot(**_ubot)
#         try:
#             await asyncio.wait_for(ubot_.start(), timeout=10)
#         except Exception:
#             await remove_ubot(int(_ubot["name"]))

#     await bash("rm -rf *session*")

#     await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots())

#     stop_event = asyncio.Event()
#     loop = asyncio.get_running_loop()

#     for s in (signal.SIGINT, signal.SIGTERM):
#         loop.add_signal_handler(
#             s,
#             lambda s=s: asyncio.create_task(shutdown(s, loop))
#         )

#     await stop_event.wait()
#     await bot.stop()


# if __name__ == "__main__":
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(main())