from dataclasses import dataclass

from ..valueObjects.CargoVO import Cargo
from ..valueObjects.EmailVO import Email
from ..valueObjects.NomeVO import Nome
from ..valueObjects.PasswordVO import Password
from ..valueObjects.UserNomeVO import UserName


@dataclass
class User:
    userName: UserName
    email: Email
    nome: Nome
    password: Password
    cargo: Cargo
    id: int | None = None

    def __init__(
        self,
        userName: str,
        email: str,
        nome: str,
        password: str | None = None,
        cargo: str | None = None,
        id: int | None = None,
        password_hashed: bool = False,
    ):
        self.id = id
        self.userName = UserName(userName)
        self.email = Email(email)
        self.nome = Nome(nome)
        self.password = Password(password, hashed=password_hashed)
        self.cargo = Cargo(cargo)

    def update(
        self,
        nome: str | None = None,
        cargo: str | None = None,
        userName: str | None = None,
        email: str | None = None,
        password: str | None = None,
    ) -> dict:
        if nome:
            self.nome = Nome(nome)
        if cargo:
            self.cargo = Cargo(cargo)
        if userName:
            self.userName = UserName(userName)
        if email:
            self.email = Email(email)
        if password:
            self.password = Password(password)
        return self.to_dict()

    def to_dict(self) -> dict:
        data = {
            "id": self.id,
            "userName": self.userName.value,
            "nome": self.nome.value,
            "email": self.email.value,
            "cargo": self.cargo.valor,
        }
        if self.password.value:
            data["password"] = self.password.value
            data["senha"] = self.password.value
        return data

    @classmethod
    def to_object(cls, **kwargs):
        return cls(
            id=kwargs.get("id"),
            userName=kwargs.get("userName") or kwargs.get("username"),
            email=kwargs.get("email"),
            nome=kwargs.get("nome") or kwargs.get("name"),
            password=kwargs.get("password") or kwargs.get("senha"),
            cargo=kwargs.get("cargo"),
            password_hashed=kwargs.get("password_hashed", True),
        )

    def __str__(self) -> str:
        return f"{self.nome} <{self.email}> - {self.cargo}"
