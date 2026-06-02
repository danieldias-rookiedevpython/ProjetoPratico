from ..dtos.output.PacientOutputDTO import PacientOutputDTO
from ..events.PacientEvents import PacientCreatedEvent
from ..ports.events.EventBusPort import NullEventBus
from ..ports.repository.IPacientRepository import IPacientRepository
from ...domain.entities.Pacient import Pacient
from ...domain.exceptions.DomainExceptions import PacientAlreadyExistsException


def _dto_value(data, *names, default=None):
    for name in names:
        if hasattr(data, name):
            return getattr(data, name)
        if isinstance(data, dict) and name in data:
            return data[name]
    return default


class CreatePacientUseCase:
    def __init__(self, repository: IPacientRepository, event_bus=None):
        self.repository = repository
        self.event_bus = event_bus or NullEventBus()

    def execute(self, data):
        pacient = Pacient(
            userName=_dto_value(data, "userName", "username"),
            email=_dto_value(data, "email"),
            nome=_dto_value(data, "name", "nome"),
            password=_dto_value(data, "password", "senha"),
        )
        if self.repository.find_by_username(pacient.userName.value):
            raise PacientAlreadyExistsException("userName")
        if self.repository.find_by_email(pacient.email.value):
            raise PacientAlreadyExistsException("email")
        saved = self.repository.save(pacient)
        self.event_bus.publish(PacientCreatedEvent.from_pacient(saved))
        return PacientOutputDTO.from_entity(saved)


CreateUserUseCase = CreatePacientUseCase
