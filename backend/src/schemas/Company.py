from pydantic import BaseModel, Field
from typing import Optional, List


class CompanyGame(BaseModel):
    game_id: int
    title: str
    description: str
    year: int
    director: str
    images: List[str]
    videos: Optional[List[str]]


class CompanyBase(BaseModel):
    company_id: int
    name: str
    foundation_year: int
    country: str

    games: Optional[List[CompanyGame]] = []


class CompanyCreate(BaseModel):
    name: str
    foundation_year: int
    country: str


class CompanyUpdate(BaseModel):
    name: Optional[str]
    foundation_year: Optional[int]
    country: Optional[str]
