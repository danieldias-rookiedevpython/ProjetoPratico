from ..dtos.output.UserOutputDTO import UserOutputDTO
from ..events.UserEvents import UserCreatedEvent, UserDeletedEvent, UserUpdatedEvent
from ..ports.events.EventBusPort import NullEventBus
from ..ports.repository.IUserRepository import IUserRepository
from ...domain.exceptions.DomainExceptions import UserAlreadyExistsException, UserNotFoundException


def _dto_value(data, *names, default=None):
    for name in names:
        if hasattr(data, name):
            return getattr(data, name)
        if isinstance(data, dict) and name in data:
            return data[name]
    return default


class CreateUserBaseUseCase:
    entity_class = None

    def __init__(self, repository: IUserRepository, event_bus=None):
        self.repository = repository
        self.event_bus = event_bus or NullEventBus()

    def execute(self, data):
        user = self.entity_class(
            userName=_dto_value(data, "userName", "username"),
            email=_dto_value(data, "email"),
            nome=_dto_value(data, "name", "nome"),
            password=_dto_value(data, "password", "senha"),
        )
        if self.repository.find_by_username(user.userName.value):
            raise UserAlreadyExistsException("userName")
        if self.repository.find_by_email(user.email.value):
            raise UserAlreadyExistsException("email")
        saved = self.repository.save(user)
        self.event_bus.publish(UserCreatedEvent.from_user(saved))
        return UserOutputDTO.from_entity(saved)


class UpdateUserBaseUseCase:
    def __init__(self, repository: IUserRepository, event_bus=None):
        self.repository = repository
        self.event_bus = event_bus or NullEventBus()

    def execute(self, data):
        user_id = _dto_value(data, "id", "user_id")
        current = self.repository.find_by_id(user_id)
        if current is None:
            raise UserNotFoundException(user_id)
        changes = {
            "userName": _dto_value(data, "userName", "username"),
            "email": _dto_value(data, "email"),
            "nome": _dto_value(data, "name", "nome"),
            "password": _dto_value(data, "password", "senha"),
        }
        changes = {key: value for key, value in changes.items() if value is not None}
        updated = self.repository.update(user_id, changes)
        if updated is None:
            raise UserNotFoundException(user_id)
        self.event_bus.publish(UserUpdatedEvent.from_user(updated))
        return UserOutputDTO.from_entity(updated)


class DeleteUserBaseUseCase:
    def __init__(self, repository: IUserRepository, event_bus=None):
        self.repository = repository
        self.event_bus = event_bus or NullEventBus()

    def execute(self, user_id: int):
        current = self.repository.find_by_id(user_id)
        if current is None:
            raise UserNotFoundException(user_id)
        deleted = self.repository.delete(user_id)
        if not deleted:
            raise UserNotFoundException(user_id)
        self.event_bus.publish(UserDeletedEvent.from_user(current))
        return True


class DetailUserBaseUseCase:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self, user_id: int):
        user = self.repository.find_by_id(user_id)
        if user is None:
            raise UserNotFoundException(user_id)
        return UserOutputDTO.from_entity(user)


class ListUserBaseUseCase:
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    def execute(self):
        return [UserOutputDTO.from_entity(user) for user in self.repository.find_all()]
