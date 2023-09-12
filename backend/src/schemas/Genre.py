from pydantic import BaseModel, Field
from typing import Optional, List

from src.schemas.Game import GameBase as Game


class GenreBase(BaseModel):
    genre_id: int = Field(..., gt=0, le=1000)
    name: str
    description: str

    games: Optional[List[Game]] = []


class GenreCreate(BaseModel):
    name: str
    description: str


class GenreUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
