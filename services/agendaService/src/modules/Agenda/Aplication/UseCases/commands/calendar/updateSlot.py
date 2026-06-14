class UpdateSlot:
    def __init__(self, repository):
        self._repository = repository
    
    def execute(self, slot_id: int, status: str) -> bool:
         self._repository.update(slot_id, status) 
         return True