



from src.modules.Agenda.Aplication.DTOs.useCase.command.ClinicUseCasesDTO import CreateClinicCommand
from src.modules.Agenda.Aplication.DTOs.exceptions import CreateUseCaseException
from src.modules.Agenda.Aplication.events.ClinicEvent import CreateClinicEvent
from src.modules.Agenda.Aplication.Ports.events.BusPort import BusPort
from src.modules.Agenda.Aplication.Ports.repository import ClinicRepositoryPort
from src.modules.Agenda.Domain.Entities import Clinic


class CreateClinicUseCase:
    
    def __init__(self, repository: ClinicRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
    
    async def execute(self, command:CreateClinicCommand):
        # Lógica para criar um administrador
        try:
         clinic = Clinic(name=command.name, rules=command.rules)
         await self._repository.save(clinic)
         self._bus.emit(CreateClinicEvent(clinic))
        except Exception as e:
            raise CreateUseCaseException(
                code="CREATE_CLINIC_ERROR",
                message="Error creating clinic",
                use_case=self.__class__.__name__,
                context={"command": command.model_dump() if hasattr(command, "model_dump") else str(command)},
                original=e,
            ) from e
        return True

