__MODULE__ = "yt"
__HELP__ = """
<blockquote><b>YouTube Download</b></blockquote>

<blockquote><b>Perintah:</b>
<code>{0}song</code> [judul] — download audio
<code>{0}vsong</code> [judul] — download video</blockquote>
"""

import asyncio
import math
import os
from datetime import timedelta
from time import time

import wget
from pyrogram.errors import FloodWait, MessageNotModified
from youtubesearchpython import VideosSearch

from GooUbot import *


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    raised = 0
    units = {0: "", 1: "KB", 2: "MB", 3: "GB", 4: "TB"}
    while size > power:
        size /= power
        raised += 1
    return f"{round(size, 2)} {units[raised]}"


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(milliseconds, 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    parts = []
    if days:
        parts.append(f"{days}d")
    if hours:
        parts.append(f"{hours}h")
    if minutes:
        parts.append(f"{minutes}m")
    if seconds:
        parts.append(f"{seconds}s")
    return " ".join(parts) or "0s"


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time()
    diff = now - start
    if round(diff % 10.00) != 0 and current != total:
        return
    percentage = current * 100 / total
    speed = current / diff if diff else 0
    elapsed = round(diff) * 1000
    if elapsed == 0:
        return
    eta = round((total - current) / speed) * 1000 if speed else 0
    bar = f"{round(percentage, 1)}% · {humanbytes(current)}/{humanbytes(total)} · ETA {time_formatter(elapsed + eta)}"
    text = f"{type_of_ps}\n{bar}"
    if file_name:
        text = f"{type_of_ps}\n<code>{file_name}</code>\n{bar}"
    try:
        await message.edit(text)
    except (FloodWait, MessageNotModified):
        pass


async def vsong_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [judul]</code>")

    status = await message.reply(f"{prs}Searching...")
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as e:
        return await status.edit(f"{ggl}<code>{e}</code>")

    try:
        file_name, title, url, duration, views, channel, thumb, data_ytp = await YoutubeDownload(
            link, as_video=True
        )
    except Exception as e:
        return await status.edit(f"{ggl}<code>{e}</code>")

    thumbnail = wget.download(thumb)
    try:
        await client.send_video(
            message.chat.id,
            video=file_name,
            thumb=thumbnail,
            file_name=title,
            duration=duration,
            supports_streaming=True,
            caption=data_ytp.format(
                "video", title, timedelta(seconds=duration), views, channel, url, bot.me.mention
            ),
            progress=progress,
            progress_args=(status, time(), f"{prs}Uploading...", f"{search['id']}.mp4"),
            reply_to_message_id=message.id,
        )
        await status.delete()
    finally:
        for f in (thumbnail, file_name):
            if f and os.path.exists(f):
                os.remove(f)


@PY.UBOT("vsong")
@PY.TOP_CMD
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song")
@PY.TOP_CMD
async def song_cmd(client, message):
    ggl = await EMO.GAGAL(client)
    prs = await EMO.PROSES(client)

    if len(message.command) < 2:
        return await message.reply(f"{ggl}<code>{message.command[0]} [judul]</code>")

    status = await message.reply(f"{prs}Searching...")
    try:
        search = VideosSearch(message.text.split(None, 1)[1], limit=1).result()["result"][0]
        link = f"https://youtu.be/{search['id']}"
    except Exception as e:
        return await status.edit(f"{ggl}<code>{e}</code>")

    try:
        file_name, title, url, duration, views, channel, thumb, data_ytp = await YoutubeDownload(
            link, as_video=False
        )
    except Exception as e:
        return await status.edit(f"{ggl}<code>{e}</code>")

    thumbnail = wget.download(thumb)
    try:
        await client.send_audio(
            message.chat.id,
            audio=file_name,
            thumb=thumbnail,
            file_name=title,
            performer=channel,
            duration=duration,
            caption=data_ytp.format(
                "audio", title, timedelta(seconds=duration), views, channel, url, bot.me.mention
            ),
            progress=progress,
            progress_args=(status, time(), f"{prs}Uploading...", f"{search['id']}.mp3"),
            reply_to_message_id=message.id,
        )
        await status.delete()
    finally:
        for f in (thumbnail, file_name):
            if f and os.path.exists(f):
                os.remove(f)
