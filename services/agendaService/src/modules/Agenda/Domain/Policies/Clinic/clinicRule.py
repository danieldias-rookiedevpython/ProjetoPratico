from .baseRuleClinic import BaseRuleClinic

class ClinicRuleGeneric(BaseRuleClinic):
    id: int
    clinic_id: int
    weekday: int
    starts_at: str
    ends_at: str
    slot_duration_minutes: int
    


class ClinicRuleException(BaseRuleClinic):
    id: int
    clinic_id: int
    weekday: int
    starts_at: str
    ends_at: str
    slot_duration_minutes: int
    
    def isValid(self, date, weekday, availability):
        return pass
    
    @staticmethod
    def create(self):
        return super().create(self)
    
    