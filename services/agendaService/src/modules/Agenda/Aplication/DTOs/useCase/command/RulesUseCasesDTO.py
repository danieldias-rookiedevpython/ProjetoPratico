from dataclasses import dataclass


@dataclass(frozen=True)
class CreateBlockRuleCommand:
    date: object | None = None
    weekday: int | None = None
    description: str | None = None
    target: str | None = None
    targetType: object | None = None
    nome: str | None = None

@dataclass(frozen=True)
class CreateGenericRuleCommand:
    ruleEffect: object
    targetType: object
    rangeTime: object
    description: str
    nome: str | None = None

@dataclass(frozen=True)
class CreateSpecificRuleCommand:
    ruleEffect: object
    target: str
    rangeTime: object
    description: str
    nome: str | None = None

@dataclass(frozen=True)
class CreateSpecificDayRuleCommand:
    ruleEffect: object
    rangeTime: object
    description: str
    date: object
    target: str | None = None
    targetType: object | None = None
    nome: str | None = None

@dataclass(frozen=True)
class CreateWeekRuleCommand:
    ruleEffect: object
    rangeTime: object
    description: str
    weekday: int
    target: str | None = None
    targetType: object | None = None
    nome: str | None = None

@dataclass(frozen=True)
class DeleteRuleCommand:
    id: str
