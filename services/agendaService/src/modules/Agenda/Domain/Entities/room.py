from src.Modules.Agenda.Domain.Policies.Clinic.baseRuleClinic import BaseRuleClinic
from src.Modules.Agenda.Domain.Policies.Room.baseRuleRoom import BaseRuleRoom
from src.Modules.Agenda.Domain.ValueObjects.id import ID
from src.Modules.Agenda.Domain.ValueObjects.rangeTime import RangeTime
from ..services.engineAvailability import engine_availability_room
from ..ValueObjects.domainEvents import DomainEvents


class Room:
    id: ID
    name: str
    availability: bool
    rules: list[BaseRuleRoom]
    rulesClinic: list[BaseRuleClinic]
    # o timeOcupped e uma matriz relacionando dia e horarios ocupados
    timeOcupped: list[int][RangeTime]
    hoursDisponibility: list[int][RangeTime]
    appointmentList_id: list[int][str]
    _events: list[DomainEvents]
    
    def __init__(self, name: str, disponibility: bool, rules: list[BaseRuleRoom]):
        self.name = name
        self.disponibility = disponibility
        self.rules = rules
    
    def verifyDisponibility(self, time: RangeTime) -> bool:
        if not self.disponibility:
            return False
        
        for rule in self.rules:
            if not rule.isSatisfied(time):
                return False
        
        for ocuppied in self.timeOcupped:
            if ocuppied.overlaps(time):
                return False
        
        self.addOcuppiedTime(BaseRuleRoom(time))
        
        return True
    
   
    def hoursDisponibility(self) -> list[RangeTime]:
        disponibility_hours = []
        for rule in self.rules:
            disponibility_hours.extend(rule.hoursDisponibility())
        
        return disponibility_hours
       
    
    def addOcuppiedTime(self, time: BaseRuleRoom):
        self.timeOcupped.append(time)
        
    @property
    def disponibility(self):
        return self.__disponibility
    
    @property
    def disponibility(self):
        return self.__disponibility

 