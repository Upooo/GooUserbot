# GooUserbot

Multi-client Telegram userbot built on **Kurigram** + **PyTgCalls**.

Bisa jalanin banyak akun userbot dalam satu instance, plugin-based, support voice chat, data di MongoDB.

## Features

- Multi-client (satu bot, banyak userbot)
- Plugin system modular (60+ module)
- Voice chat via PyTgCalls
- MongoDB backend
- Sistem expired / premium
- Logging ke file + console
- Rate-limit aman di broadcast
- Docker-ready

## Requirements

- Python 3.10+
- MongoDB
- FFmpeg (voice chat & media)

## Setup

```bash
git clone https://github.com/Upooo/GooUserbot.git
cd GooUserbot

python3 -m venv venv
source venv/bin/activate        # Linux / macOS
# venv\Scripts\activate         # Windows

pip install -U pip
pip install -r requirements.txt

cp .env.example .env
# isi .env sebelum jalanin
```

Minimal di `.env`:

| Variable | Keterangan |
|----------|------------|
| `API_ID` | dari [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | dari [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | dari [@BotFather](https://t.me/BotFather) |
| `OWNER_ID` | Telegram user ID kamu |
| `MONGO_URL` | connection string MongoDB |

Detail lengkap di `.env.example`.

## Run

```bash
python3 -m GooUbot
# atau
bash start.sh
```

Docker:

```bash
docker compose up -d --build
```

## Project Structure

```
GooUserbot/
├── GooUbot/
│   ├── __init__.py
│   ├── __main__.py
│   ├── config.py
│   ├── core/
│   │   ├── database/
│   │   ├── function/
│   │   └── helpers/
│   └── modules/
├── Dockerfile
├── docker-compose.yml
├── .env.example
├── requirements.txt
└── README.md
```

## Roadmap

**Phase 1 — Done**
- Cleanup repo (hapus file sensitif, venv, cookies)
- Secure config via `.env`
- README & struktur rapi

**Phase 2 — Done**
- Foundation Kurigram
- Fix event loop / startup
- Graceful shutdown & logging

**Phase 3 — In progress**
- Audit & polish module (admin, purge, broadcast, music, notes, dll)
- Rate-limit broadcast & invite
- Help text seragam
- Calculator aman (AST)

**Next**
- Proxy support per client
- Module AI / utility tambahan
- Permission / sudo refinement
- Support fitur Telegram terbaru

## Notes

Userbot melanggar ToS Telegram kalau dipake buat spam atau abuse. Risiko sendiri: floodwait, restrict, sampai permanent ban. Pakai bijak.

## License

Apache License 2.0

---

by [Upooo](https://github.com/Upooo)
