class DeleteRoom:
    def __init__(self, repository):
        self._repository = repository
    
    def execute(self, room_id: int) -> bool:
         self._repository.delete(room_id) 
         if(self._repository.getAllSlots()):
             return False
         return True