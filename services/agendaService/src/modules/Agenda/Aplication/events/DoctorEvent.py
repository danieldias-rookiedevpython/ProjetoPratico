from dataclasses import dataclass

from src.modules.Agenda.Domain.Entities import Doctor


@dataclass(frozen=True)
class CreateDoctorEvent:
    doctor: Doctor


@dataclass(frozen=True)
class UpdateDoctorEvent:
    doctor: Doctor


@dataclass(frozen=True)
class DeleteDoctorEvent:
    doctor_id: str

