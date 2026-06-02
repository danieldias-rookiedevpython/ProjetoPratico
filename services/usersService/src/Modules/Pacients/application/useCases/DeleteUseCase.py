from ..events.PacientEvents import PacientDeletedEvent
from ..ports.events.EventBusPort import NullEventBus
from ..ports.repository.IPacientRepository import IPacientRepository
from ...domain.exceptions.DomainExceptions import PacientNotFoundException


class DeletePacientUseCase:
    def __init__(self, repository: IPacientRepository, event_bus=None):
        self.repository = repository
        self.event_bus = event_bus or NullEventBus()

    def execute(self, pacient_id: int):
        pacient = self.repository.find_by_id(pacient_id)
        if pacient is None:
            raise PacientNotFoundException(pacient_id)
        deleted = self.repository.delete(pacient_id)
        if not deleted:
            raise PacientNotFoundException(pacient_id)
        self.event_bus.publish(PacientDeletedEvent.from_pacient(pacient))
        return True


DeleteUserUseCase = DeletePacientUseCase
