
from abc import ABC, abstractmethod
from src.modules.Agenda.Domain.rules.BaseRule import BaseRule


class CalendarDataPort(ABC):

    @abstractmethod
    def pullData(self) -> list[BaseRule]:
        pass

    async def mont(self, mes: int | str, ano: int | str) -> list[dict]:
        return []

