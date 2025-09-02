from typing import List, Optional, Union
from GooUbot.core.database import mongodb

vars_collection = mongodb["varsX"]
# === Fungsi Dasar ===
async def set_vars(user_id: int, vars_name: str, value: Union[int, str], query: str = "vars") -> None:
    await vars_collection.update_one(
        {"_id": user_id},
        {"$set": {f"{query}.{vars_name}": value}},
        upsert=True,
    )

async def get_vars(user_id: int, vars_name: str, query: str = "vars") -> Optional[Union[int, str]]:
    result = await vars_collection.find_one({"_id": user_id})
    return result.get(query, {}).get(vars_name) if result else None

async def remove_vars(user_id: int, vars_name: str, query: str = "vars") -> None:
    await vars_collection.update_one(
        {"_id": user_id},
        {"$unset": {f"{query}.{vars_name}": ""}},
    )

async def all_vars(user_id: int, query: str = "vars") -> Optional[dict]:
    result = await vars_collection.find_one({"_id": user_id})
    return result.get(query) if result else None

async def remove_all_vars(user_id: int) -> None:
    await vars_collection.delete_one({"_id": user_id})

# === Fungsi List-Based ===
async def get_list_from_vars(user_id: int, vars_name: str, query: str = "vars") -> List[int]:
    vars_data = await get_vars(user_id, vars_name, query)
    return [int(x) for x in str(vars_data).split()] if vars_data else []

async def add_to_vars(user_id: int, vars_name: str, value: int, query: str = "vars") -> None:
    vars_list = await get_list_from_vars(user_id, vars_name, query)
    if value not in vars_list:
        vars_list.append(value)
    await set_vars(user_id, vars_name, " ".join(map(str, vars_list)), query)

async def remove_from_vars(user_id: int, vars_name: str, value: int, query: str = "vars") -> None:
    vars_list = await get_list_from_vars(user_id, vars_name, query)
    if value in vars_list:
        vars_list.remove(value)
        await set_vars(user_id, vars_name, " ".join(map(str, vars_list)), query)

# === Fungsi PM Permit ===
async def get_pm_id(user_id: int) -> List[int]:
    pm_id = await get_vars(user_id, "PM_PERMIT")
    return [int(x) for x in str(pm_id).split()] if pm_id else []

async def add_pm_id(me_id: int, user_id: int) -> None:
    pm_id = await get_vars(me_id, "PM_PERMIT")
    list_ids = set(str(pm_id).split() if pm_id else [])
    list_ids.add(str(user_id))
    await set_vars(me_id, "PM_PERMIT", " ".join(list_ids))

async def remove_pm_id(me_id: int, user_id: int) -> None:
    pm_id = await get_vars(me_id, "PM_PERMIT")
    if pm_id:
        list_ids = [x for x in str(pm_id).split() if x != str(user_id)]
        await set_vars(me_id, "PM_PERMIT", " ".join(list_ids))

# === Fungsi Status ===
async def set_status(user_id: int, status: Union[bool, str]) -> None:
    await set_vars(user_id, "WORD_DETECTION_STATUS", status)

async def get_status(user_id: int) -> Union[bool, str]:
    status = await get_vars(user_id, "WORD_DETECTION_STATUS")
    return status if status is not None else False
