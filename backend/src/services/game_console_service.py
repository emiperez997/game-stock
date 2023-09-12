from src.models.game_console_model import GameConsole as GameConsoleModel


class GameConsoleService():

    def __init__(self, db) -> None:
        self.db = db

    def create_game_console(self, game_id: int, console_id: int):
        db_game_console = GameConsoleModel(
            game_id=game_id, console_id=console_id)
        self.db.add(db_game_console)
        self.db.commit()
        self.db.refresh(db_game_console)
        return db_game_console

    def delete_game_console(self, game_id: int, console_id: int):
        db_game_console = self.db.query(GameConsoleModel).filter(
            GameConsoleModel.game_id == game_id, GameConsoleModel.console_id == console_id).first()
        if db_game_console is None:
            return None
        self.db.delete(db_game_console)
        self.db.commit()
        return db_game_console
