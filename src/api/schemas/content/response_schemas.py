from pydantic import BaseModel

from src.utils.response_generation.main import get_text


class ContentResponseDeleteSchema(BaseModel):
    message: str = get_text('delete').format('content', 1)


class ContentResponsePatchSchema(BaseModel):
    message: str = get_text('patch').format('content', 1)


class ContentResponsePostSchema(BaseModel):
    message: str = get_text('post').format('content', 1)
