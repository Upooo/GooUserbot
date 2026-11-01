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
_devs = os.getenv("DEVS", "")
DEVS = [int(x) for x in _devs.split() if x.strip().isdigit()] if _devs else []

OWNER_ID = int(os.getenv("OWNER_ID", "0"))

# Logs & Blacklist
_blacklist = os.getenv("BLACKLIST_CHAT", "")
BLACKLIST_CHAT = [int(x) for x in _blacklist.split() if x.strip().lstrip("-").isdigit()] if _blacklist else []

_logs_maker = os.getenv("LOGS_MAKER_UBOT", "")
LOGS_MAKER_UBOT = [int(x) for x in _logs_maker.split() if x.strip().lstrip("-").isdigit()] if _logs_maker else []

LOGS_ON_UBOT = int(os.getenv("LOGS_ON_UBOT", "0"))

# Database
MONGO_URL = os.getenv("MONGO_URL")
NAMA_DB = os.getenv("NAMA_DB", "GooUserbotDB")

# Team
_team = os.getenv("GOO_TEAM", "")
GooTeam = [int(x) for x in _team.split() if x.strip().isdigit()] if _team else []
