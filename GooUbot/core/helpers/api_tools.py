import random
import re

from pyrogram.enums import (
    MessagesFilter,
)

from GooUbot import get_aiosession


class API:

    WALL_CHANNELS = [
        "@animehikarixa",
        "@Anime_WallpapersHD",
    ]

    WALL_LIMIT = 100

    @staticmethod
    async def wall(client):

        channel = random.choice(
            API.WALL_CHANNELS
        )

        photos = []

        try:
            async for message in (
                client.search_messages(
                    channel,
                    filter=MessagesFilter.PHOTO,
                    limit=API.WALL_LIMIT,
                )
            ):
                photos.append(message)

        except Exception:
            return None

        return (
            random.choice(photos)
            if photos
            else None
        )

    @staticmethod
    async def waifu():

        url = (
            "https://www.waifu.im/search"
        )

        try:
            session = await get_aiosession()
            async with session.get(
                url,
                timeout=10,
            ) as response:

                if response.status != 200:
                    return None

                content = (
                    await response.text()
                )

        except Exception:
            return None

        match = re.search(
            r"var\s+files\s*=\s*\[(.*?)\]",
            content,
            re.DOTALL,
        )

        if not match:
            return None

        files = [
            item.strip("\"' ")
            for item in match.group(1).split(",")
            if item.strip()
        ]

        return (
            random.choice(files)
            if files
            else None
        )
