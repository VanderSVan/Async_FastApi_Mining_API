from sqlalchemy import Column, Integer, String

from src.db.db_sqlalchemy import BaseModel


class OreConcentrate(BaseModel):
    __tablename__ = 'ore_concentrates'

    id = Column(Integer, primary_key=True)
    name = Column(String(length=100), unique=True)
