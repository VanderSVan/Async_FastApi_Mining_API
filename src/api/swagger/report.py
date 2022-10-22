from dataclasses import dataclass
from typing import Optional, Type, Any

from fastapi import Query, Depends, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.schemas.report.base_schemas import ReportGetSchema

from src.api.models.user import UserModel
from src.api.dependencies.db import get_db
from src.api.dependencies.auth import get_current_confirmed_user


@dataclass
class ReportInterfaceGet:
    ore_concentrate_id: int = Query(..., description="Ore concentrate id")
    month: int = Query(None, description="Month number")
    year: int = Query(None, description="Year number")
    current_confirmed_user: UserModel = Depends(get_current_confirmed_user)
    db: AsyncSession = Depends(get_db)


@dataclass
class ReportOutputGetAll:
    summary: Optional[str] = 'Get a report with max, min and avg ore concentrate values'
    description: Optional[str] = (
        "**Returns** report from db with **max, min and avg ore concentrate values**.<br />"
        "Available to all **registered users.**"
    )
    response_model: Optional[Type[Any]] = ReportGetSchema
    status_code: Optional[int] = status.HTTP_200_OK
    response_description: str = 'Report with max, min and avg ore concentrate values'
