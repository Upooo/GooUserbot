from GooUbot.core.database import mongodb

ubot_collection = mongodb["Goo"]
async def add_ubot(user_id: int, api_id: int, api_hash: str, session_string: str):
    return await ubot_collection.update_one(
        {"user_id": user_id},
        {
            "$set": {
                "api_id": api_id,
                "api_hash": api_hash,
                "session_string": session_string,
            }
        },
        upsert=True,
    )

async def remove_ubot(user_id: int):
    return await ubot_collection.delete_one({"user_id": user_id})

async def get_userbots():
    data = []
    async for ubot in ubot_collection.find({"user_id": {"$exists": 1}}):
        data.append({
            "name": str(ubot.get("user_id")),
            "api_id": ubot.get("api_id"),
            "api_hash": ubot.get("api_hash"),
            "session_string": ubot.get("session_string"),
        })
    return data

# async def get_userbots():
#     return [
#         {
#             "name": str(ubot["user_id"]),
#             "api_id": ubot["api_id"],
#             "api_hash": ubot["api_hash"],
#             "session_string": ubot["session_string"],
#         }
#         async for ubot in ubot_collection.find({"user_id": {"$exists": 1}})
#     ]
