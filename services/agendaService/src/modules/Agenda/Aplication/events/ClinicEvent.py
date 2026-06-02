from dataclasses import dataclass

from src.modules.agenda.domain.entities import Clinic


@dataclass(frozen=True)
class CreateClinicEvent:
    clinic: Clinic


@dataclass(frozen=True)
class UpdateClinicEvent:
    clinic: Clinic


@dataclass(frozen=True)
class DeleteClinicEvent:
    clinic_id: str
