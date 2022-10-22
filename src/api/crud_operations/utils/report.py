from dataclasses import dataclass
from typing import Literal
from datetime import datetime as dt
from calendar import monthrange


@dataclass
class DateTimeRange:
    month: int
    year: int = None

    def build(self) -> tuple[dt, dt]:
        """
        Returns a tuple containing
        the dt value of the beginning of the month and
        the dt value of the end of the month.
        """
        from_dt: dt = self._build_datetime('start')
        to_dt: dt = self._build_datetime('end')
        return from_dt, to_dt

    def _build_datetime(self, period: Literal['start'] | Literal['end']):
        """
        Builds dt value by parameters
        """
        current_time: dt = dt.now()
        result_year: int = self.year if self.year else current_time.year
        result_month: int = self.month if self.month else current_time.month
        result_day: int = (1 if period == 'start'
                           else monthrange(result_year, result_month)[1])
        result_hour: int = 0 if period == 'start' else 23
        result_minute: int = 0 if period == 'start' else 59
        result_second: int = 0 if period == 'start' else 59
        return dt(year=result_year,
                  month=result_month,
                  day=result_day,
                  hour=result_hour,
                  minute=result_minute,
                  second=result_second)
