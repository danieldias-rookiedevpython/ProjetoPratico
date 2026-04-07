from src.modules.Agenda.Domain.Repository.IAgendaRepository import IAgendaRepository
from src.modules.Agenda.Domain.Entities.AgendaEntity import AgendaEntity

class CreateAgendaUseCase:

    def __init__(self, repository: IAgendaRepository):
        self.repository = repository

    def execute(self, data: AgendaCreateDTO) -> AgendaEntity:
        # Lógica para criar uma agenda
        if not data:
            raise ValueError("Data is required")
        
        new_agenda = AgendaEntity(id=None, name=data.name)
        self.repository.save(new_agenda)
        return new_agenda