
from dataclasses import dataclass
from src.modules.agenda.domain.entities import Day, Doctor, Room
from src.modules.agenda.domain.entities.Appointment import Appointment
from src.modules.agenda.domain.entities.Patient import Patient
from src.modules.agenda.domain.entities.Room import Room
from src.modules.agenda.domain.valueObjects import Hour
from src.modules.agenda.domain.valueObjects.AppointmentType import AppointmentType


    
@dataclass(frozen=True)
class AppointmentSchedulingOutputDTO:
    doctor: Doctor
    day: Day
    patient: Patient
    room: list[Room]
    appointments: list[Appointment]
    type: AppointmentType
    time: Hour
