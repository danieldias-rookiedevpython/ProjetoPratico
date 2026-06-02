from dataclasses import dataclass

from src.modules.agenda.domain.entities import Room


@dataclass(frozen=True)
class CreateRoomEvent:
    room: Room


@dataclass(frozen=True)
class UpdateRoomEvent:
    room: Room


@dataclass(frozen=True)
class DeleteRoomEvent:
    room_id: str
