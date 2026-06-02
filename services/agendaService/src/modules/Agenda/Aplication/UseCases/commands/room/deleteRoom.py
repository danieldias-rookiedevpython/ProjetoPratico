from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.events.RoomEvent import DeleteRoomEvent
from src.modules.agenda.domain.entities.Room import Room
from src.modules.agenda.aplication.ports.repository.RoomRepositoryPort import RoomRepositoryPort

class DeleteRoomUseCase:
    def __init__(self, repository: RoomRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus= bus
    async def execute(self, room_id: str) -> bool:
        try:
            room = await self._repository.getRoom(room_id)
            if not isinstance(room, Room):
                return False
            roomEntity = Room(name = room.name, disponibility = room.disponibility, rules = room.rules)
            
            if(room and roomEntity.delete()):
                await self._repository.deleteRoom(room_id)
                self._bus.emit(DeleteRoomEvent(str(room_id)))
                return True
        
        except Exception as e:
            return False
        return False
       
