from src.Modules.Agenda.Domain.Policies.Doctor.baseRuleDoctor import BaseRuleDoctor
from src.Modules.Agenda.Domain.ValueObjects.rangeTime import RangeTime
from ..services.engineAvailability import engine_availability_doctor
from ..ValueObjects.id import ID
from ..ValueObjects.domainEvents import DomainEvents



class Doctor:
    id: int
    id_extern: str
    name: str
    rules: list[BaseRuleDoctor]
    clinicRules: list[BaseRuleDoctor]
    availability: bool
    timeOcupped: list[int][RangeTime]
    _events: list[DomainEvents]