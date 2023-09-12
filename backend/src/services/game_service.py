from src.models.game_model import Game as GameModel
from src.models.game_console_model import GameConsole as GameConsoleModel

from src.schemas.Game import GameCreate, GameUpdate

from src.services.company_service import CompanyService
from src.services.genre_service import GenreService
from src.services.genre_game_service import GenreGameService
from src.services.game_console_service import GameConsoleService
from src.services.console_service import ConsoleService


from sqlalchemy import text


class GameService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_games(self, order_by: str, order: str, limit: int, offset: int):
        return self.db.query(GameModel).order_by(text(order_by + " " + order)).limit(limit).offset(offset).all()

    def get_game_by_id(self, game_id: int):
        return self.db.query(GameModel).filter(GameModel.game_id == game_id).first()

    def count_games(self):
        return self.db.query(GameModel).count()

    def create_game(self, game: GameCreate):
        company = CompanyService(self.db).get_company_by_id(game.company_id)
        if not company:
            return None

        consolesDB = []
        genresDB = []

        for console_id in game.consoles:
            console = ConsoleService(self.db).get_console_by_id(console_id)
            if not console:
                return None
            consolesDB.append(console)

        for genre_id in game.genres:
            genre = GenreService(self.db).get_genre_by_id(genre_id)
            if not genre:
                return None
            genresDB.append(genre)

        game.consoles = consolesDB
        game.genres = genresDB

        db_game = GameModel(**game.dict())
        self.db.add(db_game)
        self.db.commit()
        self.db.refresh(db_game)
        return db_game

    def update_game(self, game_id: int, game: GameUpdate):
        db_game = self.db.query(GameModel).filter(
            GameModel.game_id == game_id).first()
        db_game.title = game.title if game.title else db_game.title
        db_game.year = game.year if game.year else db_game.year
        db_game.consoles = game.consoles if game.consoles else db_game.consoles
        db_game.director = game.director if game.director else db_game.director
        db_game.chapters = game.chapters if game.chapters else db_game.chapters
        self.db.commit()
        self.db.refresh(db_game)
        return db_game

    def delete_game(self, game_id: int):
        db_game = self.db.query(GameModel).filter(
            GameModel.game_id == game_id).first()
        if db_game is None:
            return None
        self.db.delete(db_game)
        self.db.commit()
        return db_game

    def add_genre_to_game(self, game_id: int, genre_id: int):
        game = self.db.query(GameModel).filter(
            GameModel.game_id == game_id).first()
        genre = GenreService(self.db).get_genre_by_id(genre_id)
        if not genre or not game:
            return None

        game.genres.append(genre)
        self.db.commit()
        self.db.refresh(game)
        return game
