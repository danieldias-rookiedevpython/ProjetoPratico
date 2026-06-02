from typing import Any
from src.modules.agenda.domain.rules.BaseRule import BaseRule
from src.modules.agenda.domain.services import VerifyInRange
from src.modules.agenda.domain.valueObjects.Id import ID
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime



class Room:

    def __init__(self, name: str, rules: list[BaseRule] | None = None, disponibility: bool = True, id: str | None = None):
        self.name = name
        self._disponibility = disponibility
        self.rules = rules or []
        self.id = ID.generate_id()  if id==None else ID(id)
        self.appointmentList: list[Any] = []
        
  

    def verifyInDisponibility(self, time: RangeTime) -> bool:
        
        if not self._disponibility:
            return False
        
         
        if VerifyInRange.execute(time, self.rules):
            for appointment in self.appointmentList:
                if appointment.verifyOverleaps(time):
                    return False
        else:
            return False
        
        return True

    def update(self, name: str | None = None, rules: list[BaseRule] | None = None, disponibility: bool | None = None):
        if name is not None:
            self.name = name
        if rules is not None:
            self.rules = rules
        if disponibility is not None:
            self._disponibility = disponibility
        return self

    def updateStateRoom(self, data: Any):
        disponibility = getattr(data, "disponibility", None)
        name = getattr(data, "name", None)
        rules = getattr(data, "rules", None)
        return self.update(name=name, rules=rules, disponibility=disponibility)

    def delete(self) -> bool:
        self._disponibility = False
        return True
    
   
       

        
    @property
    def disponibility(self):
        return self._disponibility

 
