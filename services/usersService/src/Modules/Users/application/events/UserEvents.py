from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class UserEvent:
    user_id: int | None
    userName: str
    cargo: str | None
    occurred_at: datetime

    @classmethod
    def from_user(cls, user):
        return cls(
            user_id=user.id,
            userName=user.userName.value,
            cargo=user.cargo.valor,
            occurred_at=datetime.now(timezone.utc),
        )


class UserCreatedEvent(UserEvent):
    pass


class UserUpdatedEvent(UserEvent):
    pass


class UserDeletedEvent(UserEvent):
    pass
