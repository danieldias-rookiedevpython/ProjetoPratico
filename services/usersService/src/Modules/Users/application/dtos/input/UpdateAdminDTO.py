from dataclasses import dataclass


@dataclass(frozen=True)
class UpdateAdminDTO:
    id: int
    userName: str | None = None
    email: str | None = None
    name: str | None = None
    password: str | None = None
