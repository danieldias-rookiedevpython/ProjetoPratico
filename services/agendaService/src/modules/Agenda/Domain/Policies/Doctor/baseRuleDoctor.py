from abc import ABC, abstractmethod
from prometheus_client import Enum
from src.Modules.Agenda.Domain.ValueObjects.date import Date
from src.Modules.Agenda.Domain.ValueObjects.rangeTime import RangeTime


class RuleEffect(Enum):
    ADD = "add"
    REMOVE = "remove"
  
    
class BaseRuleDoctor(ABC):
    def __init__(
        self,
        id: str,
        ruleEffect: RuleEffect,
        idToManager = int,
        rom_id: str = None,
        rangeTime: RangeTime = None,
        description: str = None,
        priority: int = None
        
      ):
        self._id=id
        self._rom_id = rom_id
        self._rangeTime = rangeTime
        self._description = description
        self._idToManager = idToManager
        self._priority = priority
        self._ruleEffect = ruleEffect
    
    @staticmethod   
    @abstractmethod
    def create(self):
        pass
    
    @staticmethod
    @abstractmethod
    def isValid(self, Data):
        pass
    
    @property
    def id(self) -> str:
        return self._id
    
    @property
    def rom_id(self) -> str:
        return self._rom_id
    
    @property
    def rangeTime(self) -> str:
        return self._rangeTime
    
    @property
    def description(self) -> str:
        return self._description
    
    @property
    def idToManager(self) -> str:
        return self._idToManager
    
    @property
    def priority(self) -> str:
        return self._priority
    
    @property
    def ruleEffect(self) -> str:
        return self._ruleEffect