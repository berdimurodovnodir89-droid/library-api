from typing import List
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field, field_validator


class GenreResponse(BaseModel):
    id: int = Field(gt=0)
    name: str
    description: str = None

    model_config = ConfigDict(from_attributes=True)
