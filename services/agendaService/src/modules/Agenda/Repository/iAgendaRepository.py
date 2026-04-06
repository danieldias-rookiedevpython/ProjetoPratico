from typing import Protocol

class IUserRepository(Protocol):
    def save(self, user: User) -> None: ...