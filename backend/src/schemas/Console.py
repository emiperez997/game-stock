from pydantic import BaseModel, Field
from typing import Optional, List

from src.schemas.Game import GameBase


class ConsoleBase(BaseModel):
    console_id: int
    name: str
    description: str
    year: int

    games: Optional[List[GameBase]] = []


class ConsoleCreate(BaseModel):
    name: str
    description: str
    year: int


class ConsoleUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    year: Optional[int]
