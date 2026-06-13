from src.modules.Agenda.Aplication.DTOs.exceptions import DeleteUseCaseException
from src.modules.Agenda.Aplication.events.CalendarEvent import DeleteCalendarEvent
from src.modules.Agenda.Aplication.Ports.repository.CalendarRepositoryPort import CalendarRepositoryPort


class DeleteCalendarUseCase:
    def __init__(self, repository: CalendarRepositoryPort, bus=None):
        self._repository = repository
        self.bus = bus
    
    async def execute(self, ano:str) -> bool:
        try:
            await self._repository.delete(ano) 
            if self.bus:
                self.bus.emit(DeleteCalendarEvent(str(ano)))
            return True
        except Exception as e:
            raise DeleteUseCaseException(
                code="DELETE_CALENDAR_ERROR",
                message="Error deleting calendar",
                use_case=self.__class__.__name__,
                context={"year": ano},
                original=e,
            ) from e

