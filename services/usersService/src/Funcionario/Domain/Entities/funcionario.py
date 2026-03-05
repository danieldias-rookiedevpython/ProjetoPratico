from ValueObjects.idFuncionario import IdFuncioanrio 

class Funcionario:
    def __init__(self, id, name, cpf):
        self.id = IdFuncioanrio(id)
        self.name = name
    
