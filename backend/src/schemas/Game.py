from pydantic import BaseModel, Field
from typing import Optional, List


class GameConsole(BaseModel):
    console_id: int
    name: str
    description: str
    year: int


class GameGenre(BaseModel):
    genre_id: int
    name: str
    description: str


class GameBase(BaseModel):
    game_id: int
    title: str
    description: str
    year: int
    director: str
    images: List[str]
    videos: Optional[List[str]]

    company_id: int

    consoles: Optional[List[GameConsole]] = []
    genres: Optional[List[GameGenre]] = []


class GameCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=50)
    description: str
    year: int = Field(..., gt=0, le=2030)
    director: str = Field(..., min_length=3, max_length=50)
    images: List[str]
    videos: Optional[List[str]]

    company_id: int

    consoles: Optional[List[int]] = []
    genres: Optional[List[int]] = []


class GameUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str]
    year: Optional[int] = Field(None, gt=0, le=2030)
    director: Optional[str] = Field(None, min_length=3, max_length=50)
    images: Optional[List[str]]
    videos: Optional[List[str]]

    company_id: Optional[int]

    consoles: Optional[List[int]] = []
    genres: Optional[List[int]] = []
