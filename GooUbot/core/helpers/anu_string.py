from GooUbot import get_vars


class STR:

    DEFAULTS = {
        "STRING_PONG": "ᴄʟᴏᴛ",
        "STRING_OWNER": "ᴏɴᴇʟ",
        "STRING_UBOT": "ᴜʙᴏᴛ",
    }

    @staticmethod
    async def _get_string(
        client,
        key,
    ):
        value = await get_vars(
            client.me.id,
            key,
        )

        return (
            value
            or STR.DEFAULTS[key]
        )

    @staticmethod
    async def PONG(client):
        return await STR._get_string(
            client,
            "STRING_PONG",
        )

    @staticmethod
    async def OWNER(client):
        return await STR._get_string(
            client,
            "STRING_OWNER",
        )

    @staticmethod
    async def UBOT(client):
        return await STR._get_string(
            client,
            "STRING_UBOT",
        )


# from GooUbot import *

# class STR:
#     async def PONG(client):
#         str_pong = await get_vars(client.me.id, "STRING_PONG")
#         string_pong = str_pong if str_pong else "ᴄʟᴏᴛ"
#         result = f"{string_pong}"
#         return result

#     async def OWNER(client):
#         str_pong = await get_vars(client.me.id, "STRING_OWNER")
#         string_pong = str_pong if str_pong else "ᴏɴᴇʟ"
#         result = f"{string_pong}"
#         return result

#     async def UBOT(client):
#         str_pong = await get_vars(client.me.id, "STRING_UBOT")
#         string_pong = str_pong if str_pong else "ᴜʙᴏᴛ"
#         result = f"{string_pong}"
#         return result
