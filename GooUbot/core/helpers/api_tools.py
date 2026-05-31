import random
import re

from pyrogram.enums import (
    MessagesFilter,
)

from GooUbot import aiosession


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
            async with aiosession.get(
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
    
# import asyncio
# import random
# import requests

# from pyrogram.enums import MessagesFilter

# class API:
#     async def wall(client):
#         anime_channel = random.choice(["@animehikarixa", "@Anime_WallpapersHD"])
#         animenya = [
#             anime
#             async for anime in client.search_messages(
#                 anime_channel, filter=MessagesFilter.PHOTO
#             )
#         ]
#         return random.choice(animenya)

#     def waifu():
#         url = "https://www.waifu.im/search"
#         response = requests.get(url)
#         content = response.text
#         start_index = content.find("var files = [") + len("var files = ")
#         end_index = content.find("]", start_index)
#         files_str = content[start_index:end_index]
#         files = [file.strip('" ') for file in files_str.split(",")]
#         return random.choice(files)