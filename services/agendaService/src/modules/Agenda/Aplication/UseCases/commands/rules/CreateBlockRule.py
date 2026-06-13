from src.modules.Agenda.Aplication.DTOs.exceptions import CreateUseCaseException
from src.modules.Agenda.Aplication.DTOs.useCase.command.RulesUseCasesDTO import CreateBlockRuleCommand
from src.modules.Agenda.Aplication.events.RuleEvent import CreateBlockRuleEvent
from src.modules.Agenda.Aplication.Ports.events.BusPort import BusPort
from src.modules.Agenda.Aplication.Ports.repository import RuleRepositoryPort
from src.modules.Agenda.Domain.rules.BlockRule import BlockRule


class CreateBlockRuleUseCase:
    def __init__(self, repository: RuleRepositoryPort, bus: BusPort):
        self._repository = repository
        self._bus = bus

    async def execute(self, command: CreateBlockRuleCommand) -> bool:
        try:
            rule = BlockRule(
                date=command.date,  # type: ignore[arg-type]
                weekday=command.weekday,
                description=command.description,
                target=command.target,
                targetType=command.targetType,  # type: ignore[arg-type]
                nome=command.nome,
            )
            await self._repository.save(rule)
            self._bus.emit(CreateBlockRuleEvent(rule))
            return True
        except Exception as e:
            raise CreateUseCaseException(
                code="CREATE_BLOCK_RULE_ERROR",
                message="Error creating block rule",
                use_case=self.__class__.__name__,
                context={"command": str(command)},
                original=e,
            ) from e

