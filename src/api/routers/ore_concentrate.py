from dataclasses import asdict

from fastapi import APIRouter, Depends, status
from fastapi.responses import ORJSONResponse

from src.config import get_settings
from src.api.models.ore_concentrate import OreConcentrateModel
from src.api.swagger.ore_concentrate import (
    OreConcentrateInterfaceGetAll,
    OreConcentrateInterfaceGet,
    OreConcentrateInterfaceDelete,
    OreConcentrateInterfacePatch,
    OreConcentrateInterfacePost,

    OreConcentrateOutputGetAll,
    OreConcentrateOutputGet,
    OreConcentrateOutputDelete,
    OreConcentrateOutputPatch,
    OreConcentrateOutputPost
)
from src.api.crud_operations.ore_concentrate import OreConcentrateOperation
from src.utils.response_generation.main import get_text

settings = get_settings()
router = APIRouter(
    prefix=settings.ore_concentrate_router,
    tags=settings.ore_concentrate_tag,
)


@router.get("/", **asdict(OreConcentrateOutputGetAll()))
async def get_all_ore_concentrates(
        ore_concentrate: OreConcentrateInterfaceGetAll = Depends()
) -> list[OreConcentrateModel]:
    """
    Returns all ore_concentrates from db by parameters.
    Available to all registered users.
    """
    crud = OreConcentrateOperation(ore_concentrate.db)

    if ore_concentrate.name:
        ore_concentrate: OreConcentrateModel = (
            await crud.find_by_param('name', ore_concentrate.name.lower())
        )
        return [ore_concentrate]

    return await crud.find_all(offset=ore_concentrate.offset,
                               limit=ore_concentrate.limit)


@router.get("/{ore_concentrate_id}", **asdict(OreConcentrateOutputGet()))
async def get_ore_concentrate(
        ore_concentrate: OreConcentrateInterfaceGet = Depends()
) -> OreConcentrateModel | None:
    """
    Returns one ore_concentrate from db by ore_concentrate id.
    Available to all registered users.
    """
    crud = OreConcentrateOperation(ore_concentrate.db)
    return await crud.find_by_id(ore_concentrate.ore_concentrate_id)


@router.delete("/{ore_concentrate_id}", **asdict(OreConcentrateOutputDelete()))
async def delete_ore_concentrate(
        ore_concentrate: OreConcentrateInterfaceDelete = Depends()
) -> ORJSONResponse:
    """
    Deletes ore_concentrate from db by ore_concentrate id.
    Only available to admins.
    """
    crud = OreConcentrateOperation(ore_concentrate.db)
    await crud.delete_obj(ore_concentrate.ore_concentrate_id)

    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": get_text('delete').format(
                crud.model_name, ore_concentrate.ore_concentrate_id
            )
        }
    )


@router.patch("/{ore_concentrate_id}", **asdict(OreConcentrateOutputPatch()))
async def patch_ore_concentrate(
        ore_concentrate: OreConcentrateInterfacePatch = Depends()
) -> ORJSONResponse:
    """
    Updates ore_concentrate data.
    Only available to admins.
    """
    crud = OreConcentrateOperation(ore_concentrate.db)
    await crud.patch_obj(ore_concentrate.ore_concentrate_id, ore_concentrate.data)

    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "message": get_text('patch').format(
                crud.model_name, ore_concentrate.ore_concentrate_id
            )
        }
    )


@router.post("/create", **asdict(OreConcentrateOutputPost()))
async def add_ore_concentrate(
        ore_concentrate: OreConcentrateInterfacePost = Depends()
) -> ORJSONResponse:
    """
    Adds new ore_concentrate into db.
    Only available to admins.
    """
    crud = OreConcentrateOperation(ore_concentrate.db)
    await crud.add_obj(ore_concentrate.data)

    return ORJSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            "message": get_text('post').format(crud.model_name)
        }
    )

