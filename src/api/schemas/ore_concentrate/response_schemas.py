from pydantic import BaseModel

from src.utils.response_generation.main import get_text


class OreConcentrateResponseDeleteSchema(BaseModel):
    message: str = get_text('delete').format('ore_concentrate', 1)


class OreConcentrateResponsePatchSchema(BaseModel):
    message: str = get_text('patch').format('ore_concentrate', 1)


class OreConcentrateResponsePostSchema(BaseModel):
    message: str = get_text('post').format('ore_concentrate', 1)
