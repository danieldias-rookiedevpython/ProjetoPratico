from typing import List, Optional
from src.modules.Agenda.Domain.Entities.AgendaEntity import (
    AgendaCreate,
    AgendaEntity,
    AgendaUpdate,
)
from src.modules.Agenda.Repository.AgendaRepository import AgendaRepository


class AgendaRepository(AgendaRepository):
    def __init__(self):
        self.agendas = []
        self.counter = 1

    def create(self, agenda: AgendaCreate) -> AgendaEntity:
        new_agenda = AgendaEntity(id=self.counter, **agenda.dict())
        self.agendas.append(new_agenda)
        self.counter += 1
        return new_agenda

    def list_all(self) -> List[AgendaEntity]:
        return self.agendas

    def get_by_id(self, agenda_id: int) -> Optional[AgendaEntity]:
        for agenda in self.agendas:
            if agenda.id == agenda_id:
                return agenda
        return None

    def update(self, agenda_id: int, agenda: AgendaUpdate) -> Optional[AgendaEntity]:
        existing = self.get_by_id(agenda_id)
        if not existing:
            return None

        updated_data = agenda.dict(exclude_unset=True)
        for key, value in updated_data.items():
            setattr(existing, key, value)

        return existing

    def delete(self, agenda_id: int) -> bool:
        existing = self.get_by_id(agenda_id)
        if not existing:
            return False

        self.agendas.remove(existing)
        return True