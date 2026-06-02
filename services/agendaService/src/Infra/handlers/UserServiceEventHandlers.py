from dataclasses import dataclass
from typing import Any

from src.modules.agenda.aplication.dtos.useCase.command.DoctorUseCasesDTO import CreateDoctorCommand
from src.modules.agenda.aplication.dtos.useCase.command.PatientUseCasesDTO import CreatePatientCommand
from src.modules.agenda.aplication.useCases.commands.doctor.CreateDoctor import CreateDoctorUseCase
from src.modules.agenda.aplication.useCases.commands.doctor.DeleteDoctor import DeleteDoctorUseCase
from src.modules.agenda.aplication.useCases.commands.patient.CreatePacient import CreatePatientUseCase
from src.modules.agenda.aplication.useCases.commands.patient.DeletePacient import DeletePatientUseCase


def _payload_value(payload: Any, *names: str, default: Any = None) -> Any:
    event_payload = payload.get("data") if isinstance(payload, dict) and isinstance(payload.get("data"), dict) else payload
    for name in names:
        if isinstance(event_payload, dict) and name in event_payload:
            return event_payload[name]
        if hasattr(event_payload, name):
            return getattr(event_payload, name)
    return default


def _string_id(value: Any) -> str:
    if value is None:
        raise ValueError("event payload must contain an external user id")
    return str(value)


def _name(value: Any) -> str:
    if value is None or str(value).strip() == "":
        raise ValueError("event payload must contain userName/name")
    return str(value)


@dataclass(frozen=True)
class UserServiceEventResult:
    handled: bool
    entity: str
    external_id: str | None = None
    reason: str | None = None


class UserServiceDoctorCreatedHandler:
    def __init__(self, use_case: CreateDoctorUseCase):
        self._use_case = use_case

    async def handle(self, payload: Any) -> UserServiceEventResult:
        cargo = _payload_value(payload, "cargo", "role")
        if cargo is not None and str(cargo).lower() not in {"doctor", "medic", "medico", "médico"}:
            return UserServiceEventResult(False, "doctor", reason=f"ignored cargo={cargo}")

        external_id = _string_id(_payload_value(payload, "user_id", "id", "medic_id", "doctor_id"))
        name = _name(_payload_value(payload, "userName", "username", "name", "nome"))
        handled = await self._use_case.execute(CreateDoctorCommand(id_extern=external_id, name=name))
        return UserServiceEventResult(bool(handled), "doctor", external_id=external_id)


class UserServicePatientCreatedHandler:
    def __init__(self, use_case: CreatePatientUseCase):
        self._use_case = use_case

    async def handle(self, payload: Any) -> UserServiceEventResult:
        external_id = _string_id(_payload_value(payload, "pacient_id", "patient_id", "user_id", "id"))
        name = _name(_payload_value(payload, "userName", "username", "name", "nome"))
        handled = await self._use_case.execute(CreatePatientCommand(id=external_id, name=name))
        return UserServiceEventResult(bool(handled), "patient", external_id=external_id)


class UserServiceDoctorDeletedHandler:
    def __init__(self, use_case: DeleteDoctorUseCase):
        self._use_case = use_case

    async def handle(self, payload: Any) -> UserServiceEventResult:
        cargo = _payload_value(payload, "cargo", "role")
        if cargo is not None and str(cargo).lower() not in {"doctor", "medic", "medico", "médico", "mÃ©dico"}:
            return UserServiceEventResult(False, "doctor", reason=f"ignored cargo={cargo}")

        external_id = _string_id(_payload_value(payload, "user_id", "id", "medic_id", "doctor_id"))
        handled = await self._use_case.execute(external_id)
        return UserServiceEventResult(bool(handled), "doctor", external_id=external_id)


class UserServicePatientDeletedHandler:
    def __init__(self, use_case: DeletePatientUseCase):
        self._use_case = use_case

    async def handle(self, payload: Any) -> UserServiceEventResult:
        external_id = _string_id(_payload_value(payload, "pacient_id", "patient_id", "user_id", "id"))
        handled = await self._use_case.execute(external_id)
        return UserServiceEventResult(bool(handled), "patient", external_id=external_id)
