from dataclasses import dataclass, field




@dataclass(frozen=True)
class CreateClinicCommand:
    name: str
    rules: list = field(default_factory=list)

@dataclass(frozen=True)
class UpdateClinicCommand:
    id: str
    name: str | None = None
    rules: list | None = None

@dataclass(frozen=True)
class DeleteClinicCommand:
    id: str
