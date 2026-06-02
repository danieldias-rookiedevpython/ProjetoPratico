from dataclasses import dataclass


@dataclass(frozen=True)
class PacientOutputDTO:
    id: int | None
    userName: str
    email: str
    name: str
    cargo: str | None

    @classmethod
    def from_entity(cls, pacient):
        return cls(
            id=pacient.id,
            userName=pacient.userName.value,
            email=pacient.email.value,
            name=pacient.nome.value,
            cargo=pacient.cargo.valor,
        )

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "userName": self.userName,
            "email": self.email,
            "name": self.name,
            "cargo": self.cargo,
        }
