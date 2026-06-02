

from src.modules.agenda.aplication.events.ClinicEvent import DeleteClinicEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import ClinicRepositoryPort


class DeleteClinicUseCase:
    def __init__(self, repository: ClinicRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, clinic: str) -> bool:
        clinic = await self._repository.getClinic(clinic)
        if clinic:
            self._bus.emit(DeleteClinicEvent(str(clinic.id if hasattr(clinic, "id") else clinic)))
            return True
        return False
