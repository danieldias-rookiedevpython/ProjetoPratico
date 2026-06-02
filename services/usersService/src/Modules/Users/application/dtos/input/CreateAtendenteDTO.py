from dataclasses import dataclass


@dataclass(frozen=True)
class CreateAtendenteDTO:
    userName: str
    email: str
    name: str
    password: str
