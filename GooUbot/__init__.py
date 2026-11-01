import logging
import os
import re
import sys

from pyrogram import Client, filters
from pyrogram.enums import ParseMode
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.types import Message
from pytgcalls import PyTgCalls
from pyromod import listen
from aiohttp import ClientSession

from GooUbot.config import *

# -------------------- Logging --------------------
logger = logging.getLogger("GooUbot")
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    "[%(levelname)s] - %(name)s - %(message)s", "%d-%b %H:%M"
)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logging.getLogger("pyrogram").setLevel(logging.WARNING)
logging.getLogger("pytgcalls").setLevel(logging.WARNING)
logging.getLogger("ntgcalls").setLevel(logging.WARNING)

# Lazy aiohttp session
aiosession = None


async def get_aiosession():
    global aiosession
    if aiosession is None or aiosession.closed:
        aiosession = ClientSession()
    return aiosession


# -------------------- Bot Client --------------------
class Bot(Client):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(MessageHandler(func, filters), group)
            return func
        return decorator

    def on_callback_query(self, filters=None, group=-1):
        def decorator(func):
            self.add_handler(CallbackQueryHandler(func, filters), group)
            return func
        return decorator

    async def start(self):
        await super().start()
        logger.info(f"Bot started as {self.me.full_name} ({self.me.id})")


# -------------------- Userbot Client --------------------
class Ubot(Client):
    __module__ = "pyrogram.client"
    _ubot = []
    _prefix = {}
    _get_my_id = []
    _translate = {}
    _get_my_peer = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.call_py = PyTgCalls(self)

    def on_message(self, filters=None, group=-1):
        def decorator(func):
            for ub in list(self._ubot):
                ub.add_handler(MessageHandler(func, filters), group)
            return func
        return decorator

    def set_prefix(self, user_id, prefix):
        self._prefix[user_id] = prefix

    async def get_prefix(self, user_id):
        return self._prefix.get(user_id, ["."])

    def cmd_prefix(self, cmd):
        command_re = re.compile(r"([\"'])(.*?)(?<!\\)\1|(\S+)")

        async def func(_, client, message):
            if not message.text:
                return False

            text = message.text.strip()
            username = client.me.username or ""
            prefixes = await self.get_prefix(client.me.id)

            for prefix in prefixes:
                if not text.startswith(prefix):
                    continue

                without_prefix = text[len(prefix):]

                for command in cmd.split("|"):
                    if not re.match(
                        rf"^(?:{command}(?:@?{username})?)(?:\s|$)",
                        without_prefix,
                        flags=re.IGNORECASE | re.UNICODE,
                    ):
                        continue

                    without_command = re.sub(
                        rf"{command}(?:@?{username})?\s?",
                        "",
                        without_prefix,
                        count=1,
                        flags=re.IGNORECASE | re.UNICODE,
                    )
                    message.command = [command] + [
                        re.sub(r"\\([\"'])", r"\1", m.group(2) or m.group(3) or "")
                        for m in command_re.finditer(without_command)
                    ]
                    return True

            return False

        return filters.create(func)

    async def start(self):
        await super().start()
        await self.call_py.start()

        try:
            from GooUbot.core.database.pref import get_pref
            handler = await get_pref(self.me.id)
            self._prefix[self.me.id] = handler if handler else ["."]
        except Exception:
            self._prefix[self.me.id] = ["."]

        self._ubot.append(self)
        self._get_my_id.append(self.me.id)
        self._translate[self.me.id] = "id"

        logger.info(f"Userbot started: {self.me.full_name} ({self.me.id})")


# -------------------- Validate Config --------------------
def validate_config():
    missing = []
    if not API_ID or API_ID == 0:
        missing.append("API_ID")
    if not API_HASH:
        missing.append("API_HASH")
    if not BOT_TOKEN:
        missing.append("BOT_TOKEN")
    if not MONGO_URL:
        missing.append("MONGO_URL")
    if not OWNER_ID or OWNER_ID == 0:
        missing.append("OWNER_ID")

    if missing:
        logger.error("Missing required environment variables:")
        for m in missing:
            logger.error(f"  - {m}")
        logger.error("Please check your .env file (see .env.example)")
        sys.exit(1)


validate_config()

# Placeholders - real instances created in __main__ inside the running loop
bot = None
ubot = None


def init_clients():
    """Create bot and ubot instances inside a running event loop."""
    global bot, ubot
    bot = Bot(
        name="GooUbot",
        bot_token=BOT_TOKEN,
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=True,
    )
    ubot = Ubot(name="GooUbot")
    return bot, ubot


# Import submodules (they may reference bot/ubot later at runtime)
from GooUbot.core.database import *
from GooUbot.core.function import *
from GooUbot.core.helpers import *
