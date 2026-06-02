from calendar import monthrange
from datetime import date

from src.modules.agenda.domain.valueObjects import Date, DayStatus


class CalendarDataClient:
    def pullData(self):
        return []

    async def mont(self, mes: int | str, ano: int | str) -> list[dict]:
        month = int(mes)
        year = int(ano)
        total_days = monthrange(year, month)[1]
        return [
            {
                "rooms": [],
                "date": Date(day=day, month=month, year=year),
                "weekday": date(year, month, day).weekday(),
                "availability": True,
                "status": DayStatus.AVAILABLE,
                "rules": [],
            }
            for day in range(1, total_days + 1)
        ]
