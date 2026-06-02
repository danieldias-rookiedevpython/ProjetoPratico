class PacientDomainException(Exception):
    """Base exception for pacient domain rules."""


class PacientAlreadyExistsException(PacientDomainException):
    def __init__(self, field: str):
        super().__init__(f"paciente ja existe com este {field}")


class PacientNotFoundException(PacientDomainException):
    def __init__(self, pacient_id: int | str):
        super().__init__(f"paciente nao encontrado: {pacient_id}")
