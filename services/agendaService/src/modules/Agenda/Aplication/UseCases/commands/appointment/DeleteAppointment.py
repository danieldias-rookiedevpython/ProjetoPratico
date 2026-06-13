

from src.modules.Agenda.Aplication.DTOs.useCase.command.AppointmentUseCasesDTO import DeleteAppointmentCommand
from src.modules.Agenda.Aplication.DTOs.exceptions import DeleteUseCaseException
from src.modules.Agenda.Aplication.events.AppointmentEvent import DeleteAppointmentEvent
from src.modules.Agenda.Aplication.Ports.events.BusPort import BusPort
from src.modules.Agenda.Aplication.Ports.repository import AppointmentRepositoryPort


class DeleteAppointmentUseCase:
    def __init__(self, repository: AppointmentRepositoryPort, bus: BusPort):
        self._repository = repository
        self.bus = bus
        
    async def execute(self, command: DeleteAppointmentCommand):
        try:
            await self._repository.delete(command.id)
            self.bus.emit(DeleteAppointmentEvent(command.id))
            return True
        except Exception as e:
            raise DeleteUseCaseException(
                code="DELETE_APPOINTMENT_ERROR",
                message="Error deleting appointment",
                use_case=self.__class__.__name__,
                context={"appointment_id": command.id},
                original=e,
            ) from e

