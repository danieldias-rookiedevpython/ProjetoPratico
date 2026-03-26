class IdFuncioanrio:
    def __init__(self, id:str):
        self.id = self.verify(id) 

    def verify(self, id:str):
        return id

    def __str__(self):
        return self.id
    
    def __repr__(self):
        return self.id
    
    @staticmethod
    def create(id:str):
        return IdFuncioanrio(id)