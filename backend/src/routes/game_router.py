from fastapi import APIRouter, Request
from src.config.database import SessionLocal

from src.services.game_service import GameService
from src.schemas.Game import GameCreate, GameUpdate

from src.controllers.game_controller import GameController

router = APIRouter()

db = SessionLocal()


@router.get("/games")
async def get_all_games(request: Request):
    games = await GameController().get_all_games(request)
    return games


@router.get("/games/{game_id}")
async def get_game_by_id(game_id: int):
    game = GameService(db).get_game_by_id(game_id)
    game.genres
    game.company
    game.consoles
    return game


@router.post("/games")
async def create_game(game: GameCreate):
    game = GameService(db).create_game(game)
    print(game)
    if game is None:
        return "Error creating game"
    return game


@router.put("/games/{game_id}")
async def update_game(game_id: int, game: GameUpdate):
    return GameService(db).update_game(game_id, game)


@router.delete("/games/{game_id}")
async def delete_game(game_id: int):
    game = GameService(db).delete_game(game_id)
    if not game:
        return "Game not found"
    return game


@router.post("/games/add-genre")
async def add_genre_to_game(game_id: int, genre_id: int):
    return GameService(db).add_genre_to_game(game_id, genre_id)
