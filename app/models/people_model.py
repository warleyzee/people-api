from pydantic import BaseModel
from typing import Optional, List


class PersonStats(BaseModel):
    oldest: List[str]
    youngest: List[str]
    avg_age: Optional[int]


class InvalidAgesResponse(BaseModel):
    invalid_names: List[str]
