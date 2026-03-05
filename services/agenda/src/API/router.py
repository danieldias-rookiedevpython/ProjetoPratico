from site import getuserbase
from fastapi import APIRouter, Depends
from API.Controllers.AgendaController import AgendaController, get_controller_factory
import asyncio



router = APIRouter(prefix="/agenda")



#exemplo controler sem factory, com lambda para injetar dependência
#lambda omite a função de factory
'''
@router.post("/")
def create_user(
    name: str,
    controller: AgendaController = Depends(
        lambda: UserController(UseCasesAgendaDTO())
    )
):
    return controller.create_agendamento(name)
'''



@router.post("/")
def create_user(
    name: str,
    controller: AgendaController = Depends(get_controller_factory)
):
    return controller.create_agenda(name)