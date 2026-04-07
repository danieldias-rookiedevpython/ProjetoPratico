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
    
    def save(self, agenda):
        self.data.append(agenda)

def test_list_all():
    repository = FakeAgendaRepository()

    # Criando algumas agendas
    repository.create(AgendaCreate(paciente="João Silva", profissional="Dra. Maria Souza", data_hora="2024-07-01T10:00:00", horario="10:00"))
    repository.create(AgendaCreate(paciente="Ana Pereira", profissional="Dr. Carlos Lima", data_hora="2024-07-01T11:00:00", horario="11:00"))

     # Listando todas as agendas
    result = repository.list_all()

     # Verificando o resultado
    assert len(result) == 2
    assert result[0]["paciente"] == "João Silva"
    assert result[1]["paciente"] == "Ana Pereira"