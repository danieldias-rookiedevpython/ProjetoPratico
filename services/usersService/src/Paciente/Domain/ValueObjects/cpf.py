class CPF:
    def __init__(self, value: str) -> None:
        self.value = verify(value)

    def verify(value: str) -> str:
        return value
    
    def __str__(self) -> str:
        return self.value   
    
    def __repr__(self) -> str:
        return self.value
    
    @staticmethod
    def create(value: str) -> 'CPF':
        return CPF(value)