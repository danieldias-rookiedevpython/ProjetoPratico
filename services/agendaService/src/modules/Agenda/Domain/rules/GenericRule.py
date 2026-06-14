from src.modules.Agenda.Domain.ValueObjects.RangeTime import RangeTime
from src.modules.Agenda.Domain.rules.RuleEnum import RuleEffect, TargetType
from src.modules.Agenda.Domain.rules.BaseRule import BaseRule



class GenericRule(BaseRule):
    
    def __init__(
        self,
        ruleEffect: RuleEffect,
        targetType: TargetType,
        rangeTime: RangeTime,
        description: str ,
        nome: str | None = None,
        
    ):
        super().__init__(
            ruleEffect=ruleEffect,
            rangeTime=rangeTime, 
            description=description,
            targetType=targetType,
            nome=nome
        ) 

