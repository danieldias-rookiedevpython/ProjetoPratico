import abc

class IAgendaRepository(abc.ABC):
    @abc.abstractmethod
    def get_agendas(self):
        raise NotImplementedError