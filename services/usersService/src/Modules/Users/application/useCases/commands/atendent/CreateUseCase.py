from ...BaseUserUseCases import CreateUserBaseUseCase
from .....domain.entities.AtendenteEntity import Atendente


class CreateAtendentUseCase(CreateUserBaseUseCase):
    entity_class = Atendente


CreateAtendenteUseCase = CreateAtendentUseCase
