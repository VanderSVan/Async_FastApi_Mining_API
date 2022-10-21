from datetime import datetime as dt

from pydantic import BaseModel, Field, condecimal


class ContentBaseSchema(BaseModel):
    datetime: dt = Field(..., example=dt.utcnow().strftime('%Y-%m-%dT%H:%M:%S'))
    iron_percent: condecimal(decimal_places=6) = Field(..., example=66.6)
    silicon_percent: condecimal(decimal_places=6) = Field(..., example=5.55)
    aluminum_percent: condecimal(decimal_places=6) = Field(..., example=0.19)
    calcium_percent: condecimal(decimal_places=6) = Field(..., example=0.25)
    sulfur_percent: condecimal(decimal_places=6) = Field(..., example=0.05)
    ore_concentrate_id: int = Field(..., ge=1)


class ContentGetSchema(ContentBaseSchema):
    id: int = Field(..., ge=1)

    class Config:
        orm_mode = True


class ContentDeleteSchema(ContentBaseSchema):
    pass


class ContentPatchSchema(ContentBaseSchema):
    datetime: dt | None = Field(None, example=dt.utcnow().strftime('%Y-%m-%dT%H:%M:%S'))
    iron_percent: condecimal(decimal_places=6) | None = Field(None, example=67.385)
    silicon_percent: condecimal(decimal_places=6) | None = Field(None, example=4.789)
    aluminum_percent: condecimal(decimal_places=6) | None = Field(None, example=0.2003)
    calcium_percent: condecimal(decimal_places=6) | None = Field(None, example=0.250005)
    sulfur_percent: condecimal(decimal_places=6) | None = Field(None, example=0.051234)
    ore_concentrate_id: int | None = Field(None, ge=1)


class ContentPostSchema(ContentBaseSchema):
    pass
