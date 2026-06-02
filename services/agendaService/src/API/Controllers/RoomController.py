from fastapi import APIRouter, Depends, HTTPException, status

from src.api.provider import (
    get_create_room_use_case,
    get_delete_room_use_case,
    get_list_rooms_query_use_case,
    get_room_by_id_query_use_case,
    get_update_room_use_case,
)
from src.modules.agenda.aplication.dtos.useCase.command.RoomUseCasesDTO import (
    CreateRoomCommand,
    UpdateRoomCommand,
)
from src.modules.agenda.aplication.dtos.useCase.query import GetByIdQuery, ListQuery


routerRoom = APIRouter(prefix="/rooms", tags=["Rooms"])


@routerRoom.post("/", status_code=status.HTTP_201_CREATED)
async def create_room(command: CreateRoomCommand, use_case=Depends(get_create_room_use_case)):
    result = await use_case.execute(command.name)
    return {"created": result}


@routerRoom.get("/{room_id}")
async def get_room(room_id: str, use_case=Depends(get_room_by_id_query_use_case)):
    room = await use_case.execute(GetByIdQuery(id=room_id))
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@routerRoom.get("/")
async def list_rooms(
    limit: int | None = None,
    offset: int = 0,
    use_case=Depends(get_list_rooms_query_use_case),
):
    return await use_case.execute(ListQuery(limit=limit, offset=offset))


@routerRoom.put("/{room_id}")
async def update_room(
    room_id: str,
    command: UpdateRoomCommand,
    use_case=Depends(get_update_room_use_case),
):
    await use_case.execute(command)
    return {"updated": True}


@routerRoom.delete("/{room_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_room(room_id: str, use_case=Depends(get_delete_room_use_case)):
    await use_case.execute(room_id)
