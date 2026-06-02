from dataclasses import dataclass
from datetime import datetime, timezone


@dataclass(frozen=True)
class PacientEvent:
    pacient_id: int | None
    userName: str
    occurred_at: datetime

    @classmethod
    def from_pacient(cls, pacient):
        return cls(
            pacient_id=pacient.id,
            userName=pacient.userName.value,
            occurred_at=datetime.now(timezone.utc),
        )


class PacientCreatedEvent(PacientEvent):
    pass


class PacientUpdatedEvent(PacientEvent):
    pass


class PacientDeletedEvent(PacientEvent):
    pass
