from .UserEntity import User


class Admin(User):
    def __init__(
        self,
        userName: str,
        email: str,
        nome: str,
        password: str | None = None,
        id: int | None = None,
        password_hashed: bool = False,
    ):
        super().__init__(
            userName=userName,
            email=email,
            nome=nome,
            password=password,
            cargo="ADMIN",
            id=id,
            password_hashed=password_hashed,
        )
