from dataclasses import dataclass




@dataclass(frozen=True)
class CreateRoomCommand:
    name: str

@dataclass(frozen=True)
class UpdateRoomCommand:
    id: str
    name: str | None = None
    disponibility: bool | None = None
    rules: list | None = None

@dataclass(frozen=True)
class DeleteRoomCommand:
    id: str
