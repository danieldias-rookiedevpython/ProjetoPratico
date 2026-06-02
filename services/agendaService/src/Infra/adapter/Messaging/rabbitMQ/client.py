from typing import Any, Callable

from src.infra.adapter.Messaging.EventBus import AwaitableResult
from src.infra.clients.rabbitmq import RabbitMQClient


class RabbitMQEventBus:
    def __init__(self, url: str | None = None, exchange_name: str = "agenda.events"):
        self._client = RabbitMQClient(url=url, exchange_name=exchange_name)

    async def connect(self):
        return await self._client.connect()

    def emit(self, event: Any = "event", data: Any = None):
        return self.publish(event=event, data=data, routing_key=str(event))

    async def publish(self, event: Any = "event", data: Any = None, routing_key: str | None = None):
        await self._client.publish(routing_key or str(event), {"event": event, "data": data})

    def on(self, event: Any, callback: Callable[..., Any]):
        return AwaitableResult(False)

    async def ping(self):
        return await self._client.ping()

    async def close(self) -> None:
        await self._client.close()
