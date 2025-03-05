from fastapi import APIRouter, Depends

from auth.token import get_current_user_id
from queries.user_q import select_user_by_id
from models.user_models import User

user_router = APIRouter(prefix="/user")


@user_router.get("/", response_model=User)
async def get_user(user_id: str = Depends(get_current_user_id)):
    user = await select_user_by_id(user_id)
    return user
