__MODULE__ = "stream"
__HELP__ = """
<blockquote><b>Stream / Music</b></blockquote>

<blockquote><b>Perintah:</b> <code>{0}play</code> [url/judul/reply audio]
Play audio di voice chat.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}vplay</code> [url/judul/reply video]
Play video di voice chat.</blockquote>

<blockquote><b>Perintah:</b> <code>{0}pause</code> / <code>{0}resume</code> / <code>{0}end</code>
Kontrol stream.</blockquote>
"""

import os
import re

from pytgcalls.types import MediaStream
from yt_dlp import YoutubeDL
from youtubesearchpython import VideosSearch

from GooUbot import *

DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)


def _safe_name(title: str) -> str:
    return re.sub(r"[^\w\s-]", "", title)[:80].strip() or "media"


@PY.UBOT("play")
@PY.TOP_CMD
@PY.GROUP
async def play_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if message.reply_to_message and message.reply_to_message.audio:
        status = await message.reply(f"{prs}Downloading...")
        try:
            audio_file = await message.reply_to_message.download(
                f"{DOWNLOAD_DIR}/{message.reply_to_message.audio.file_unique_id}"
            )
            if not audio_file.endswith(".opus"):
                opus_file = audio_file.rsplit(".", 1)[0] + ".opus"
                os.system(f"ffmpeg -i '{audio_file}' -acodec libopus '{opus_file}' -y -loglevel error")
                if os.path.exists(audio_file):
                    os.remove(audio_file)
                audio_file = opus_file

            await client.call_py.play(message.chat.id, MediaStream(audio_file))
            await status.edit(f"{brhsl}Playing audio.")
        except Exception as e:
            await status.edit(f"{ggl}<code>{e}</code>")
        return

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [url/judul]</code>")

    query = " ".join(message.command[1:])
    url = query if ("youtube.com" in query or "youtu.be" in query) else None

    if not url:
        search = VideosSearch(query, limit=1).result()
        if not search.get("result"):
            return await message.reply(f"{ggl}Lagu tidak ditemukan.")
        url = search["result"][0]["link"]

    status = await message.reply(f"{prs}Downloading audio...")
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "opus",
                "preferredquality": "192",
            }],
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = _safe_name(info.get("title", "audio"))
            file_path = f"{DOWNLOAD_DIR}/{title}.opus"

        # yt-dlp may use original title; resolve actual path
        if not os.path.exists(file_path):
            for f in os.listdir(DOWNLOAD_DIR):
                if f.endswith(".opus") and info.get("id", "") in f or title[:20] in f:
                    file_path = f"{DOWNLOAD_DIR}/{f}"
                    break

        if not os.path.exists(file_path):
            return await status.edit(f"{ggl}Download gagal.")

        await client.call_py.play(message.chat.id, MediaStream(file_path))
        await status.edit(f"{brhsl}Playing: <b>{info.get('title', 'audio')}</b>")
    except Exception as e:
        logger.error(f"play error: {e}")
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("vplay")
@PY.TOP_CMD
@PY.GROUP
async def play_video(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if message.reply_to_message and message.reply_to_message.video:
        status = await message.reply(f"{prs}Downloading...")
        try:
            video_file = await message.reply_to_message.download(
                f"{DOWNLOAD_DIR}/{message.reply_to_message.video.file_unique_id}.mp4"
            )
            await client.call_py.play(message.chat.id, MediaStream(video_file))
            await status.edit(f"{brhsl}Playing video.")
        except Exception as e:
            await status.edit(f"{ggl}<code>{e}</code>")
        return

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [url/judul]</code>")

    query = " ".join(message.command[1:])
    url = query if ("youtube.com" in query or "youtu.be" in query) else None

    if not url:
        search = VideosSearch(query, limit=1).result()
        if not search.get("result"):
            return await message.reply(f"{ggl}Video tidak ditemukan.")
        url = search["result"][0]["link"]

    status = await message.reply(f"{prs}Downloading video...")
    try:
        ydl_opts = {
            "format": "bv*+ba/b",
            "outtmpl": f"{DOWNLOAD_DIR}/%(title)s.%(ext)s",
            "noplaylist": True,
            "merge_output_format": "mp4",
            "quiet": True,
            "no_warnings": True,
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            title = _safe_name(info.get("title", "video"))
            file_path = f"{DOWNLOAD_DIR}/{title}.mp4"

        if not os.path.exists(file_path):
            for f in os.listdir(DOWNLOAD_DIR):
                if f.endswith(".mp4") and title[:20] in f:
                    file_path = f"{DOWNLOAD_DIR}/{f}"
                    break

        if not os.path.exists(file_path):
            return await status.edit(f"{ggl}Download gagal.")

        await client.call_py.play(message.chat.id, MediaStream(file_path))
        await status.edit(f"{brhsl}Playing: <b>{info.get('title', 'video')}</b>")
    except Exception as e:
        logger.error(f"vplay error: {e}")
        await status.edit(f"{ggl}<code>{e}</code>")


@PY.UBOT("pause")
@PY.TOP_CMD
@PY.GROUP
async def pause_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        await client.call_py.pause_stream(message.chat.id)
        await message.reply(f"{brhsl}Paused.")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")


@PY.UBOT("resume")
@PY.TOP_CMD
@PY.GROUP
async def resume_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        await client.call_py.resume_stream(message.chat.id)
        await message.reply(f"{brhsl}Resumed.")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")


@PY.UBOT("end")
@PY.TOP_CMD
@PY.GROUP
async def stop_audio(client, message):
    brhsl = await EMO.BERHASIL(client)
    ggl = await EMO.GAGAL(client)
    try:
        await client.call_py.leave_call(message.chat.id)
        await message.reply(f"{brhsl}Stopped & left VC.")
    except Exception as e:
        await message.reply(f"{ggl}<code>{e}</code>")
