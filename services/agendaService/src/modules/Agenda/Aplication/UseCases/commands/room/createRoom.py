from src.modules.agenda.domain.entities.Room import Room
from src.modules.agenda.aplication.dtos.exceptions import CreateUseCaseException
from src.modules.agenda.aplication.events.RoomEvent import CreateRoomEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository.RoomRepositoryPort import RoomRepositoryPort


class CreateRoomUseCase:
    def __init__(self, repository: RoomRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, name: str) -> bool:
        try:
            rules=await self._repository.getGenericRulesRoom()
            room = Room(name=name, rules=rules)
            if isinstance(room,Room):
             await self._repository.save(room) 
             self._bus.emit(CreateRoomEvent(room))
             return True
            return False
        
        except Exception as e:
            raise CreateUseCaseException(
                code="CREATE_ROOM_ERROR",
                message="Error creating room",
                use_case=self.__class__.__name__,
                context={"name": name},
                original=e,
            ) from e
