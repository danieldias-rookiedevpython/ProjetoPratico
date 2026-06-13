
from src.modules.Agenda.Aplication.DTOs.exceptions import DeleteUseCaseException
from src.modules.Agenda.Aplication.events.RuleEvent import DeleteRuleEvent
from src.modules.Agenda.Aplication.Ports.events.BusPort import BusPort
from src.modules.Agenda.Aplication.Ports.repository.RuleRepositoryPort import RuleRepositoryPort

class DeleteRuleUseCase:
    def __init__(self, repository: RuleRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus
        
    async def execute(self, rule_id: str) -> bool:
        
        rule = await self._repository.deleteRule(rule_id)

        if rule is Exception:
            raise DeleteUseCaseException(
                code="DELETE_RULE_ERROR",
                message="Error deleting rule",
                use_case=self.__class__.__name__,
                context={"rule_id": rule_id},
            )

        
        self._bus.emit(DeleteRuleEvent(rule_id))

        return True

