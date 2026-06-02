
from src.modules.agenda.aplication.events.PatientEvent import CreatePatientEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import PatientRepositoryPort
from src.modules.agenda.aplication.dtos.useCase.command.PatientUseCasesDTO import CreatePatientCommand
from src.modules.agenda.domain.entities.Patient import Patient


class CreatePatientUseCase:
    def __init__(self, repository: PatientRepositoryPort, bus: BusPort):
        self.repository = repository
        self._bus = bus
    
    async def execute(self, command: CreatePatientCommand) -> bool:
       
       try:
            pacient = Patient(id=command.id, name=command.name)
            
            await self.repository.save(pacient)
            self._bus.emit(CreatePatientEvent(pacient))
            
            return True 
            
       except Exception as e:
            return False
