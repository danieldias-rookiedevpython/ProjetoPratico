
from abc import ABC, abstractmethod

from src.modules.Agenda.Aplication.DTOs.repositorys.input.AppointmentSchedulingInputDTO import AppointmentSchedulingInputDTO
from src.modules.Agenda.Aplication.DTOs.repositorys.output.AppointmentSchedulingOutputDTO import AppointmentSchedulingOutputDTO

class AppointmentSchedulingRepositoryPort (ABC):
   
    @abstractmethod
    async def getContext(self, appointmentScheduling: AppointmentSchedulingInputDTO) -> AppointmentSchedulingOutputDTO:
       pass
   

