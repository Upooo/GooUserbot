from GooUbot.core.database import mongodb

user_expired_collection = mongodb["users"]
async def get_expired_date(user_id: int):
    user = await user_expired_collection.find_one({"_id": user_id})
    return user.get("expire_date") if user else None

async def set_expired_date(user_id: int, expire_date: int):
    await user_expired_collection.update_one(
        {"_id": user_id}, {"$set": {"expire_date": expire_date}}, upsert=True
    )

async def rem_expired_date(user_id: int):
    await user_expired_collection.update_one(
        {"_id": user_id}, {"$unset": {"expire_date": ""}}, upsert=True
    )
