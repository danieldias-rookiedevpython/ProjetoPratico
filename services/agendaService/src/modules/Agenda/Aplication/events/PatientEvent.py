from dataclasses import dataclass

from src.modules.agenda.domain.entities import Patient


@dataclass(frozen=True)
class CreatePatientEvent:
    patient: Patient


@dataclass(frozen=True)
class DeletePatientEvent:
    patient_id: str
