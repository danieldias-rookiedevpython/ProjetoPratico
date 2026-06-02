from abc import ABC, abstractmethod
from typing import Any

from src.modules.agenda.aplication.dtos.useCase.query import ListDaysQuery, ListQuery


class EntityQueryRepositoryPort(ABC):
    @abstractmethod
    async def get_by_id(self, entity_id: str) -> Any:
        pass

    @abstractmethod
    async def list(self, query: ListQuery) -> list[Any]:
        pass


class AppointmentQueryRepositoryPort(EntityQueryRepositoryPort):
    pass


class ClinicQueryRepositoryPort(EntityQueryRepositoryPort):
    pass


class DoctorQueryRepositoryPort(EntityQueryRepositoryPort):
    pass


class PatientQueryRepositoryPort(EntityQueryRepositoryPort):
    pass


class RoomQueryRepositoryPort(EntityQueryRepositoryPort):
    pass


class RuleQueryRepositoryPort(EntityQueryRepositoryPort):
    pass


class CalendarQueryRepositoryPort(ABC):
    @abstractmethod
    async def get_by_id(self, day_id: str) -> Any:
        pass

    @abstractmethod
    async def list(self, query: ListDaysQuery) -> list[Any]:
        pass
