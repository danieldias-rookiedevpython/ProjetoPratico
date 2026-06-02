from dataclasses import dataclass


@dataclass(frozen=True)
class UserOutputDTO:
    id: int | None
    userName: str
    email: str
    name: str
    cargo: str | None

    @classmethod
    def from_entity(cls, user):
        return cls(
            id=user.id,
            userName=user.userName.value,
            email=user.email.value,
            name=user.nome.value,
            cargo=user.cargo.valor,
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "userName": self.userName,
            "email": self.email,
            "name": self.name,
            "cargo": self.cargo,
        }
