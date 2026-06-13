
from src.modules.Agenda.Domain.ValueObjects.Date import Date
from src.modules.Agenda.Domain.ValueObjects.RangeTime import RangeTime
from src.modules.Agenda.Domain.rules.RuleEnum import RuleEffect
from src.modules.Agenda.Domain.rules.BaseRule import BaseRule


class SpecificRule(BaseRule):
    
    def __init__(
        self,
        ruleEffect: RuleEffect,
        target: str,
        rangeTime: RangeTime,
        description: str,
        nome: str | None = None
    ):
        super().__init__(
            ruleEffect=ruleEffect,
            target=target,
            rangeTime=rangeTime,
            description=description,
            nome = nome
        )

