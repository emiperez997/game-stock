from sqlalchemy import *
from sqlalchemy.orm import relationship

from src.config.database import Base


class GameGenre(Base):
    __tablename__ = "game_genres"

    game_id = Column(Integer, ForeignKey("games.game_id"), primary_key=True)
    genre_id = Column(Integer, ForeignKey("genres.genre_id"), primary_key=True)
