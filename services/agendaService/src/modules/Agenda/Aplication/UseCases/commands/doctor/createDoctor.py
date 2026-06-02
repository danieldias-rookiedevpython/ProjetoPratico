
from src.modules.agenda.aplication.dtos.useCase.command.DoctorUseCasesDTO import CreateDoctorCommand
from src.modules.agenda.aplication.dtos.exceptions import CreateUseCaseException
from src.modules.agenda.aplication.events.DoctorEvent import CreateDoctorEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository import DoctorRepositoryPort
from src.modules.agenda.domain.entities import Doctor



class CreateDoctorUseCase:
    
    def __init__(self, repository:DoctorRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, data:CreateDoctorCommand):
      try:
        basicRules = await self._repository.GetDoctorGenericRules()
        doctor = Doctor(name=data.name, id=data.id_extern, rules=basicRules)
        
        if isinstance(doctor, Doctor):
            await self._repository.save(doctor)
            self._bus.emit(CreateDoctorEvent(doctor))
            return True
        
      except Exception as e:
        raise CreateUseCaseException(
            code="CREATE_DOCTOR_ERROR",
            message="Error creating doctor",
            use_case=self.__class__.__name__,
            context={"command": data.model_dump() if hasattr(data, "model_dump") else str(data)},
            original=e,
        ) from e
