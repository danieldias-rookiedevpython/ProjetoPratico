from dataclasses import dataclass


@dataclass(frozen=True)
class UseCaseExceptionDTO:
    message: str
    code: str = "PACIENT_USE_CASE_ERROR"
