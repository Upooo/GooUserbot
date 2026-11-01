# GooUserbot

**Multi-Client Telegram Userbot** berbasis Pyrogram/Kurigram + PyTgCalls.

> Project ini sedang dalam tahap modernisasi (Phase 1 selesai).

## Fitur Utama

- Multi-client (banyak akun userbot dalam 1 instance)
- Plugin system modular
- Voice Chat support (PyTgCalls)
- MongoDB untuk penyimpanan data
- Sistem expired / premium
- Banyak module utility, admin, fun, dll

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

## Roadmap / Next Update

### Phase 1 (Selesai)
- [x] Hapus file sensitif (`cookies.txt`)
- [x] Perbaiki `.gitignore`
- [x] Bersihkan `requirements.txt`
- [x] Amankan `config.py` (hilangkan hardcoded secret)
- [x] Tambah `.env.example`
- [x] README yang layak

### Phase 2 (Berikutnya)
- [ ] Migrasi penuh ke **Kurigram** (fork Pyrogram yang aktif)
- [ ] Update PyTgCalls ke versi terbaru
- [ ] Hapus folder virtualenv `Goo/` dari history repo
- [ ] Tambah dukungan **proxy per client**
- [ ] Perbaiki error handling & logging
- [ ] Docker support
- [ ] Audit & cleanup module yang jarang dipakai / berbahaya

### Phase 3 (Future)
- [ ] Support Telegram Business features
- [ ] Sistem plugin yang lebih modern
- [ ] Web dashboard (opsional)
- [ ] Better rate-limit handling

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
