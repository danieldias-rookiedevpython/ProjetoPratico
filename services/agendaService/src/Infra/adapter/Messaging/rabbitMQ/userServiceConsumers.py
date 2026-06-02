import json
from dataclasses import asdict, is_dataclass
from typing import Any

from src.infra.clients.rabbitmq import RabbitMQClient
from src.infra.config.settings import settings
from src.infra.handlers import (
    UserServiceDoctorCreatedHandler,
    UserServiceDoctorDeletedHandler,
    UserServicePatientCreatedHandler,
    UserServicePatientDeletedHandler,
)


def _event_name(payload: dict[str, Any]) -> str:
    event = payload.get("event") or payload.get("type") or payload.get("name") or ""
    return str(event).lower()


class UserServiceCreatedEventsConsumer:
    def __init__(
        self,
        rabbitmq: RabbitMQClient,
        doctor_created_handler: UserServiceDoctorCreatedHandler,
        patient_created_handler: UserServicePatientCreatedHandler,
        doctor_deleted_handler: UserServiceDoctorDeletedHandler,
        patient_deleted_handler: UserServicePatientDeletedHandler,
    ):
        self._rabbitmq = rabbitmq
        self._doctor_created_handler = doctor_created_handler
        self._patient_created_handler = patient_created_handler
        self._doctor_deleted_handler = doctor_deleted_handler
        self._patient_deleted_handler = patient_deleted_handler

    async def start(self) -> None:
        await self._rabbitmq.consume(
            queue_name=settings.user_events_queue,
            routing_keys=[
                settings.user_doctor_created_routing_key,
                settings.user_patient_created_routing_key,
                settings.user_doctor_deleted_routing_key,
                settings.user_patient_deleted_routing_key,
            ],
            handler=self.handle_message,
        )

    async def handle_message(self, message) -> None:
        async with message.process():
            payload = json.loads(message.body.decode("utf-8"))
            await self.handle_payload(payload, routing_key=message.routing_key)

    async def handle_payload(self, payload: dict[str, Any], routing_key: str | None = None) -> dict[str, Any]:
        event_name = _event_name(payload)
        route = routing_key or event_name

        if route in {settings.user_doctor_created_routing_key, "usercreatedevent", "doctorcreatedevent"}:
            result = await self._doctor_created_handler.handle(payload)
        elif route in {settings.user_patient_created_routing_key, "pacientcreatedevent", "patientcreatedevent"}:
            result = await self._patient_created_handler.handle(payload)
        elif route in {settings.user_doctor_deleted_routing_key, "userdeletedevent", "doctordeletedevent"}:
            result = await self._doctor_deleted_handler.handle(payload)
        elif route in {settings.user_patient_deleted_routing_key, "pacientdeletedevent", "patientdeletedevent"}:
            result = await self._patient_deleted_handler.handle(payload)
        else:
            return {"handled": False, "reason": f"ignored event route={route}"}

        return asdict(result) if is_dataclass(result) else dict(result)
