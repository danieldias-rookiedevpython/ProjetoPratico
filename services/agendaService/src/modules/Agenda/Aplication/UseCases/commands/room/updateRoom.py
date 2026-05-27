class UpdateRoom:
    def __init__(self, repository):
        self._repository = repository
    
    def execute(self, room_id: int, name: str) -> bool:
         name = Room(name)
         self._repository.update(room_id, name) 
         return True