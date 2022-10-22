from pydantic import BaseModel, Field, constr


class OreConcentrateBaseSchema(BaseModel):
    name: str = Field(..., example='iron')


class OreConcentrateGetSchema(OreConcentrateBaseSchema):
    id: int = Field(..., ge=1)

    class Config:
        orm_mode = True


class OreConcentrateDeleteSchema(OreConcentrateBaseSchema):
    pass


class OreConcentratePatchSchema(OreConcentrateBaseSchema):
    name: constr(to_lower=True) | None = Field(None, example='Copper')


class OreConcentratePostSchema(OreConcentrateBaseSchema):
    name: constr(to_lower=True) = Field(..., example='Aluminum')
