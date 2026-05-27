import datetime
from ..ValueObjects.domainEvents import DomainEvents
from src.Modules.Agenda.Domain.Entities.doctor import Doctor
from src.Modules.Agenda.Domain.ValueObjects.enumAppoimentType import AppoimentType
from src.Modules.Agenda.Domain.ValueObjects.id import ID
from src.Modules.Agenda.Domain.ValueObjects.rangeTime import RangeTime
from src.Modules.Agenda.Domain.ValueObjects.slotStatus import SlotStatus


class Appointment:
    
    id: ID
    room_id: int
    patient_id: int
    doctor_id: int
    type: AppoimentType
    time: RangeTime
    _events: list[DomainEvents]
    

    def __init__(self, id: int, patient_id: int, doctor_id: int, room_id: int, doctor_slot_id: int, base_slot_id: int, starts_at: datetime, ends_at: datetime) -> None:
        self.id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.room_id = room_id
        self.doctor_slot_id = doctor_slot_id
        self.base_slot_id = base_slot_id
        self.starts_at = starts_at
        self.ends_at = ends_at
    
    
    @staticmethod
    def create(
        self,
        patient_id: int,
        
    ):

        if doctor_slot.status != SlotStatus.AVAILABLE:
            raise Exception("Doctor slot unavailable")

        if base_slot.status != SlotStatus.AVAILABLE:
            raise Exception("Room unavailable")

        doctor_slot.status = SlotStatus.BOOKED
        base_slot.status = SlotStatus.BOOKED

        appointment = Appointment(
            patient_id=patient_id,
            doctor_id=doctor_slot.doctor_id,
            room_id=base_slot.room_id,
            doctor_slot_id=doctor_slot.id,
            base_slot_id=base_slot.id,
            starts_at=doctor_slot.starts_at,
            ends_at=doctor_slot.ends_at
        )

        return appointment
    
    def update(): pass
    
    def delete(): pass
    
    
    
    
    
    @property
    def id(self) -> int:
        return self._id

    @property
    def patient_id(self) -> int:
        return self._patient_id

    @property
    def doctor_id(self) -> int:
        return self._doctor_id

    @property
    def room_id(self) -> int:
        return self._room_id

    @property
    def doctor_slot_id(self) -> int:
        return self._doctor_slot_id

    @property
    def base_slot_id(self) -> int:
        return self._base_slot_id

    @property
    def starts_at(self) -> datetime:
        return self._starts_at

    @property
    def ends_at(self) -> datetime:
        return self._ends_at
    
    