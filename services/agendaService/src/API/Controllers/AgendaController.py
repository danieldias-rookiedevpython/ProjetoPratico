from fastapi import APIRouter
from src.modules.Agenda.Aplication.Service.AgendaService import AgendaService
from src.Infra.RepoAdapter.AgendaRepository import AgendaRepository
from src.modules.Agenda.Domain.Entities.AgendaEntity import (
    AgendaCreate,
    AgendaUpdate,
)

routerAgenda = APIRouter(prefix="/agenda", tags=["Agenda"])

repository = AgendaRepository()
service = AgendaService(repository)


@routerAgenda.post("/")
def create(agenda: AgendaCreate):
    return service.create(agenda)


@routerAgenda.get("/")
def list_all():
    return service.list_all()


@routerAgenda.get("/{agenda_id}")
def get_by_id(agenda_id: int):
    return service.get_by_id(agenda_id)


@routerAgenda.put("/{agenda_id}")
def update(agenda_id: int, agenda: AgendaUpdate):
    return service.update(agenda_id, agenda)


@routerAgenda.delete("/{agenda_id}")
def delete(agenda_id: int):
    return service.delete(agenda_id)