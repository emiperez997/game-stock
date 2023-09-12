from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from src.config.database import Base


class Game(Base):
    __tablename__ = "games"

    game_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, unique=True, index=True, nullable=False)
    description = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    director = Column(String, nullable=False)
    images = Column(ARRAY(String), nullable=False)
    videos = Column(ARRAY(String), nullable=True)

    company_id = Column(Integer, ForeignKey("companies.company_id"))

    # Relation many to one with Company
    company = relationship("Company", back_populates="games")

    # Relation many to many with Genre
    genres = relationship("Genre", secondary="game_genres",
                          back_populates="games")
    consoles = relationship("Console", secondary="game_consoles",
                            back_populates="games")
