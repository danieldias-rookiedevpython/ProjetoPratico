from ...BaseUserUseCases import CreateUserBaseUseCase
from .....domain.entities.AdminEntity import Admin


class CreateAdminUseCase(CreateUserBaseUseCase):
    entity_class = Admin
