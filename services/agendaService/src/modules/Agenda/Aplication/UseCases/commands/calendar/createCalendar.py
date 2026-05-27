from src.Modules.Agenda.Domain.Entities.calendar import Calendar 
from src.Modules.Agenda.Aplication.Ports.Repository.IAgendaRepository import IAgendaRepository
from src.Modules.Agenda.Aplication.Ports.Repository.ICalendarData import ICalendarData
from src.Modules.Agenda.Aplication.DTOs.output.calendar.createCalendarResponse import ResponseCreateCalendarDTO


class CreateCalendar:
    
    def __init__(self, repository: IAgendaRepository, baseData: ICalendarData
):
        self._repository = repository
        self._baseData = baseData

    def execute(self, calandaryCommand: dict):
       data = self._baseData.pullData(calandaryCommand['ano'])
       policys: list[int]
       try:
           policys = self._repository.findAllPolicys()
       except Exception as e:
             raise Exception("=: " + str(e))
         
       policys = PolicyToDomainMapper.map(policys)
        
       calendar = Calendar(policys)

       action = calendar.createSlots(data)
       responseDays = [ResponseCreateCalendarDTO]
       
       if action == True:
           try:
               days= calendar.getCalendar()
               self._repository.create(days)
               
               for day in days:
                     response = ResponseCreateCalendarDTO()
                     response.id = day.id
                     response.availability = day.isAvailable
                     response.weekDay = day.weekday
                     response.date = day.date
                     
                     responseDays.append(response)
                   
           except Exception as e:
               raise Exception("Erro ao criar calendário: " + str(e))
           
           
           
       
           
       return {"days": responseDays}
   
       
    