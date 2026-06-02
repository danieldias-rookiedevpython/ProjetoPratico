from dataclasses import dataclass

from src.modules.agenda.domain.entities import Day


@dataclass(frozen=True)
class CreateCalendarEvent:
    days: list[Day]
    year: str


@dataclass(frozen=True)
class UpdateDayEvent:
    day: Day


@dataclass(frozen=True)
class DeleteCalendarEvent:
    year: str
