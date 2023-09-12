from src.models.genre_model import Genre as GenreModel

from src.schemas.Genre import GenreCreate, GenreUpdate


class GenreService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_genres(self):
        return self.db.query(GenreModel).all()

    def get_genre_by_id(self, genre_id: int):
        return self.db.query(GenreModel).filter(GenreModel.genre_id == genre_id).first()

    def create_genre(self, genre: GenreCreate):
        db_genre = GenreModel(**genre.dict())
        self.db.add(db_genre)
        self.db.commit()
        self.db.refresh(db_genre)
        return db_genre

    def update_genre(self, genre_id: int, genre: GenreUpdate):
        db_genre = self.db.query(GenreModel).filter(
            GenreModel.genre_id == genre_id).first()
        db_genre.name = genre.name if genre.name else db_genre.name
        db_genre.description = genre.description if genre.description else db_genre.description
        self.db.commit()
        self.db.refresh(db_genre)
        return db_genre

    def delete_genre(self, genre_id: int):
        db_genre = self.db.query(GenreModel).filter(
            GenreModel.genre_id == genre_id).first()
        if db_genre is None:
            return None
        self.db.delete(db_genre)
        self.db.commit()
        return db_genre
