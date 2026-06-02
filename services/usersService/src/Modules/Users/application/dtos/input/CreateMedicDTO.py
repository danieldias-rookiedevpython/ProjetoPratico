from dataclasses import dataclass


@dataclass(frozen=True)
class CreateMedicDTO:
    userName: str
    email: str
    name: str
    password: str
