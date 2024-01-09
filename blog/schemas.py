from pydantic import BaseModel
from typing import List



class Blog(BaseModel):
    title:str
    content:str
    tags: List[str] = []
    published_by:str | None = None


