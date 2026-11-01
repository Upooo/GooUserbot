import asyncio
import logging
import signal
import sys

from GooUbot import bot, ubot, logger, get_aiosession
from GooUbot.core.database.userbot import get_userbots, remove_ubot
from GooUbot.core.function.plugins import loadPlugins
from GooUbot.core.function.expired import expiredUserbots

# Optional helpers that may exist
try:
    from GooUbot.core.helpers.tools import bash, installPeer
except ImportError:
    async def bash(cmd):
        pass

    async def installPeer():
        pass


async def shutdown(sig=None):
    logger.info("Shutting down gracefully...")

    # Stop all userbots
    for client in list(ubot._ubot):
        try:
            await client.stop()
        except Exception as e:
            logger.warning(f"Failed to stop userbot {getattr(client.me, 'id', '?')}: {e}")

    try:
        await bot.stop()
    except Exception:
        pass

    # Close aiohttp session
    try:
        session = await get_aiosession()
        if session and not session.closed:
            await session.close()
    except Exception:
        pass

    logger.info("Shutdown complete.")
    sys.exit(0)


async def start_userbots():
    """Start all saved userbots from database."""
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

    # Start the assistant bot first
    await bot.start()

    # Start all userbots
    await start_userbots()

    # Load plugins & other background tasks
    await loadPlugins()

    try:
        await installPeer()
    except Exception as e:
        logger.warning(f"installPeer failed: {e}")

    # Start expired checker in background
    asyncio.create_task(expiredUserbots())

    logger.info("GooUserbot is running. Press Ctrl+C to stop.")

    # Keep running
    stop_event = asyncio.Event()

    loop = asyncio.get_running_loop()
    for sig in (signal.SIGINT, signal.SIGTERM):
        try:
            loop.add_signal_handler(sig, lambda: asyncio.create_task(shutdown(sig)))
        except NotImplementedError:
            # Windows
            pass

    try:
        await stop_event.wait()
    except asyncio.CancelledError:
        pass
    finally:
        await shutdown()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
