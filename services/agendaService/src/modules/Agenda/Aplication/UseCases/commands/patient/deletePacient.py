




from src.modules.Agenda.Aplication.events.PatientEvent import DeletePatientEvent
from src.modules.Agenda.Aplication.Ports.events.BusPort import BusPort
from src.modules.Agenda.Aplication.Ports.repository import PatientRepositoryPort


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

