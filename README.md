# GooUserbot

**Multi-Client Telegram Userbot** berbasis Kurigram (Pyrogram fork) + PyTgCalls.

> Phase 1 & Phase 2 sudah selesai. Project sudah jauh lebih modern dan aman.

## Fitur Utama

- Multi-client (banyak akun userbot dalam 1 instance)
- Plugin system modular
- Voice Chat support (PyTgCalls)
- MongoDB untuk penyimpanan data
- Sistem expired / premium
- Banyak module utility, admin, fun, dll
- Graceful shutdown & better logging
- Config validation saat startup

## Requirements

- Python 3.10+
- MongoDB
- FFmpeg (untuk voice chat & media)

## Instalasi Cepat

```bash
# Clone repo
git clone https://github.com/Upooo/GooUserbot.git
cd GooUserbot

# Buat virtual environment
python3 -m venv venv
source venv/bin/activate   # Linux/macOS
# atau
venv\\Scripts\\activate    # Windows

# Install dependencies
pip install -U pip
pip install -r requirements.txt

# Setup environment
cp .env.example .env
nano .env   # isi semua yang wajib

# Jalankan
python3 -m GooUbot
# atau
bash start.sh
```

## Environment Variables

Lihat file `.env.example` untuk daftar lengkap. Yang **wajib** diisi:

| Variable     | Keterangan                          |
|--------------|-------------------------------------|
| `API_ID`     | Dari https://my.telegram.org        |
| `API_HASH`   | Dari https://my.telegram.org        |
| `BOT_TOKEN`  | Dari @BotFather                     |
| `OWNER_ID`   | Telegram ID kamu                    |
| `MONGO_URL`  | Connection string MongoDB           |

## Struktur Project

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
│   └── modules/          # 70+ plugin
├── .env.example
├── requirements.txt
├── start.sh
└── README.md
```

## Roadmap

### Phase 1 (Selesai)
- [x] Hapus file sensitif (`cookies.txt`)
- [x] Perbaiki `.gitignore`
- [x] Bersihkan `requirements.txt`
- [x] Amankan `config.py`
- [x] Tambah `.env.example`
- [x] README yang layak

### Phase 2 (Selesai)
- [x] Siap pakai **Kurigram** (drop-in replacement Pyrogram)
- [x] Update struktur core (`__init__.py` & `__main__.py`)
- [x] Graceful shutdown (tidak lagi `kill -9`)
- [x] Hapus operasi berbahaya (`rm -rf *session*`)
- [x] Config validation saat startup
- [x] Better logging
- [x] Pure asyncio (hapus Tornado)
- [x] uvloop support
- [x] Persiapan proxy per client

### Phase 3 (Berikutnya - Big Update)
- [ ] Audit & cleanup semua module
- [ ] Proxy support penuh
- [ ] Docker support
- [ ] Perbaikan sudo / permission system
- [ ] Update PyTgCalls lebih lanjut
- [ ] Support fitur Telegram terbaru (Business, Topics, dll)

## Peringatan

Menggunakan userbot **melanggar** Terms of Service Telegram jika disalahgunakan (spam, bulk messaging, dll). Risiko yang mungkin terjadi:

- FloodWait / Limit
- Account restricted / frozen
- Permanent ban

Gunakan dengan bijak. Developer tidak bertanggung jawab atas segala bentuk penyalahgunaan.

## License

Apache License 2.0

---

Made with ❤️ by [Upooo](https://github.com/Upooo)
