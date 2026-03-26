
from ..Aplication.UseCases.createUseCase import UseCasesAgenda
from ..Infra.Repositorys.AgendaRepository import AgendaRepository

#uma forma
'''
def get_repository_factory():
    # Aqui você pode criar e configurar a instância do seu repositório
    # Por exemplo, se você tiver uma implementação concreta do repositório:
    from ...Infrastructure.Repositories import AgendaRepository
    return AgendaRepository()


def get_usecase_factory():
    # Aqui você pode criar e configurar a instância do seu use case
    # Por exemplo, se você tiver uma implementação concreta do UseCasesAgendaInterface:
    from ...Aplication.UseCases import UseCasesAgenda
    return UseCasesAgenda(get_repository_factory())


def get_controller_factory():
    return AgendaController(get_usecase_factory())

'''

#forma 2
'''
def router_factory():
    repository = AgendaRepository()
    usecase = UseCasesAgenda(repository)
    controller = AgendaController(usecase)
    return AgendaRouter(controller).router

'''

#atual
def useCase_factory():
    repository = AgendaRepository()
    usecase = UseCasesAgenda(repository)
    return usecase
  
    