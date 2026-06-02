from dataclasses import dataclass


@dataclass(frozen=True)
class CreatePacientDTO:
    userName: str
    email: str
    name: str
    password: str
