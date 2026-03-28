from typing import List
from datetime import datetime

from pydantic import BaseModel, ConfigDict


class AuthorResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    bio: str = ""
    born_date: datetime | None = None

    model_config = ConfigDict(from_attributes=True)


class AuthorsResponse(BaseModel):
    limit: int = 20
    skip: int = 0
    search: str = ""
    count: int
    result: List[AuthorResponse]
