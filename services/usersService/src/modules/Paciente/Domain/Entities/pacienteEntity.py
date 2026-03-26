
from ValueObjects.cpf import CPF
from ValueObjects.idPaciente import IdPaciente
class Funcionario:
    def __init__(self, id, name, cpf):
        self.id = IdPaciente(id)
        self.name = name
        self.cpf = CPF(cpf)
