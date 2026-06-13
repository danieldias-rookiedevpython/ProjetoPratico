from src.modules.Agenda.Aplication.Ports.events.BusPort import BusPort
from src.modules.Agenda.Aplication.Ports.repository import AppointmentRepositoryPort
from src.modules.Agenda.Domain.ValueObjects import AppointmentType
from src.modules.Agenda.Aplication.DTOs.useCase.command.AppointmentUseCasesDTO import CreateAppointmentTypeCommand
from src.modules.Agenda.Aplication.DTOs.exceptions import CreateUseCaseException

class CreateAppointmentTypeUseCase:
    def __init__(self, repository: AppointmentRepositoryPort, bus: BusPort ):
        self._repository = repository
        self.bus = bus
        
    async def execute(self, command: CreateAppointmentTypeCommand):
         
         type =AppointmentType(
            name=command.name,
            duration=command.duration,
            description=command.description
        )
         
         if isinstance(type, AppointmentType):
            await self._repository.saveType(type)
            self.bus.publish()
            return True
        
         raise CreateUseCaseException(
            code="CREATE_APPOINTMENT_TYPE_ERROR",
            message="Error creating appointment type",
            use_case=self.__class__.__name__,
            context={"command": command.model_dump() if hasattr(command, "model_dump") else str(command)},
         )

