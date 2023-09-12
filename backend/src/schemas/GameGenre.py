from pydantic import BaseModel, Field
from typing import Optional, List


class GameGenreBase(BaseModel):
    game_id: int
    genre_id: int
