import hashlib
import re

from ..exceptions.DomainExceptions import InvalidPasswordException


class Password:
    def __init__(self, value: str | None, hashed: bool = False):
        if value is None:
            self.value = None
            return
        if hashed:
            self.value = value
            return

        value = value.strip()
        if len(value) < 8:
            raise InvalidPasswordException("senha deve ter pelo menos 8 caracteres")
        if len(value) > 128:
            raise InvalidPasswordException("senha deve ter no maximo 128 caracteres")
        if not re.search(r"[A-Z]", value):
            raise InvalidPasswordException("senha deve conter uma letra maiuscula")
        if not re.search(r"[a-z]", value):
            raise InvalidPasswordException("senha deve conter uma letra minuscula")
        if not re.search(r"[0-9]", value):
            raise InvalidPasswordException("senha deve conter um numero")
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", value):
            raise InvalidPasswordException("senha deve conter um caractere especial")
        self.value = self._hash_password(value)

    @staticmethod
    def _hash_password(value: str) -> str:
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    @property
    def hash(self) -> str | None:
        return self.value

    @property
    def valor(self) -> str | None:
        return self.value

    def verify(self, value: str) -> bool:
        return self.value == self._hash_password(value)

    def __str__(self) -> str:
        return "********"

    def __repr__(self) -> str:
        return "Password('********')"
