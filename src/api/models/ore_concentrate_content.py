from sqlalchemy import Column, Integer, Numeric, DateTime, ForeignKey

from src.db.db_sqlalchemy import BaseModel


class OreConcentrateContentModel(BaseModel):
    __tablename__ = 'ore_concentrate_contents'

    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime)
    iron_percent = Column(Numeric(scale=6))
    silicon_percent = Column(Numeric(scale=6))
    aluminum_percent = Column(Numeric(scale=6))
    calcium_percent = Column(Numeric(scale=6))
    sulfur_percent = Column(Numeric(scale=6))

    ore_concentrate_id = Column(
        Integer, ForeignKey('ore_concentrates.id',
                            onupdate='CASCADE',
                            ondelete='CASCADE')
    )
