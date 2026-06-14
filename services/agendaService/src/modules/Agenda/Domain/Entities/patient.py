from src.Modules.Agenda.Domain.Policies.Patient.baseRulePatient import BaseRulePatient


class Patient:
    id: int
    name: str


    def __init__(self, id: int, name: str, rules: list[int]= []):
        self.id = id
        self.name = name
 