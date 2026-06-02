from ..dtos.output.PacientOutputDTO import PacientOutputDTO
from ..events.PacientEvents import PacientUpdatedEvent
from ..ports.events.EventBusPort import NullEventBus
from ..ports.repository.IPacientRepository import IPacientRepository
from ...domain.exceptions.DomainExceptions import PacientNotFoundException
from .CreateUseCase import _dto_value


class UpdatePacientUseCase:
    def __init__(self, repository: IPacientRepository, event_bus=None):
        self.repository = repository
        self.event_bus = event_bus or NullEventBus()

    def execute(self, data):
        pacient_id = _dto_value(data, "id", "pacient_id")
        if self.repository.find_by_id(pacient_id) is None:
            raise PacientNotFoundException(pacient_id)
        changes = {
            "userName": _dto_value(data, "userName", "username"),
            "email": _dto_value(data, "email"),
            "nome": _dto_value(data, "name", "nome"),
            "password": _dto_value(data, "password", "senha"),
        }
        changes = {key: value for key, value in changes.items() if value is not None}
        updated = self.repository.update(pacient_id, changes)
        if updated is None:
            raise PacientNotFoundException(pacient_id)
        self.event_bus.publish(PacientUpdatedEvent.from_pacient(updated))
        return PacientOutputDTO.from_entity(updated)


UpdateUserUseCase = UpdatePacientUseCase
