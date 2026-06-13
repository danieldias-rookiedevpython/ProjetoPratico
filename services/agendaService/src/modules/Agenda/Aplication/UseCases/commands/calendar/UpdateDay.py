from dataclasses import dataclass
from src.modules.Agenda.Aplication.DTOs.exceptions import UpdateUseCaseException
from src.modules.Agenda.Aplication.events.CalendarEvent import UpdateDayEvent
from src.modules.Agenda.Aplication.Ports.events.BusPort import BusPort
from src.modules.Agenda.Aplication.Ports.repository.CalendarRepositoryPort import CalendarRepositoryPort
from src.modules.Agenda.Domain.Entities import Day


@dataclass(frozen=True)
class UpdateDayCommand:
    id: str
    data: dict


class UpdateDayUseCase:
    def __init__(self, repository: CalendarRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, command: UpdateDayCommand):
        try:
            data = await self._repository.get(command.id)
            if not isinstance(data, Day):
                return False
            day = data
            dayUpdated = day.update(command.data)
            await self._repository.updateDay(dayUpdated)
            self._bus.emit(UpdateDayEvent(dayUpdated))
            return True
        except Exception as e:
            raise UpdateUseCaseException(
                code="UPDATE_DAY_ERROR",
                message="Error updating calendar day",
                use_case=self.__class__.__name__,
                context={"command": str(command)},
                original=e,
            ) from e

