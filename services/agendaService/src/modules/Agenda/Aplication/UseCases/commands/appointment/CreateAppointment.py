from src.modules.Agenda.Aplication.DTOs.exceptions import CreateUseCaseException
from src.modules.Agenda.Aplication.DTOs.repositorys.input import AppointmentSchedulingInputDTO
from src.modules.Agenda.Aplication.events.AppointmentEvent import CreateAppointmentEvent
from src.modules.Agenda.Aplication.Ports.events.BusPort import BusPort
from src.modules.Agenda.Aplication.Ports.repository.AppointmentRepositoryPort import AppointmentRepositoryPort
from src.modules.Agenda.Aplication.Ports.repository.AppointmentSchedulingRepositoryPort import AppointmentSchedulingRepositoryPort
from src.modules.Agenda.Aplication.DTOs.useCase.command.AppointmentUseCasesDTO import CreateAppointmentCommand
from src.modules.Agenda.Domain.Entities import Appointment


class CreateAppointmentUseCase:
    def __init__(self, repositoryAppointment: AppointmentRepositoryPort, repositorySchedulingContext: AppointmentSchedulingRepositoryPort, bus: BusPort):
        self._repositoryAppointment = repositoryAppointment
        self._repositorySchedulingContext = repositorySchedulingContext
        self._bus = bus
        
    async def execute(self, command:CreateAppointmentCommand):
        try:
            
            
            context = await self._repositorySchedulingContext.getContext(
                AppointmentSchedulingInputDTO(
                    date=command.date, 
                    weekday=command.weekday, 
                    doctor=command.doctor, 
                    patient=command.patient, 
                    room=command.room,
                    time=command.time,
                    type=command.type,
                )
            )
            
            appointment = Appointment.create(
                patient=context.patient,
                doctor=context.doctor,
                rooms=context.room,
                day=context.day,
                time=context.time,
                type=context.type
            )
           
            if isinstance(appointment, Appointment):
                await self._repositoryAppointment.save(appointment, command.scheduler_id)
                self._bus.emit(CreateAppointmentEvent(appointment))
                return True
            
            
        except Exception as e:
            raise CreateUseCaseException(
                code="CREATE_APPOINTMENT_ERROR",
                message="Error creating appointment",
                use_case=self.__class__.__name__,
                context={"command": command.model_dump() if hasattr(command, "model_dump") else str(command)},
                original=e,
            ) from e
      
    

