from typing import Optional

from bson import ObjectId

from db import db
from models.thesis_models import Thesis, ThesisCreate


theses_collection = db["theses"]


async def insert_thesis(thesis_data: ThesisCreate) -> Thesis:
    document = thesis_data.model_dump()
    await theses_collection.insert_one(document)
    new_thesis = Thesis(**document)
    return new_thesis


async def select_theses_by_user_id(user_id: str) -> list[Thesis]:
    documents = theses_collection.find({"user_id": user_id})
    theses = [Thesis(**doc) async for doc in documents]
    return theses


async def select_thesis_by_id(thesis_id: str) -> Optional[Thesis]:
    document = await theses_collection.find_one({"_id": ObjectId(thesis_id)})
    if not document:
        return None

    thesis = Thesis(**document)
    return thesis
