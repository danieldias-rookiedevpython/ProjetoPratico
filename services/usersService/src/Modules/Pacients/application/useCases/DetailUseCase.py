from ..dtos.output.PacientOutputDTO import PacientOutputDTO
from ..ports.repository.IPacientRepository import IPacientRepository
from ...domain.exceptions.DomainExceptions import PacientNotFoundException


class DetailPacientUseCase:
    def __init__(self, repository: IPacientRepository):
        self.repository = repository

    def execute(self, pacient_id: int):
        pacient = self.repository.find_by_id(pacient_id)
        if pacient is None:
            raise PacientNotFoundException(pacient_id)
        return PacientOutputDTO.from_entity(pacient)


DetailUserUseCase = DetailPacientUseCase
