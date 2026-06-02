
from src.modules.agenda.aplication.dtos.useCase.command.RoomUseCasesDTO import UpdateRoomCommand
from src.modules.agenda.aplication.events.RoomEvent import UpdateRoomEvent
from src.modules.agenda.aplication.ports.events.BusPort import BusPort
from src.modules.agenda.aplication.ports.repository.RoomRepositoryPort import RoomRepositoryPort


class UpdateRoomUseCase:
    def __init__(self, repository: RoomRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus= bus
    
    async def execute(self, Imput:UpdateRoomCommand) -> bool:
         room = await self._repository.getRoom(Imput.id)
         if not isinstance(room, object) or not hasattr(room, "updateStateRoom"):
             return False
         roomUpdated = room.updateStateRoom(Imput)
         
         if(roomUpdated and await self._repository.update(roomUpdated)):
             self._bus.emit(UpdateRoomEvent(roomUpdated))
             return True
         
         return False
