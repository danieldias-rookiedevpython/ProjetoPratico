




from src.modules.agenda.aplication.events.PatientEvent import DeletePatientEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import PatientRepositoryPort


class DeletePatientUseCase:
    def __init__(self, repository: PatientRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, id: str):
        try:
            
            pacient = await self._repository.getPacient(id)
            if not pacient:
                return False
            
            await self._repository.delete(id)
            self._bus.emit(DeletePatientEvent(id))
            return True
            
        except Exception as e:
            return False
