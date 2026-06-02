
from .AppointmentController import routerAppointment
from .CalendarController import routerCalendar
from .ClinicController import routerClinic
from .DoctorController import routerDoctor
from .InfraController import routerInfra
from .PatientController import routerPatient
from .RoomController import routerRoom
from .RuleController import routerRule
from .WebsocketController import router as routerWebsocket

__all__ = [
    "routerAppointment",
    "routerCalendar",
    "routerClinic",
    "routerDoctor",
    "routerInfra",
    "routerPatient",
    "routerRoom",
    "routerRule",
    "routerWebsocket",
]
