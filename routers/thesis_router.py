from fastapi import APIRouter, status, Depends, HTTPException

from models.thesis_models import Thesis, ThesisCreate
from queries.thesis_q import insert_thesis, select_theses_by_user_id
from auth.token import get_current_user_id


thesis_router = APIRouter(prefix="/thesis")


@thesis_router.post("/", status_code=status.HTTP_201_CREATED, response_model=Thesis)
async def post_thesis(thesis_data: ThesisCreate, user_id: str = Depends(get_current_user_id)):
    print(thesis_data.user_id)
    print(user_id)
    if thesis_data.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE)
    
    thesis = await insert_thesis(thesis_data)
    return thesis


@thesis_router.get("/user", response_model=list[Thesis])
async def get_user_theses(user_id: str = Depends(get_current_user_id)):
    user_theses = await select_theses_by_user_id(user_id)
    return user_theses
