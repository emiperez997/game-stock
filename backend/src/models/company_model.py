from sqlalchemy import *
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import ARRAY

from src.config.database import Base


class Company(Base):
    __tablename__ = "companies"

    company_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    foundation_year = Column(Integer, nullable=False)
    country = Column(String, nullable=False)

    games = relationship("Game", back_populates="company")
