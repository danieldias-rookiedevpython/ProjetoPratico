from typing import Any

from src.modules.agenda.aplication.dtos.useCase.query import GetByIdQuery, ListDaysQuery, ListQuery
from src.modules.agenda.aplication.ports.repository.querys import (
    AppointmentQueryRepositoryPort,
    CalendarQueryRepositoryPort,
    ClinicQueryRepositoryPort,
    DoctorQueryRepositoryPort,
    EntityQueryRepositoryPort,
    PatientQueryRepositoryPort,
    RoomQueryRepositoryPort,
    RuleQueryRepositoryPort,
)


class GetEntityByIdUseCase:
    def __init__(self, repository: EntityQueryRepositoryPort):
        self._repository = repository

    async def execute(self, query: GetByIdQuery) -> Any:
        return await self._repository.get_by_id(query.id)


class ListEntitiesUseCase:
    def __init__(self, repository: EntityQueryRepositoryPort):
        self._repository = repository

    async def execute(self, query: ListQuery | None = None) -> list[Any]:
        return await self._repository.list(query or ListQuery())


class GetAppointmentByIdUseCase(GetEntityByIdUseCase):
    def __init__(self, repository: AppointmentQueryRepositoryPort):
        super().__init__(repository)


class ListAppointmentsUseCase(ListEntitiesUseCase):
    def __init__(self, repository: AppointmentQueryRepositoryPort):
        super().__init__(repository)


class GetClinicByIdUseCase(GetEntityByIdUseCase):
    def __init__(self, repository: ClinicQueryRepositoryPort):
        super().__init__(repository)


class ListClinicsUseCase(ListEntitiesUseCase):
    def __init__(self, repository: ClinicQueryRepositoryPort):
        super().__init__(repository)


class GetDoctorByIdUseCase(GetEntityByIdUseCase):
    def __init__(self, repository: DoctorQueryRepositoryPort):
        super().__init__(repository)


class ListDoctorsUseCase(ListEntitiesUseCase):
    def __init__(self, repository: DoctorQueryRepositoryPort):
        super().__init__(repository)


class GetPatientByIdUseCase(GetEntityByIdUseCase):
    def __init__(self, repository: PatientQueryRepositoryPort):
        super().__init__(repository)


class ListPatientsUseCase(ListEntitiesUseCase):
    def __init__(self, repository: PatientQueryRepositoryPort):
        super().__init__(repository)


class GetRoomByIdUseCase(GetEntityByIdUseCase):
    def __init__(self, repository: RoomQueryRepositoryPort):
        super().__init__(repository)


class ListRoomsUseCase(ListEntitiesUseCase):
    def __init__(self, repository: RoomQueryRepositoryPort):
        super().__init__(repository)


class GetRuleByIdUseCase(GetEntityByIdUseCase):
    def __init__(self, repository: RuleQueryRepositoryPort):
        super().__init__(repository)


class ListRulesUseCase(ListEntitiesUseCase):
    def __init__(self, repository: RuleQueryRepositoryPort):
        super().__init__(repository)


class GetDayByIdUseCase:
    def __init__(self, repository: CalendarQueryRepositoryPort):
        self._repository = repository

    async def execute(self, query: GetByIdQuery) -> Any:
        return await self._repository.get_by_id(query.id)


class ListDaysUseCase:
    def __init__(self, repository: CalendarQueryRepositoryPort):
        self._repository = repository

    async def execute(self, query: ListDaysQuery | None = None) -> list[Any]:
        return await self._repository.list(query or ListDaysQuery())
