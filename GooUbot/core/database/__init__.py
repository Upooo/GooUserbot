from motor.motor_asyncio import AsyncIOMotorClient
from GooUbot.config import MONGO_URL, NAMA_DB

mongo_client = AsyncIOMotorClient(MONGO_URL)
mongodb = mongo_client[NAMA_DB]

from GooUbot.core.database.expired import *
from GooUbot.core.database.userbot import *
from GooUbot.core.database.pref import *
from GooUbot.core.database.variabel import *