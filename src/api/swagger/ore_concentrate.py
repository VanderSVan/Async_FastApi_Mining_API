from dataclasses import dataclass
from typing import Optional, Type, Any

from fastapi import Query, Path, Body, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.ore_concentrate.base_schemas import (
    OreConcentrateGetSchema,
    OreConcentratePatchSchema,
    OreConcentratePostSchema
)
from src.api.schemas.ore_concentrate.response_schemas import (
    OreConcentrateResponseDeleteSchema,
    OreConcentrateResponsePatchSchema,
    OreConcentrateResponsePostSchema
)
from src.api.models.user import UserModel
from src.api.dependencies.db import get_db
from src.api.dependencies.auth import (
    get_current_admin,
    get_current_confirmed_user
)


@dataclass
class OreConcentrateInterfaceGetAll:
    name: str = Query(default=None, description='Ore concentrate name')
    offset: int = Query(default=None, description='How far to offset')
    limit: int = Query(default=None, description='How many limit')
    current_confirmed_user: UserModel = Depends(get_current_confirmed_user)
    db: AsyncSession = Depends(get_db)
    

@dataclass
class OreConcentrateInterfaceGet:
    ore_concentrate_id: int = Path(..., ge=1)
    current_confirmed_user: UserModel = Depends(get_current_confirmed_user)
    db: AsyncSession = Depends(get_db)


@dataclass
class OreConcentrateInterfaceDelete:
    ore_concentrate_id: int = Path(..., ge=1)
    admin: UserModel = Depends(get_current_admin)
    db: AsyncSession = Depends(get_db)


@dataclass
class OreConcentrateInterfacePatch:
    ore_concentrate_id: int = Path(..., ge=1)
    data: OreConcentratePatchSchema = Body(..., example={'name': 'Copper'})
    admin: UserModel = Depends(get_current_admin)
    db: AsyncSession = Depends(get_db)


@dataclass
class OreConcentrateInterfacePost:
    data: OreConcentratePostSchema = Body(..., example={'name': 'Aluminum'})
    admin: UserModel = Depends(get_current_admin)
    db: AsyncSession = Depends(get_db)


@dataclass
class OreConcentrateOutputGetAll:
    summary: Optional[str] = 'Get all ore concentrates by parameters'
    description: Optional[str] = (
        "**Returns** all ore concentrates from db by **parameters**.<br />"
        "Available to all **registered users.**"
    )
    response_model: Optional[Type[Any]] = list[OreConcentrateGetSchema] | None
    status_code: Optional[int] = status.HTTP_200_OK
    response_description: str = 'List of ore concentrates'


@dataclass
class OreConcentrateOutputGet:
    summary: Optional[str] = 'Get ore concentrate by ore_concentrate.id'
    description: Optional[str] = (
        "**Returns** ore concentrate from db by **ore_concentrate.id**.<br />"
        "Available to all **registered users.**"
    )
    response_model: Optional[Type[Any]] = OreConcentrateGetSchema | None
    status_code: Optional[int] = status.HTTP_200_OK
    response_description: str = 'Ore concentrate data'


@dataclass
class OreConcentrateOutputDelete:
    summary: Optional[str] = 'Delete ore concentrate by ore_concentrate.id'
    description: Optional[str] = (
        "**Deletes** ore concentrate from db by **ore_concentrate.id**. <br />"
        "Only available to **admins.**"
    )
    response_model: Optional[Type[Any]] = OreConcentrateResponseDeleteSchema
    status_code: Optional[int] = status.HTTP_200_OK


@dataclass
class OreConcentrateOutputPatch:
    summary: Optional[str] = 'Patch ore concentrate by ore_concentrate id'
    description: Optional[str] = (
        "**Updates** ore concentrate from db by **ore_concentrate.id**. <br />"
        "Only available to **admins.**"
    )
    response_model: Optional[Type[Any]] = OreConcentrateResponsePatchSchema
    status_code: Optional[int] = status.HTTP_200_OK


@dataclass
class OreConcentrateOutputPost:
    summary: Optional[str] = 'Add new ore concentrate'
    description: Optional[str] = (
        "**Adds** new ore concentrate into db. <br />"
        "Only available to **admins.**"
    )
    response_model: Optional[Type[Any]] = OreConcentrateResponsePostSchema
    status_code: Optional[int] = status.HTTP_201_CREATED
