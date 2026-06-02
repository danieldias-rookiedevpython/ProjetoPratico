from src.modules.agenda.domain.entities.Day import Day
from src.modules.agenda.domain.entities.Doctor import Doctor
from src.modules.agenda.domain.entities.Patient import Patient
from src.modules.agenda.domain.entities.Room import Room
from src.modules.agenda.domain.valueObjects import Hour, RangeTime
from src.modules.agenda.domain.valueObjects.EnumAppointment import AppointmentStatus
from src.modules.agenda.domain.valueObjects.AppointmentType import  AppointmentType
from src.modules.agenda.domain.valueObjects.Id import ID




class Appointment:
   

    def __init__(
        self,
        rangeTime: RangeTime,
        patient: str,
        doctor: str,
        room: str,
        type: AppointmentType,
        time: Hour,
        status: AppointmentStatus,
        id: ID | None = None
    ) -> None:
        self._patient_id = patient
        self._doctor_id = doctor
        self._room_id = room
        self._type = type
        self._time = time
        self._status = status
        self._id = id or ID()
        self._rangeTime = rangeTime
        
      
    
    @staticmethod
    def create(
        patient: Patient,
        doctor: Doctor,
        rooms: list[Room],
        day: Day,
        time: Hour,
        type: AppointmentType,
    ):
        
        raw_time = str(time)
        rangeTime = RangeTime.generate(raw_time, type.duration)
        
        if day.verifyInDisponibility(rangeTime) and doctor.verifyInDisponibility(rangeTime):
            
            roomSelected = None
            for room in rooms:
                if room.verifyInDisponibility(rangeTime):
                    roomSelected = room
            
            if(roomSelected == None):
                return None
            
            return Appointment(
                id=ID(),
                patient=str(patient.id),
                doctor=str(doctor.id),
                room=str(roomSelected.id),
                time=Hour(raw_time),
                type=type,
                status= AppointmentStatus.AVAILABLE,
                rangeTime=rangeTime
            )

        return None
       
    
    
    
    
    def verifyOverleaps(self, time):
        return self._rangeTime.overlaps(time)

    def update(self, data):
        if hasattr(data, "time"):
            self._time = Hour(data.time)
        return self

    @property
    def id(self) -> ID:
        return self._id

    @property
    def rangeTime(self) -> RangeTime:
        return self._rangeTime

    @property
    def time(self) -> Hour:
        return self._time

    @property
    def status(self) -> AppointmentStatus:
        return self._status
    
    
