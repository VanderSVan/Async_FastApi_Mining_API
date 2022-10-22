from dataclasses import dataclass
from datetime import datetime as dt

from sqlalchemy import select, and_, func

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.engine.row import Row
from sqlalchemy.sql.selectable import Select

from src.api.models.content import ContentModel
from src.api.crud_operations.utils.report import DateTimeRange
from src.api.schemas.report.base_schemas import ReportGetSchema


@dataclass
class ReportOperation:
    session: AsyncSession
    ore_concentrate_id: int
    month: int
    year: int

    @property
    def _dt_range(self) -> tuple[dt | None, dt | None]:
        return (
            DateTimeRange(self.month, self.year).build()
            if self.month else (None, None)
        )

    async def get_report(self) -> dict[str, list[Row]]:
        output_fields = list(ReportGetSchema.schema()['properties'])
        aggregate_values = [await self._get_aggregate_values(field) for field in output_fields]
        return dict(zip(output_fields, aggregate_values))

    async def _get_aggregate_values(self, desired_attribute_name: str) -> list[Row]:
        query = await self.session.execute(
            self._build_query(desired_attribute_name)
        )
        return query.fetchall()

    def _build_query(self, desired_attribute_name: str) -> Select:
        query = (
            select(func.max(getattr(ContentModel, desired_attribute_name)),
                   func.min(getattr(ContentModel, desired_attribute_name)),
                   func.avg(getattr(ContentModel, desired_attribute_name))
                   ).where(and_(
                                ContentModel.ore_concentrate_id == self.ore_concentrate_id,
                                (ContentModel.datetime >= self._dt_range[0]
                                 if self._dt_range[0] is not None else True),
                                (ContentModel.datetime <= self._dt_range[1]
                                 if self._dt_range[1] is not None else True),
                                )
                           )
        )
        return query
