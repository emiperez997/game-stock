from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgresql://emi:admin@localhost:5432/play_pulse"
# SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://root:root@localhost:3306/games_test"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
