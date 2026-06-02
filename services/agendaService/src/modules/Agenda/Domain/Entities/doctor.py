from src.modules.agenda.domain.rules.BaseRule import BaseRule
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime
from ..valueObjects.Id import ID
from ..services.VerifyInRange import VerifyInRange



class Doctor:
   
    
    #id_extern: str,
    def __init__(self, name: str, rules: list[BaseRule] | None = None, id: str | None = None, availability: bool = True):
        self._id = ID(id)
        self._name = name
        self._rules = rules or []
        self._availability = availability
        
        
        
        
    def verifyInDisponibility(self, time: RangeTime) -> bool:
        
        if not self._availability:
            return False
        
        return VerifyInRange.execute(time, self._rules)

        
    def update(self, name: str | None = None, rules: list[BaseRule] | None = None, availability: bool | None = None):
        if name is not None:
            self._name = name
        if rules is not None:
            self._rules = rules
        if availability is not None:
            self._availability = availability
        return self
    
    def delete(self) -> bool:
        self._availability = False
        return True
        
    def updateAvailability(self, availability: bool):
        self._availability = availability
        return self
        

        
        
    def addRule(self, rule: BaseRule):
        self._rules.append(rule)
        
        
    def updateRules(self, rules: list[BaseRule]):
        self._rules = rules
        
    def deleteRule(self, rule: BaseRule):
        self._rules.remove(rule)
        
    
    def addClinicRule(self, rule: BaseRule):
        self._rules.append(rule)
        
        
    def updateClinicRules(self, rules: list[BaseRule]):
        self._rules = rules
        
    def deleteClinicRule(self, rule: BaseRule):
        self._rules.remove(rule)
        
    
    def deleteClinicRules(self):
        self._rules = []

    @property
    def id(self) -> ID:
        return self._id

    @property
    def name(self) -> str:
        return self._name

    @property
    def rules(self) -> list[BaseRule]:
        return self._rules

    @property
    def availability(self) -> bool:
        return self._availability
    
    
