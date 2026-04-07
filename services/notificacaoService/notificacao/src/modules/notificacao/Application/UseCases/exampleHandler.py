class UseCasesAgenda:
    def __init__(self):
        pass

    def create_agendamento(self, name: str):
        if not name:
            raise ValueError("Nome é obrigatório")

        return {"message": f"Agendamento criado para {name}"}