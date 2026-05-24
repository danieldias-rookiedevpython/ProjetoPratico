from src.Modules.Agenda.Aplication.DTOs.output.calendar.createCalendarResponse import ResponseCreateCalendarDTO
from src.Modules.Agenda.Domain.Entities.slot import Slot


class CreateCalendarMapper:
    def __init__(self, repository):
        self._repository = repository

    def toDTO(self, data: list[Slot]) -> list[ResponseCreateCalendarDTO]:
        responseElements = []
        for element in data:
                     response = ResponseCreateCalendarDTO()
                     response.id = element.id
                     response.availability = element.isAvailable
                     response.weekDay = element.weekelement
                     response.date = element.date
                     
                     responseElements.append(response)
           
        return ResponseCreateCalendarDTO(data)