from dataclasses import asdict

from fastapi import APIRouter, Depends

from src.config import get_settings
from src.api.swagger.report import (
    ReportInterfaceGet,


    ReportOutputGetAll,

)
from src.api.crud_operations.report import ReportOperation

settings = get_settings()
router = APIRouter(
    prefix=settings.report_router,
    tags=settings.report_tag,
)


@router.get("/", **asdict(ReportOutputGetAll()))
async def get_report(
        report: ReportInterfaceGet = Depends()
):
    """
    Returns all report from db by parameters.
    Available to all registered users.
    """
    report_operation = ReportOperation(
        report.db,
        ore_concentrate_id=report.ore_concentrate_id,
        month=report.month,
        year=report.year
    )
    return await report_operation.get_report()

