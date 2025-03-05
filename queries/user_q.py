from typing import Optional

from bson import ObjectId

from db import db
from models.user_models import User, UserCreate


users_collection = db["users"]


async def insert_user(user_data: UserCreate) -> User:
    document = user_data.model_dump()
    await users_collection.insert_one(document)
    new_user = User(**document)
    return new_user


async def select_user_by_email(email: str) -> Optional[User]:
    document = await users_collection.find_one({"email": email})
    if not document:
        return None

    user = User(**document)
    return user

async def select_user_by_id(user_id: str) -> Optional[User]:
    document = await users_collection.find_one({"_id": ObjectId(user_id)})
    if not document:
        return None

    user = User(**document)
    return user
