from sqlalchemy import *
from sqlalchemy.orm import relationship

from src.config.database import Base


class GameConsole(Base):
    __tablename__ = "game_consoles"

    game_id = Column(Integer, ForeignKey("games.game_id"), primary_key=True)
    console_id = Column(Integer, ForeignKey(
        "consoles.console_id"), primary_key=True)
