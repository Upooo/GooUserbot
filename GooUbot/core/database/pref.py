from GooUbot.core.database import mongodb

prefix_collection = mongodb["prefix"]
async def get_pref(user_id: int):
    pref = await prefix_collection.find_one({"_id": user_id})
    return pref.get("prefixesi") if pref else "."

async def set_pref(user_id: int, prefix: str):
    await prefix_collection.update_one(
        {"_id": user_id}, {"$set": {"prefixesi": prefix}}, upsert=True
    )

async def rem_pref(user_id: int):
    await prefix_collection.update_one(
        {"_id": user_id}, {"$unset": {"prefixesi": ""}}, upsert=True
    )
