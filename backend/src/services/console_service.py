from src.models.console_model import Console as ConsoleModel

from src.schemas.Console import ConsoleCreate, ConsoleUpdate


class ConsoleService():

    def __init__(self, db) -> None:
        self.db = db

    def get_all_consoles(self):
        return self.db.query(ConsoleModel).all()

    def get_console_by_id(self, console_id: int):
        return self.db.query(ConsoleModel).filter(ConsoleModel.console_id == console_id).first()

    def count_consoles(self):
        return self.db.query(ConsoleModel).count()

    def create_console(self, console: ConsoleCreate):
        db_console = ConsoleModel(**console.dict())
        self.db.add(db_console)
        self.db.commit()
        self.db.refresh(db_console)
        return db_console

    def update_console(self, console_id: int, console: ConsoleUpdate):
        db_console = self.db.query(ConsoleModel).filter(
            ConsoleModel.console_id == console_id).first()
        db_console.name = console.name if console.name else db_console.name
        self.db.commit()
        self.db.refresh(db_console)
        return db_console

    def delete_console(self, console_id: int):
        db_console = self.db.query(ConsoleModel).filter(
            ConsoleModel.console_id == console_id).first()
        if db_console is None:
            return None
        self.db.delete(db_console)
        self.db.commit()
        return db_console
