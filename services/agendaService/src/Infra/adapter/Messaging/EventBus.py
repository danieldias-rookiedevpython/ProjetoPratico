from collections import defaultdict
from typing import Any, Callable


class AwaitableResult:
    def __init__(self, value=None):
        self.value = value

    def __await__(self):
        async def _wrap():
            return self.value

        return _wrap().__await__()


class InMemoryEventBus:
    def __init__(self):
        self._subscribers = defaultdict(list)
        self.events = []

    def emit(self, event="event", data=None):
        payload = {"event": event, "data": data}
        self.events.append(payload)
        for callback in self._subscribers[event]:
            callback(data)
        return AwaitableResult(payload)

    def publish(self, event="event", data=None, routing_key: str | None = None):
        return self.emit(routing_key or event, data)

    def on(self, event: Any, callback: Callable[..., Any]):
        self._subscribers[event].append(callback)
        return AwaitableResult(True)
