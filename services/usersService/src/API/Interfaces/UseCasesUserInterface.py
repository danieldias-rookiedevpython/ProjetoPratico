from typing import Protocol


class IUseCasesCreateUser(Protocol):
    def execute(self, data): ...


class IUseCasesListUser(Protocol):
    def execute(self): ...


class IUseCasesDeleteUser(Protocol):
    def execute(self, user_id: int): ...


class IUseCasesUpdateUser(Protocol):
    def execute(self, data): ...


class IUseCasesDetailUser(Protocol):
    def execute(self, user_id: int): ...
