from typing import Protocol


class EventBusPort(Protocol):
    def publish(self, event) -> None: ...


class NullEventBus:
    def publish(self, event) -> None:
        return None
