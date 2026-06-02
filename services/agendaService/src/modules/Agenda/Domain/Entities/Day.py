from src.modules.agenda.domain.entities.Room import Room
from src.modules.agenda.domain.services import VerifyInRange
from src.modules.agenda.domain.valueObjects import Date
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime
from src.modules.agenda.domain.valueObjects.EnumDay import DayStatus
from ..rules.BaseRule import BaseRule

class Day:
   
    def __init__(
        self,
        rooms: list[Room],
        date: Date,
        weekday: int,
        availability: bool,
        status: DayStatus,
        rules: list[BaseRule],
    ):

        self._rooms = rooms or []
        self._date = date
        self._availability = availability
        
        self._weekday = weekday
        self._status = status
        self._id = date
        self._rules = rules or []
        self._events: list[object] = []
        self.appointmentList_id: list[int] = []
       
        
    def update(self, rooms: list[Room] | dict):
        if isinstance(rooms, dict):
            self._availability = bool(rooms.get("availability", self._availability))
            self._status = rooms.get("status", self._status)
            return self
        self._rooms = rooms
        return self
 
    def updateState(self, newStatus: DayStatus):
        self._status = newStatus
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
    

    
    def verifyInDisponibility(self, time: RangeTime) -> bool:
        if not self._availability:
            return False
     
        return VerifyInRange.execute(time, self._rules)

        
        
        
    
    
    @staticmethod
    def selfCreate(
        rooms: list[Room],
        date: Date,
        weekday: int,
        availability: bool,
        status: DayStatus,
        rules: list[BaseRule],
    ) -> 'Day':
        
        
        for rule in rules:
          
          if (rule.date == date and rule.weekday == None and rule.rangeTime == None):
              availability = False
              status = DayStatus.HOLIDAY
              return Day(
                    rooms=rooms,
                    date=date,
                    weekday=weekday,
                    availability=availability,
                    status=status,
                    rules=[rule]
                )
              
          if(rule.date == None and rule.weekday == weekday and rule.rangeTime == None):
              availability = False
              status = DayStatus.HOLIDAY
              return Day(
                    rooms=rooms,
                    date=date,
                    weekday=weekday,
                    availability=availability,
                    status=status,
                    rules=[rule]
                )
       
    
        
        obj =Day(
            rooms=rooms,
            date=date,
            weekday=weekday,
            availability=availability,
            status=status,
            rules=rules
        )
        
        obj.addEvent("objeto de evento")
        return obj
        
    
    
    def addRules(self, rules: list[BaseRule]):
        self._rules.extend(rules)

    def addEvent(self, event):
        self._events.append(event)

    @property
    def rooms(self) -> list[Room]:
        return self._rooms

    @property
    def date(self) -> Date:
        return self._date

    @property
    def weekday(self) -> int:
        return self._weekday

    @property
    def availability(self) -> bool:
        return self._availability

    @property
    def status(self) -> DayStatus:
        return self._status

    @property
    def rules(self) -> list[BaseRule]:
        return self._rules
        
    
    
