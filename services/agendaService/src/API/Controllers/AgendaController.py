from src.Agenda.API.Interfaces.UseCasesAgendaInterface import IUseCasesAgenda
from fastapi import APIRouter,Depends
from src.Agenda.API.provider import useCase_factory
from fastapi_restful.cbv import cbv


routerAgenda = APIRouter(
    prefix="/agenda", 
    tags=["Agenda"],
    #dependencies= Depends(hookFunction)
)

@cbv(routerAgenda)
class AgendaController:
  
    @routerAgenda.post(
        "/",
        #dependencies= Depends(hookFunction)
    )
    def create_agenda(self, name: str,  useCase: IUseCasesAgenda = Depends(useCase_factory)):
        return useCase.execute(name)
    



    @routerAgenda.put(
        "/",
        #dependencies= Depends(hookFunction)
    )
    def update_agenda(self, name: str,  useCase: IUseCasesAgenda = Depends(useCase_factory)):
        return useCase.execute(name)
    



    @routerAgenda.patch(
        "/",
        #dependencies= Depends(hookFunction)
    )
    def update_agenda(self, name: str,  useCase: IUseCasesAgenda = Depends(useCase_factory)):
        return useCase.execute(name)
    



    @routerAgenda.post(
        "/",
        #dependencies= Depends(hookFunction)
    )
    def delete_agenda(self, name: str,  useCase: IUseCasesAgenda = Depends(useCase_factory)):
        return useCase.execute(name)
    



    @routerAgenda.post(
        "/",
        #dependencies= Depends(hookFunction)
    )
    def list_agenda(self, name: str,  useCase: IUseCasesAgenda = Depends(useCase_factory)):
            return useCase.execute(name)
    



    @routerAgenda.post(
        "/",
        #dependencies= Depends(hookFunction)
    )
    def get_agenda_profissional(self, name: str,  useCase: IUseCasesAgenda = Depends(useCase_factory)):
            return useCase.execute(name)
    


    
    @routerAgenda.post(
        "/",
        #dependencies= Depends(hookFunction)
    )
    def list_agenda_profissionais(self, name: str,  useCase: IUseCasesAgenda = Depends(useCase_factory)):
            return useCase.execute(name)



    #admin metodes

    #super admin metodes