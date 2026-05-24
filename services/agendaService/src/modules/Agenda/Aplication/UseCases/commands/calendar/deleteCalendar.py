class DeleteCalendar:
    def __init__(self, repository):
        self._repository = repository
    
    def execute(self, calendar_id: int) -> bool:
         self._repository.delete(calendar_id) 
         if(self._repository.getAllSlots()):
             return False
         return True