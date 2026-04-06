from typing import Protocol


#protocol que define os métodos que o controller deve implementar em tempo de desenvolvimento, sem precisar da implementação concreta
#use mypy para verificar se a classe que implementa o controller realmente implementa os métodos definidos na interface
#não existe em runtime, é apenas para verificação estática de tipos

class IUseCasesAgenda(Protocol):
    def __init__(self):
        pass
    def execute(self, name: str):
        pass
 