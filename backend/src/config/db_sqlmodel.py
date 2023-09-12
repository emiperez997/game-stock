from sqlmodel import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://emi:admin@localhost:5432/games_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)
