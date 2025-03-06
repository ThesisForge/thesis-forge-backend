from typing import Optional

from pydantic import BaseModel

from models.common import MongoId


class ThesisBase(BaseModel):
    topic_name: str
    main_area: str
    secondary_area: Optional[str]
    personal_interest: int
    business_potential: int
    open_source_contribution: int
    scientific_value: int
    topic_description: str
    external_links: Optional[str] = None
    user_id: Optional[str] = None


class ThesisCreate(ThesisBase):
    pass


class Thesis(ThesisBase, MongoId):
    pass
