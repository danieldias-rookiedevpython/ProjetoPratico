from fastapi import APIRouter

from src.api.controllers import (
    routerAppointment,
    routerCalendar,
    routerClinic,
    routerDoctor,
    routerInfra,
    routerPatient,
    routerRoom,
    routerRule,
    routerWebsocket,
)


api_router = APIRouter(prefix="/agenda")

api_router.include_router(routerAppointment)
api_router.include_router(routerCalendar)
api_router.include_router(routerClinic)
api_router.include_router(routerDoctor)
api_router.include_router(routerInfra)
api_router.include_router(routerPatient)
api_router.include_router(routerRoom)
api_router.include_router(routerRule)
api_router.include_router(routerWebsocket)

routerAgenda = api_router
