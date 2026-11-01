# GooUserbot

Multi-client Telegram userbot built on **Kurigram** + **PyTgCalls**.

Bisa jalanin banyak akun userbot dalam satu instance, plugin-based, support voice chat, dan data disimpan di MongoDB.

## Features

- Multi-client (satu bot, banyak userbot)
- Plugin system modular (60+ module)
- Voice chat via PyTgCalls
- MongoDB backend
- Sistem expired / premium
- Graceful shutdown & config validation

## Requirements

- Python 3.10+
- MongoDB
- FFmpeg (buat voice chat & media processing)

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
# isi .env dulu sebelum jalanin
```

Isi minimal di `.env`:

| Variable | Keterangan |
|----------|------------|
| `API_ID` | dari [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | dari [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | dari [@BotFather](https://t.me/BotFather) |
| `OWNER_ID` | Telegram user ID kamu |
| `MONGO_URL` | connection string MongoDB |

Detail lengkap ada di `.env.example`.

## Run

```bash
python3 -m GooUbot
# atau
bash start.sh
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
├── .env.example
├── requirements.txt
├── start.sh
└── README.md
```

## Roadmap

**Done**
- Cleanup repo (hapus file sensitif, venv, dll)
- Secure config via `.env`
- Migrasi foundation ke Kurigram
- Graceful shutdown, better logging, config validation
- Fix event loop issues

**Next**
- Audit & cleanup module
- Proxy support per client
- Docker
- Perbaikan permission / sudo system
- Support fitur Telegram terbaru

## Notes

Userbot melanggar ToS Telegram kalau dipake buat spam atau abuse. Risiko sendiri: floodwait, restrict, sampai permanent ban. Pakai bijak.

## License

Apache License 2.0

---

by [Upooo](https://github.com/Upooo)
