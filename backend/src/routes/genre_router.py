from fastapi import APIRouter, Path, Body
from typing import Optional, List
from src.services.genre_service import GenreService
from src.config.database import SessionLocal

from src.schemas.Genre import GenreCreate, GenreUpdate, GenreBase as Genre

router = APIRouter()

db = SessionLocal()


@router.get("/genre")
def get_all_genres():
    genres = GenreService(db).get_all_genres()
    for genre in genres:
        genre.games
    return genres


@router.get("/genre/{guide_id}")
def get_genre_by_id(genre_id: int = Path(..., gt=0, le=1000)):
    genre = GenreService(db).get_genre_by_id(genre_id)
    genre.games
    return genre


@router.post("/genre")
def create_genre(genre: GenreCreate):
    return GenreService(db).create_genre(genre)


@router.put("/genre/{genre_id}")
def update_genre(genre_id: int, genre: GenreUpdate):
    genre = GenreService(db).update_genre(genre_id, genre)
    if not genre:
        return "Genre not found"
    return genre


@router.delete("/genre/{genre_id}")
def delete_genre(genre_id: int):
    genre = GenreService(db).delete_genre(genre_id)
    if not genre:
        return "Genre not found"
    return genre
