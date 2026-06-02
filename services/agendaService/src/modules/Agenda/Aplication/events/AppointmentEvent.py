from dataclasses import dataclass

from src.modules.agenda.domain.entities import Appointment


@dataclass(frozen=True)
class CreateAppointmentEvent:
    appointment: Appointment


@dataclass(frozen=True)
class UpdateAppointmentEvent:
    appointment: Appointment


@dataclass(frozen=True)
class DeleteAppointmentEvent:
    appointment_id: str


@dataclass(frozen=True)
class CancelAppointmentEvent:
    appointment_id: str
