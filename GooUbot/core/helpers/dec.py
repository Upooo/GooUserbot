import asyncio

from pyrogram.enums import (
    ChatType,
)

from GooUbot import ubot


PRIVATE_CHAT_TYPES = {
    ChatType.PRIVATE,
}

GROUP_CHAT_TYPES = {
    ChatType.GROUP,
    ChatType.SUPERGROUP,
}


async def get_private_and_group_chats(
    client,
):
    private_chats = []
    group_chats = []

    try:
        async for dialog in (
            client.get_dialogs()
        ):
            chat_type = (
                dialog.chat.type
            )

            if (
                chat_type
                in PRIVATE_CHAT_TYPES
            ):
                private_chats.append(
                    dialog.chat.id
                )

            elif (
                chat_type
                in GROUP_CHAT_TYPES
            ):
                group_chats.append(
                    dialog.chat.id
                )

    except Exception as e:
        print(
            "[ERROR] "
            f"Failed getting dialogs "
            f"for {client.me.id}: "
            f"{e}"
        )

    return (
        private_chats,
        group_chats,
    )


async def install_my_peer(
    client,
):
    private_chats, group_chats = (
        await get_private_and_group_chats(
            client
        )
    )

    client_id = client.me.id

    client._get_my_peer[
        client_id
    ] = {
        "pm": private_chats,
        "gc": group_chats,
    }


async def installPeer():

    tasks = [
        install_my_peer(client)
        for client in ubot._ubot
    ]

    results = await asyncio.gather(
        *tasks,
        return_exceptions=True,
    )

    for client, result in zip(
        ubot._ubot,
        results,
    ):
        if isinstance(
            result,
            Exception,
        ):
            print(
                "[ERROR] "
                f"install_my_peer "
                f"failed for "
                f"{client.me.id}: "
                f"{result}"
            )

# import asyncio
# from pyrogram.enums import ChatType
# from GooUbot import *
# from GooUbot import ubot

# chat_type = {
#     "group": [ChatType.GROUP, ChatType.SUPERGROUP],
#     "users": [ChatType.PRIVATE],
# }

# async def get_private_and_group_chats(client):
#     pm_chats = []
#     gc_chats = []

#     async for dialog in client.get_dialogs(limit=None):
#         try:
#             if dialog.chat.type in chat_type.get("users"):
#                 pm_chats.append(dialog.chat.id)
#             elif dialog.chat.type in chat_type.get("group"):
#                 gc_chats.append(dialog.chat.id)
#         except Exception as e:
#             print(f"[INFO]: {e}")

#     return pm_chats, gc_chats


# async def install_my_peer(client):
#     pm_chats, gc_chats = await get_private_and_group_chats(client)
#     client_id = client.me.id
#     client._get_my_peer[client_id] = {"pm": pm_chats, "gc": gc_chats}


# async def installPeer():
#     tasks = [install_my_peer(client) for client in ubot._ubot]
#     await asyncio.gather(*tasks, return_exceptions=True)



