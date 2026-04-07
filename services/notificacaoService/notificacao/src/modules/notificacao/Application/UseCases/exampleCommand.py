class ExampleCommand:
    def execute(self, data: dict):
        if not data:
            raise ValueError("Dados são obrigatórios")

        return {"status": "success", "data": data}