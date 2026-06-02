from dataclasses import dataclass




@dataclass(frozen=True)
class CreatePatientCommand:
    id: str
    name: str

@dataclass(frozen=True)
class UpdatePatientCommand:
    id: str
    name: str | None = None

@dataclass(frozen=True)
class DeletePatientCommand:
    id: str
