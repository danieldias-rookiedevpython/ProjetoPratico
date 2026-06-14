from services.agendaService.src.modules.Consulta.Agenda.Domain.Entities.agendaEntity import Agenda


class UseCasesAgenda:
    def __init__(self):
        pass

    def create_agendamento(self, name: str):
        agenda = Agenda(id=IdAgenda(), name=name)
        # Lógica para criar um agendamento
        return {"message": f"Agendamento criado para {name}"}