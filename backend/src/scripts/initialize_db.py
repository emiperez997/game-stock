from src.models.company_model import Company
from src.models.game_model import Game
from src.models.genre_model import Genre
from src.models.console_model import Console

# Many to many relations
from src.models.game_genre_model import GameGenre
from src.models.game_console_model import GameConsole

from src.config.database import engine, Base


def initialize_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    try:
        initialize_db()
        print("Database initialized")
    except:
        print("Database already initialized")
