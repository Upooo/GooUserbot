import os
from dotenv import load_dotenv

load_dotenv(".env")

# Telegram API (wajib diisi di .env)
API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")

# Bot Token (wajib)
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Limit
MAX_BOT = int(os.getenv("MAX_BOT", "50"))

# Owner & Devs
DEVS = list(map(int, os.getenv("DEVS", "").split())) if os.getenv("DEVS") else []
OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Logs & Blacklist
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "").split())) if os.getenv("BLACKLIST_CHAT") else []
LOGS_MAKER_UBOT = list(map(int, os.getenv("LOGS_MAKER_UBOT", "").split())) if os.getenv("LOGS_MAKER_UBOT") else []
LOGS_ON_UBOT = int(os.getenv("LOGS_ON_UBOT", "0"))

# Database
MONGO_URL = os.getenv("MONGO_URL")
NAMA_DB = os.getenv("NAMA_DB", "GooUserbotDB")

# Team (bisa dipindah ke database nanti)
GooTeam = [
    int(x) for x in os.getenv("GOO_TEAM", "").split() if x.strip().isdigit()
]
