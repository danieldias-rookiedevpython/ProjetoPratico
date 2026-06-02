from fastapi import APIRouter, Depends

from src.api.provider import (
    get_infra_health_handler,
    get_user_service_doctor_created_handler,
    get_user_service_doctor_deleted_handler,
    get_user_service_patient_created_handler,
    get_user_service_patient_deleted_handler,
)
from src.infra.handlers import (
    InfraHealthHandler,
    UserServiceDoctorCreatedHandler,
    UserServiceDoctorDeletedHandler,
    UserServicePatientCreatedHandler,
    UserServicePatientDeletedHandler,
)


routerInfra = APIRouter(prefix="/infra", tags=["Infra"])


@routerInfra.get("/health")
async def infra_health(handler: InfraHealthHandler = Depends(get_infra_health_handler)):
    return await handler.check()


@routerInfra.post("/events/users/doctor-created")
async def handle_user_service_doctor_created(
    payload: dict,
    handler: UserServiceDoctorCreatedHandler = Depends(get_user_service_doctor_created_handler),
):
    return await handler.handle(payload)


@routerInfra.post("/events/users/patient-created")
async def handle_user_service_patient_created(
    payload: dict,
    handler: UserServicePatientCreatedHandler = Depends(get_user_service_patient_created_handler),
):
    return await handler.handle(payload)


@routerInfra.post("/events/users/doctor-deleted")
async def handle_user_service_doctor_deleted(
    payload: dict,
    handler: UserServiceDoctorDeletedHandler = Depends(get_user_service_doctor_deleted_handler),
):
    return await handler.handle(payload)


@routerInfra.post("/events/users/patient-deleted")
async def handle_user_service_patient_deleted(
    payload: dict,
    handler: UserServicePatientDeletedHandler = Depends(get_user_service_patient_deleted_handler),
):
    return await handler.handle(payload)
