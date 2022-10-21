from dataclasses import asdict

from fastapi import APIRouter, Depends, status
from fastapi.responses import ORJSONResponse

from src.config import get_settings
from src.api.models.content import ContentModel
from src.api.swagger.content import (
    ContentInterfaceGetAll,
    ContentInterfaceGet,
    ContentInterfaceDelete,
    ContentInterfacePatch,
    ContentInterfacePost,

    ContentOutputGetAll,
    ContentOutputGet,
    ContentOutputDelete,
    ContentOutputPatch,
    ContentOutputPost
)
from src.api.crud_operations.content import ContentOperation
from src.utils.response_generation.main import get_text

settings = get_settings()
router = APIRouter(
    prefix=settings.content_router,
    tags=settings.content_tag,
)


@router.get("/", **asdict(ContentOutputGetAll()))
async def get_all_content(
        content: ContentInterfaceGetAll = Depends()
) -> list[ContentModel] | list[None]:
    """
    Returns all content from db by parameters.
    Available to all registered users.
    """
    crud = ContentOperation(content.db)
    return await crud.find_all_by_params(
        from_dt=content.from_dt,
        to_dt=content.to_dt,
        iron=content.iron_percent,
        silicon=content.silicon_percent,
        aluminum=content.aluminum_percent,
        calcium=content.calcium_percent,
        sulfur=content.sulfur_percent,
        ore_concentrate_id=content.ore_concentrate_id,
        offset=content.offset,
        limit=content.limit
    )


@router.get("/{content_id}", **asdict(ContentOutputGet()))
async def get_content(
        content: ContentInterfaceGet = Depends()
) -> ContentModel | None:
    """
    Returns one content from db by content id.
    Available to all registered users.
    """
    crud = ContentOperation(content.db)
    return await crud.find_by_id(content.content_id)


@router.delete("/{content_id}", **asdict(ContentOutputDelete()))
async def delete_content(
        content: ContentInterfaceDelete = Depends()
) -> ORJSONResponse:
    """
    Deletes content from db by content id.
    Only available to admins.
    """
    crud = ContentOperation(content.db)
    await crud.delete_obj(content.content_id)

    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": get_text('delete').format(
                crud.model_name, content.content_id
            )
        }
    )


@router.patch("/{content_id}", **asdict(ContentOutputPatch()))
async def patch_content(
        content: ContentInterfacePatch = Depends()
) -> ORJSONResponse:
    """
    Updates content data.
    Only available to admins.
    """
    crud = ContentOperation(content.db)
    await crud.patch_obj(content.content_id, content.data)

    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": get_text('patch').format(
                crud.model_name, content.content_id
            )
        }
    )


@router.post("/create", **asdict(ContentOutputPost()))
async def add_content(
        content: ContentInterfacePost = Depends()
) -> ORJSONResponse:
    """
    Adds new content into db.
    Only available to admins.
    """
    crud = ContentOperation(content.db)
    await crud.add_obj(content.data)

    return ORJSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": get_text('post').format(crud.model_name)
        }
    )
