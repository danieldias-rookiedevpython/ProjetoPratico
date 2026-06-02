



from src.modules.agenda.aplication.dtos.useCase.command.DoctorUseCasesDTO import UpdateDoctorCommand
from src.modules.agenda.aplication.events.DoctorEvent import UpdateDoctorEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import DoctorRepositoryPort


class UpdateDoctorUseCase:
    
    def __init__(self, repository:DoctorRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, data:UpdateDoctorCommand):
        
        doctor = await self._repository.get(data)
        
        if doctor:
            self._bus.emit(UpdateDoctorEvent(doctor))
            return True
        
        return None
