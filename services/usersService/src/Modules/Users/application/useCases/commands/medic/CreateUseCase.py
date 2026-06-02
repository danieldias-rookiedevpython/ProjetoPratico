from ...BaseUserUseCases import CreateUserBaseUseCase
from .....domain.entities.MedicEntity import Medic


class CreateMedicUseCase(CreateUserBaseUseCase):
    entity_class = Medic
