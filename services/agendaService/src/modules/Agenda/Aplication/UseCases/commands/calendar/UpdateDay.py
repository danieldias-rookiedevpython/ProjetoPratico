from dataclasses import dataclass
from src.modules.agenda.aplication.dtos.exceptions import UpdateUseCaseException
from src.modules.agenda.aplication.events.CalendarEvent import UpdateDayEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository.CalendarRepositoryPort import CalendarRepositoryPort
from src.modules.agenda.domain.entities import Day


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
