import asyncio
import logging
import signal
import sys

# Set uvloop policy BEFORE any other imports that might touch the loop
try:
    import uvloop
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
except ImportError:
    pass

from GooUbot import bot, ubot, logger, get_aiosession, Ubot
from GooUbot.core.database.userbot import get_userbots, remove_ubot
from GooUbot.core.function.plugins import loadPlugins
from GooUbot.core.function.expired import expiredUserbots

try:
    from GooUbot.core.helpers.tools import bash, installPeer
except ImportError:
    async def bash(cmd):
        pass

    async def installPeer():
        pass


async def shutdown():
    logger.info("Shutting down gracefully...")

    for client in list(ubot._ubot):
        try:
            await client.stop()
        except Exception as e:
            logger.warning(f"Failed to stop userbot: {e}")

    try:
        await bot.stop()
    except Exception:
        pass

    try:
        session = await get_aiosession()
        if session and not session.closed:
            await session.close()
    except Exception:
        pass

    logger.info("Shutdown complete.")


async def start_userbots():
    userbots = await get_userbots()
    logger.info(f"Found {len(userbots)} userbot(s) in database")

    for data in userbots:
        user_id = int(data["name"])
        try:
            client = Ubot(
                name=str(user_id),
                api_id=data["api_id"],
                api_hash=data["api_hash"],
                session_string=data["session_string"],
                in_memory=True,
            )
            await asyncio.wait_for(client.start(), timeout=30)
        except asyncio.TimeoutError:
            logger.warning(f"Userbot {user_id} timed out, removing...")
            await remove_ubot(user_id)
        except Exception as e:
            logger.error(f"Failed to start userbot {user_id}: {e}")
            await remove_ubot(user_id)


async def main():
    logger.info("Starting GooUserbot...")

    await bot.start()
    await start_userbots()
    await loadPlugins()

    try:
        await installPeer()
    except Exception as e:
        logger.warning(f"installPeer failed: {e}")

    asyncio.create_task(expiredUserbots())

    logger.info("GooUserbot is running. Press Ctrl+C to stop.")

    stop_event = asyncio.Event()

    def _signal_handler():
        stop_event.set()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, _signal_handler)
        except NotImplementedError:
            pass

    await stop_event.wait()
    await shutdown()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
