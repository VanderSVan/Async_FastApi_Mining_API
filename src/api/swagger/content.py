from dataclasses import dataclass
from datetime import datetime as dt
from typing import Optional, Type, Any

from fastapi import Query, Path, Body, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.content.base_schemas import (
    ContentGetSchema,
    ContentPatchSchema,
    ContentPostSchema
)
from src.api.schemas.content.response_schemas import (
    ContentResponseDeleteSchema,
    ContentResponsePatchSchema,
    ContentResponsePostSchema
)
from src.api.models.user import UserModel
from src.api.dependencies.db import get_db
from src.api.dependencies.auth import (
    get_current_admin,
    get_current_confirmed_user
)


@dataclass
class ContentInterfaceGetAll:
    ore_concentrate_id: int = Query(..., description="Ore concentrate id")
    from_dt: dt = Query(None, description='Datetime from. (format: 2022-10-01T00:00:00)')
    to_dt: dt = Query(None, description='To datetime. (format: 2022-11-01T00:00:00)')
    iron_percent: float = Query(None, description='Great or equal')
    silicon_percent: float = Query(None, description='Less or equal')
    aluminum_percent: float = Query(None, description='Less or equal')
    calcium_percent: float = Query(None, description='Less or equal')
    sulfur_percent: float = Query(None, description='Less or equal')
    offset: int = Query(None, description='How far to offset')
    limit: int = Query(None, description='How many limit')
    current_confirmed_user: UserModel = Depends(get_current_confirmed_user)
    db: AsyncSession = Depends(get_db)


@dataclass
class ContentInterfaceGet:
    content_id: int = Path(..., ge=1)
    current_confirmed_user: UserModel = Depends(get_current_confirmed_user)
    db: AsyncSession = Depends(get_db)


@dataclass
class ContentInterfaceDelete:
    content_id: int = Path(..., ge=1)
    admin: UserModel = Depends(get_current_admin)
    db: AsyncSession = Depends(get_db)
    

@dataclass
class ContentInterfacePatch:
    content_id: int = Path(..., ge=1)
    data: ContentPatchSchema = Body(..., example={
        "datetime": "2022-10-21T18:00:00",
        "iron_percent": 66.6,
        "silicon_percent": 5.55,
        "aluminum_percent": 0.19,
        "calcium_percent": 0.25,
        "sulfur_percent": 0.05,
        "ore_concentrate_id": 1,
    }
                                    )
    current_confirmed_user: UserModel = Depends(get_current_confirmed_user)
    db: AsyncSession = Depends(get_db)


@dataclass
class ContentInterfacePost:
    data: ContentPostSchema = Body(..., example={
        "datetime": "2022-10-21T18:00:00",
        "iron_percent": 67.385,
        "silicon_percent": 4.789,
        "aluminum_percent": 0.2003,
        "calcium_percent": 0.250005,
        "sulfur_percent": 0.051234,
        "ore_concentrate_id": 1,
    }
                                    )
    current_confirmed_user: UserModel = Depends(get_current_confirmed_user)
    db: AsyncSession = Depends(get_db)


@dataclass
class ContentOutputGetAll:
    summary: Optional[str] = 'Get all ore concentrate content by parameters'
    description: Optional[str] = (
        "**Returns** all ore concentrate content from db by **parameters**.<br />"
        "Available to all **registered users.**"
    )
    response_model: Optional[Type[Any]] = list[ContentGetSchema] | None
    status_code: Optional[int] = status.HTTP_200_OK
    response_description: str = 'List of ore concentrate content'


@dataclass
class ContentOutputGet:
    summary: Optional[str] = 'Get ore concentrate content by content_id'
    description: Optional[str] = (
        "**Returns** ore concentrate content from db by **content id**.<br />"
        "Available to all **registered users.**"
    )
    response_model: Optional[Type[Any]] = ContentGetSchema | None
    status_code: Optional[int] = status.HTTP_200_OK
    response_description: str = 'Content data'


@dataclass
class ContentOutputDelete:
    summary: Optional[str] = 'Delete ore concentrate content by content_id'
    description: Optional[str] = (
        "**Deletes** ore concentrate content from db by **content id**. <br />"
        "Only available to **admins.**"
    )
    response_model: Optional[Type[Any]] = ContentResponseDeleteSchema
    status_code: Optional[int] = status.HTTP_200_OK


@dataclass
class ContentOutputPatch:
    summary: Optional[str] = 'Patch ore concentrate content by content_id'
    description: Optional[str] = (
        "**Updates** ore concentrate content from db by **content id**. <br />"
        "Available to all **registered users.**"
    )
    response_model: Optional[Type[Any]] = ContentResponsePatchSchema
    status_code: Optional[int] = status.HTTP_200_OK


@dataclass
class ContentOutputPost:
    summary: Optional[str] = 'Add new ore concentrate content'
    description: Optional[str] = (
        "**Adds** new ore concentrate content into db. <br />"
        "Available to all **registered users.**"
    )
    response_model: Optional[Type[Any]] = ContentResponsePostSchema
    status_code: Optional[int] = status.HTTP_201_CREATED

