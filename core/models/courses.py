from typing import Union
from pydantic import BaseModel

class Course(BaseModel):
    name: str
    description: Union[str, None] = None
    credit: float

