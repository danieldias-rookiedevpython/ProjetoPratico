
from dataclasses import dataclass
from typing import Optional
from ..services.engineAvailability import engine_availability_slots
from sqlalchemy import Date
from src.Modules.Agenda.Domain.Entities.appointment import Appointment
from src.Modules.Agenda.Domain.Entities.room import Room
from src.Modules.Agenda.Domain.Policies.Clinic.baseRuleClinic import BaseRuleClinic
from src.Modules.Agenda.Domain.ValueObjects.rangeTime import RangeTime
from src.Modules.Agenda.Domain.ValueObjects.slotStatus import SlotStatus
from ..ValueObjects.domainEvents import DomainEvents


class Slot:
   
    _events: list[DomainEvents]
    def __init__(
        self,
        room_id: list[Room],
        date: Date,
        weekday: int,
        availability: bool,
        status: SlotStatus,
        rules: list[BaseRuleClinic],
        disponibility: list[RangeTime] = [],
        appointmentList_id:list[Appointment]=[],
        slot_id: int = None
    ):

        self.room_id = room_id
        self.date = date
        self.availability = availability
        self.weekday = weekday
        self.status = status
        self.appointmentList_id = appointmentList_id
        self.id = slot_id
        self.rules = rules
       
        
   
    
    def updateState(self, newStatus: SlotStatus):
        self.status = newStatus
        self.addEvent("objeto de evento")
        
    def createExceptions(self, exceptions: list[RangeTime]):
        self.hoursExceptions = exceptions
        self.addEvent("objeto de evento")
        
    def addAppointment(self, appointment_id: int):
        self.appointmentList_id.append(appointment_id)
        self.addEvent("objeto de evento")
    
    def removeAppointment(self, appointment_id: int):
        self.appointmentList_id.remove(appointment_id)
        self.addEvent("objeto de evento")
    
    def isAvailable(self, time: RangeTime) -> bool:
        if self.status != SlotStatus.AVAILABLE:
            return False
        
        for exception in self.hoursExceptions or []:
            if exception.overlaps(time):
                return False
        
        return True
    
    
    @staticmethod
    def selfCreate(
        room_id: int ,
        date: Date,
        weekday: int,
        availability: int,
        status: SlotStatus,
        rules: list[BaseRuleClinic],
    ) -> 'Slot':
        
        
        for rule in rules:
          
          if (rule.date == date and rule.weekday == None and rule.rangeTime == None):
              availability = False
              status = SlotStatus.HOLIDAY
              return Slot(
                    room_id=room_id,
                    date=date,
                    weekday=weekday,
                    availability=availability,
                    status=status,
                    rules=[].append(rule)
                )
              
          if(rule.date == None and rule.weekday == weekday and rule.rangeTime == None):
              availability = False
              status = SlotStatus.HOLIDAY
              return Slot(
                    room_id=room_id,
                    date=date,
                    weekday=weekday,
                    availability=availability,
                    status=status,
                    rules=[].append(rule)
                )
          
        rulesAdequate = engine_availability_slots(rules, date, weekday)
       
    
        
        obj =Slot(
            room_id=room_id,
            date=date,
            weekday=weekday,
            availability=availability,
            status=status,
            rules=rulesAdequate
        )
        
        obj.addEvent("objeto de evento")
        return obj
        
    
    
    def addEvent(self, event: DomainEvents):
        self._events.append(event)
        
    
    
    
    # =========================
    # GETTERS
    # =========================

    @property
    def room_id(self):
        return self.__room_id

    @property
    def date(self):
        return self.__date

    @property
    def weekday(self):
        return self.__weekday

    @property
    def availability(self):
        return self.__availability

    @property
    def status(self):
        return self.__status

    @property
    def hoursRange(self):
        return self.__hoursRange

    @property
    def appointmentList_id(self):
        return self.__appointmentList_id


    @property
    def hoursExceptions(self):
        return self.__hoursExceptions

    @property
    def slot_id(self):
        return self.__slot_id

    # =========================
    # SETTERS
    # =========================

    @room_id.setter
    def room_id(self, value):
        self.__room_id = value

    @date.setter
    def date(self, value):
        self.__date = value

    @weekday.setter
    def weekday(self, value):
        self.__weekday = value

    @availability.setter
    def availability(self, value):
        self.__availability = value

    @status.setter
    def status(self, value):
        self.__status = value

    @hoursRange.setter
    def hoursRange(self, value):
        self.__hoursRange = value

    @appointmentList_id.setter
    def appointmentList_id(self, value):
        self.__appointmentList_id = value

    @hoursExceptions.setter
    def hoursExceptions(self, value):
        self.__hoursExceptions = value

    @slot_id.setter
    def slot_id(self, value):
        self.__slot_id = value