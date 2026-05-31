import os
from dotenv import load_dotenv

load_dotenv(".env")

API_ID = int(os.getenv("API_ID", "20124949"))
API_HASH = os.getenv("API_HASH", "ff39880b27afecc7b5063766a78591db")

BOT_TOKEN = os.getenv("BOT_TOKEN")
MAX_BOT = int(os.getenv("MAX_BOT", "50"))

DEVS = list(map(int, os.getenv("DEVS", "8101612045").split()))
OWNER_ID = int(os.getenv("OWNER_ID", "8101612045"))  

BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002580967407").split()))
LOGS_MAKER_UBOT = list(map(int, os.getenv("LOGS_MAKER_UBOT", "-1002864434436").split()))
LOGS_ON_UBOT = int(os.getenv("LOGS_ON_UBOT", "-1002580967407"))

MONGO_URL = os.getenv("MONGO_URL")
NAMA_DB = os.getenv("NAMA_DB", "UselyubotDB")

GooTeam = [
    8101612045,
    7714463332,
    6642010805
]