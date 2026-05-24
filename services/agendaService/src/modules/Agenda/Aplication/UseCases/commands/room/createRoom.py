class CreateRoom:
    def __init__(self, repository):
        self._repository = repository
    
    def execute(self, name: str) -> bool:
         name = Room(name)
         self._repository.create(name) 
         return True