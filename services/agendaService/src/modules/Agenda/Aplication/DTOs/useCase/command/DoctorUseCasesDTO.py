from dataclasses import dataclass




@dataclass(frozen=True)
class CreateDoctorCommand:
    id_extern: str
    name: str

@dataclass(frozen=True)
class UpdateDoctorCommand:
    id: str
    name: str | None = None
    availability: bool | None = None
    rules: list | None = None

@dataclass(frozen=True)
class DeleteDoctorCommand:
    id: str
