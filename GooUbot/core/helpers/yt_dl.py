from asyncio import get_event_loop
from functools import partial
from pathlib import Path

from yt_dlp import YoutubeDL


DOWNLOAD_DIR = "downloads"
COOKIE_FILE = "cookies.txt"


def run_sync(func, *args, **kwargs):
    return get_event_loop().run_in_executor(
        None,
        partial(func, *args, **kwargs),
    )


def format_duration(seconds):
    if not seconds:
        return "0:00"

    seconds = int(seconds)

    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    if hours:
        return f"{hours}:{minutes:02}:{seconds:02}"

    return f"{minutes}:{seconds:02}"


async def YoutubeDownload(url, as_video=False):
    Path(DOWNLOAD_DIR).mkdir(
        parents=True,
        exist_ok=True,
    )

    base_opts = {
        "quiet": True,
        "no_warnings": True,
        "nocheckcertificate": True,
        "geo_bypass": True,
        "cookiefile": COOKIE_FILE,
        "outtmpl": f"{DOWNLOAD_DIR}/%(id)s.%(ext)s",
        "noplaylist": True,
        "merge_output_format": "mp4",
    }

    if as_video:
        base_opts["format"] = (
            "bestvideo[height<=720][ext=mp4]+"
            "bestaudio[ext=m4a]/best[height<=720]"
        )
    else:
        base_opts["format"] = (
            "bestaudio[ext=m4a]/bestaudio"
        )

    data_ytp = (
        "<emoji id=6005994005148471369>💡</emoji> "
        "informasi {}\n\n"
        "<emoji id=5904544038643569182>🏷</emoji> "
        "nama: {}\n"
        "<emoji id=6030547358222127917>🧭</emoji> "
        "durasi: {}\n"
        "<emoji id=5233246225146332642>👀</emoji> "
        "dilihat: {}\n"
        "<emoji id=6005896024059547548>📢</emoji> "
        "channel: {}\n"
        "<emoji id=6005993794695076239>🔗</emoji> "
        'tautan: <a href="{}">youtube</a>'
    )

    ydl = YoutubeDL(base_opts)

    ytdl_data = await run_sync(
        ydl.extract_info,
        url,
        download=True,
    )

    file_name = ydl.prepare_filename(ytdl_data)

    # kalau merge mp4 hasil beda extension
    if as_video and not file_name.endswith(".mp4"):
        mp4_file = Path(file_name).with_suffix(".mp4")
        if mp4_file.exists():
            file_name = str(mp4_file)

    videoid = ytdl_data.get("id", "")
    title = ytdl_data.get("title", "Unknown")
    yt_url = f"https://youtu.be/{videoid}"

    duration = format_duration(
        ytdl_data.get("duration", 0)
    )

    channel = ytdl_data.get(
        "uploader",
        "Unknown",
    )

    views = "{:,}".format(
        ytdl_data.get("view_count", 0)
    ).replace(",", ".")

    thumb = (
        ytdl_data.get("thumbnail")
        or f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
    )

    return (
        file_name,
        title,
        yt_url,
        duration,
        views,
        channel,
        thumb,
        data_ytp,
    )

# from asyncio import get_event_loop
# from functools import partial

# from yt_dlp import YoutubeDL


# def run_sync(func, *args, **kwargs):
#     return get_event_loop().run_in_executor(None, partial(func, *args, **kwargs))


# async def YoutubeDownload(url, as_video=False):
#     if as_video:
#         ydl_opts = {
#             "quiet": True,
#             "no_warnings": True,
#             "format": "(bestvideo[height<=?720][width<=?1280][ext=mp4])+(bestaudio[ext=m4a])",
#             "outtmpl": "downloads/%(id)s.%(ext)s",
#             "nocheckcertificate": True,
#             "geo_bypass": True,
#             "cookiefile": "cookies.txt",
#         }
#     else:
#         ydl_opts = {
#             "quiet": True,
#             "no_warnings": True,
#             "format": "bestaudio[ext=m4a]",
#             "outtmpl": "downloads/%(id)s.%(ext)s",
#             "nocheckcertificate": True,
#             "geo_bypass": True,
#             "cookiefile": "cookies.txt",
#         }
#     data_ytp = "<emoji id=6005994005148471369>💡</emoji> informasi {}\n\n<emoji id=5904544038643569182>🏷</emoji> nama: {}\n<emoji id=6030547358222127917>🧭</emoji> durasi: {}\n<emoji id=5233246225146332642>👀</emoji> dlihat: {}\n<emoji id=6005896024059547548>📢</emoji> channel: {}\n<emoji id=6005993794695076239>🔗</emoji> tautan: <a href={}>youtube</a>"
#     ydl = YoutubeDL(ydl_opts)
#     ytdl_data = await run_sync(ydl.extract_info, url, download=True)
#     file_name = ydl.prepare_filename(ytdl_data)
#     videoid = ytdl_data["id"]
#     title = ytdl_data["title"]
#     url = f"https://youtu.be/{videoid}"
#     duration = ytdl_data["duration"]
#     channel = ytdl_data["uploader"]
#     views = f"{ytdl_data['view_count']:,}".replace(",", ".")
#     thumb = f"https://img.youtube.com/vi/{videoid}/hqdefault.jpg"
#     return file_name, title, url, duration, views, channel, thumb, data_ytp
