from src.models.game_genre_model import GameGenre as GenreGameModel

from src.schemas.GameGenre import GameGenreBase


class GenreGameService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_game_genres(self):
        return self.db.query(GenreGameModel).all()

    def get_game_genre_by_id(self, game_id: int, genre_id: int):
        return self.db.query(GenreGameModel).filter(GenreGameModel.game_id == game_id, GenreGameModel.genre_id == genre_id).first()

    def create_game_genre(self, game_genre: GameGenreBase):
        db_game_genre = GenreGameModel(**game_genre.dict())
        self.db.add(db_game_genre)
        self.db.commit()
        self.db.refresh(db_game_genre)
        return db_game_genre

    def delete_game_genre(self, game_id: int, genre_id: int):
        db_game_genre = self.db.query(GenreGameModel).filter(
            GenreGameModel.game_id == game_id, GenreGameModel.genre_id == genre_id).first()
        if db_game_genre is None:
            return None
        self.db.delete(db_game_genre)
        self.db.commit()
        return db_game_genre
