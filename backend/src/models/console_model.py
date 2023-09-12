from sqlalchemy import *
from sqlalchemy.orm import relationship

from src.config.database import Base


class Console(Base):
    __tablename__ = "consoles"

    console_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    year = Column(Integer)

    games = relationship("Game", secondary="game_consoles",
                         back_populates="consoles")
