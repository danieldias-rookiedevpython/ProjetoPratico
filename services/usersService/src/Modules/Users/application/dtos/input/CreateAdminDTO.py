from dataclasses import dataclass


@dataclass(frozen=True)
class CreateAdminDTO:
    userName: str
    email: str
    name: str
    password: str
