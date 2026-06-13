import pytest
from services.agendaService.src.modules.Agenda.Domain.Entities.agendaEntity import AgendaCreate
from src.modules.Agenda.Aplication.UseCases.createUseCase import CreateAgendaUseCase

class FakeAgendaRepository:
    def __init__(self):
        self.data = []
        self.current_id = 1

    def create(self, agenda):
        agenda_dict = agenda.dict()
        agenda_entity = agenda_dict.copy()
        agenda_entity['id'] = self.current_id
        self.current_id += 1
        self.data.append(agenda_entity)
        return agenda_entity
    
    def list_all(self):
        return self.data
    
    def get_by_id(self, agenda_id):
        for agenda in self.data:
            if agenda['id'] == agenda_id:
                return agenda
        return None
    
    def update(self, agenda_id, agenda):
        for i, item in enumerate(self.data):
            if item['id'] == agenda_id:
                update = {**item, **agenda.dict(exclude_unset=True)}
                self.data[i] = update
                return update
            return None
        
    def delete(self, agenda_id):
        for i, item in enumerate(self.data):
            if item['id'] == agenda_id:
                del self.data[i]
                return True
        return False

    def save(self, agenda):
        self.data.append(agenda)

def test_create_agenda():
    repository = FakeAgendaRepository()
    use_case = CreateAgendaUseCase(repository)

    # Simulando dados de entrada
    agenda = AgendaCreate(
        paciente="João Silva",
        profissional="Dra. Maria Souza",
        data_hora="2024-07-01",
        horario="10:00:00"
        )

    # Executando o caso de uso
    result = repository.create(agenda)

    # Verificando o resultado
    assert result['id'] == 1
    assert result['paciente'] == "João Silva"
    assert result['profissional'] == "Dra. Maria Souza"
    assert result['data_hora'] == "2024-07-01"
    assert result['horario'] == "10:00:00"