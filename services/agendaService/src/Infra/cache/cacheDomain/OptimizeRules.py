from src.modules.agenda.domain.rules.BaseRule import BaseRule
from src.modules.agenda.domain.rules.RuleEnum import RuleEffect
from src.modules.agenda.domain.valueObjects.RangeTime import RangeTime

class OptimizeRules:
    def __init__(self):
        self.rules = []
        
       

                    
    def removeRedundantRules(self, rules: list[BaseRule] | None = None) -> list[BaseRule]:
        rules = rules or []
    
        ordered_rules = sorted(
                rules or [],
                key=lambda rule: (
                    getattr(rule, "ruleEffectPriority", 999),
                    getattr(getattr(rule, "rangeTime", None), "start_time", None) or "",
                ),
            )
    
        arrayAdd: list[BaseRule] = []
        arrayRemove: list[BaseRule] = []

    

        for rule in rules:
            if rule.ruleEffect == RuleEffect.ADD:
                self.merge_into(arrayAdd, rule)

            elif rule.ruleEffect == RuleEffect.REMOVE:
                self.merge_into(arrayRemove, rule)

        return arrayAdd + arrayRemove
    
    def merge_into(target: list[BaseRule], rule: BaseRule) -> None:
            if not target:
                target.append(rule)
                return

            last = target[-1]

            fused_range = RangeTime.fusion(last.rangeTime, rule.rangeTime)

            if fused_range:
                last.rangeTime = fused_range
            else:
                target.append(rule)
            
    @property
    def rules(self):
            return self._rules