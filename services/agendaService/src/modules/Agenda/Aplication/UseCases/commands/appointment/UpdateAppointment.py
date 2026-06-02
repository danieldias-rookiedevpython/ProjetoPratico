from src.modules.agenda.aplication.dtos.useCase.command.AppointmentUseCasesDTO import UpdateAppointmentCommand
from src.modules.agenda.aplication.dtos.exceptions import UpdateUseCaseException
from src.modules.agenda.aplication.events.AppointmentEvent import UpdateAppointmentEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import AppointmentRepositoryPort
from src.modules.agenda.domain.entities import Appointment


class UpdateAppointmentUseCase:
    def __init__(self, repository: AppointmentRepositoryPort, bus: BusPort):
        self._repository = repository
        self.bus = bus
        
    async def execute(self, command:UpdateAppointmentCommand):
        
       try:
           appointment = await self._repository.getAppointment(id=command.id)
        
           if isinstance(appointment, Appointment):
                await self._repository.save(appointment)
                self.bus.emit(UpdateAppointmentEvent(appointment))
                return True
           return False
    
       except Exception as e:
            raise UpdateUseCaseException(
                code="UPDATE_APPOINTMENT_ERROR",
                message="Error updating appointment",
                use_case=self.__class__.__name__,
                context={"appointment_id": command.id},
                original=e,
            ) from e
        
