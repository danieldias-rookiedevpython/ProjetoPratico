import IAgendaRepository from "../../Domain/Repository/iAgendaRepository"
import AgendaEntity from "../../Domain/Entities/agendaEntity"

class CreateAgendaUseCase:

    def __init__(self, repository: IAgendaRepository):
        self.repository = repository
        self.agenda = AgendaEntity()

    def execute(self, name: str):
        # Lógica para criar uma agenda
        new_agenda = {"name": name}
        self.repository.save(new_agenda)
        return new_agenda