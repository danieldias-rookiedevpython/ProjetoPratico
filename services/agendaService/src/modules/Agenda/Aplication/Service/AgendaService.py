from typing import List, Optional
from src.modules.Agenda.Domain.Entities.AgendaEntity import (
    AgendaCreate,
    AgendaEntity,
    AgendaUpdate,
)
from src.modules.Agenda.Repository.AgendaRepository import AgendaRepository


class AgendaService:
    def __init__(self, repository: AgendaRepository):
        self.repository = repository

    def create(self, agenda: AgendaCreate) -> AgendaEntity:
        return self.repository.create(agenda)

    def list_all(self) -> List[AgendaEntity]:
        return self.repository.list_all()

    def get_by_id(self, agenda_id: int) -> Optional[AgendaEntity]:
        return self.repository.get_by_id(agenda_id)

    def update(self, agenda_id: int, agenda: AgendaUpdate) -> Optional[AgendaEntity]:
        return self.repository.update(agenda_id, agenda)

    def delete(self, agenda_id: int) -> bool:
        return self.repository.delete(agenda_id)