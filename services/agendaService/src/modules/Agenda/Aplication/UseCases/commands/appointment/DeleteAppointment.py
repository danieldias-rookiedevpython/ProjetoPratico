

from src.modules.agenda.aplication.dtos.useCase.command.AppointmentUseCasesDTO import DeleteAppointmentCommand
from src.modules.agenda.aplication.dtos.exceptions import DeleteUseCaseException
from src.modules.agenda.aplication.events.AppointmentEvent import DeleteAppointmentEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import AppointmentRepositoryPort


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
