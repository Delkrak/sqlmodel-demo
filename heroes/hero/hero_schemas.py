from pydantic import BaseModel
from typing import Optional


class HeroBase(BaseModel):
    name: str
    secret_name: str
    age: Optional[int] = None


class HeroCreate(HeroBase):
    pass


class HeroPublic(HeroBase):
    id: int


class HeroUpdate(BaseModel):
    name: Optional[str] = None
    secret_name: Optional[str] = None
    age: Optional[int] = None
