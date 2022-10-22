from typing import Any
from pydantic import BaseModel, Field


class ReportBaseSchema(BaseModel):
    iron_percent: Any = Field(...)
    silicon_percent: Any = Field(...)
    aluminum_percent: Any = Field(...)
    calcium_percent: Any = Field(...)
    sulfur_percent: Any = Field(...)


class ReportGetSchema(ReportBaseSchema):

    class Config:
        orm_mode = True
