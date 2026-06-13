
from dataclasses import dataclass
from src.modules.Agenda.Domain.Entities import Day, Doctor, Room
from src.modules.Agenda.Domain.Entities.Appointment import Appointment
from src.modules.Agenda.Domain.Entities.Patient import Patient
from src.modules.Agenda.Domain.Entities.Room import Room
from src.modules.Agenda.Domain.ValueObjects import Hour
from src.modules.Agenda.Domain.ValueObjects.AppointmentType import AppointmentType


    
@dataclass(frozen=True)
class AppointmentSchedulingOutputDTO:
    doctor: Doctor
    day: Day
    patient: Patient
    room: list[Room]
    appointments: list[Appointment]
    type: AppointmentType
    time: Hour

