from ..dtos.output.PacientOutputDTO import PacientOutputDTO
from ..ports.repository.IPacientRepository import IPacientRepository


class ListPacientUseCase:
    def __init__(self, repository: IPacientRepository):
        self.repository = repository

    def execute(self):
        return [PacientOutputDTO.from_entity(pacient) for pacient in self.repository.find_all()]


ListUserUseCase = ListPacientUseCase
