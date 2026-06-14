import pytest
from services.agendaService.src.modules.Agenda.Domain.Entities.agendaEntity import AgendaCreate

class FakeAgendaRepository:
    def __init__(self):
        self.data = []
        self.current_id = 1

    def create(self, agenda):
        agenda_dict = agenda.dict()
        agenda_entity = agenda_dict.copy()
        agenda_entity["id"] = self.current_id
        self.current_id += 1
        self.data.append(agenda_entity)
        return agenda_entity

    def list_all(self):
        return self.data

    def get_by_id(self, agenda_id):
        for agenda in self.data:
            if agenda["id"] == agenda_id:
                return agenda
        return None

    def update(self, agenda_id, agenda):
        for i, item in enumerate(self.data):
            if item["id"] == agenda_id:
                updated = {**item, **agenda.dict(exclude_unset=True)}
                self.data[i] = updated
                return updated
        return None

    def delete(self, agenda_id):
        for i, item in enumerate(self.data):
            if item["id"] == agenda_id:
                del self.data[i]
                return True
        return False
    
def test_update_agenda():
    repository = FakeAgendaRepository()

    # Criando uma agenda
    created = repository.create(AgendaCreate(paciente="João Silva", profissional="Dra. Maria Souza", data_hora="2024-07-01", horario="10:00:00"))

    # Atualizando a agenda
    updated_data = AgendaCreate(paciente="João Silva", profissional="Dra. Maria Souza", data_hora="2024-07-01", horario="11:00:00")

    result = repository.update(created["id"], updated_data)

    # Verificando o resultado
    assert result is not None
    assert result["id"] == created["id"]
    assert result["data_hora"] == "2024-07-01"