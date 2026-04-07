class NameValidator:
    def validate(self, name: str):
        if not name or not name.strip():
            raise ValueError("Nome inválido")

        return True