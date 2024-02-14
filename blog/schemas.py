from pydantic import BaseModel
from typing import List



class Blog(BaseModel):
    title:str
    content:str


