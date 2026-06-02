from dataclasses import dataclass

from src.modules.agenda.domain.rules import BaseRule


@dataclass(frozen=True)
class CreateBlockRuleEvent:
    rule: BaseRule


@dataclass(frozen=True)
class CreateGenericRuleEvent:
    rule: BaseRule


@dataclass(frozen=True)
class CreateSpecificEntityRuleEvent:
    rule: BaseRule


@dataclass(frozen=True)
class CreateSpecificRuleEvent:
    rule: BaseRule


@dataclass(frozen=True)
class CreateWeekRuleEvent:
    rule: BaseRule


@dataclass(frozen=True)
class DeleteRuleEvent:
    rule_id: str
