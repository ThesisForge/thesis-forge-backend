# from typing import Optional

from pydantic import BaseModel, EmailStr

from models.common import MongoId


class UserBase(BaseModel):
    first_name: str
    last_name: str 
    email: EmailStr
    # password: Optional[str]


class UserCreate(UserBase):
    pass


class User(UserBase, MongoId):
    pass
