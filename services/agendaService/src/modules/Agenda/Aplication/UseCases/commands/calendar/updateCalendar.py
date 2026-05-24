class UpdateCalendar:
    def __init__(self, repository):
        self._repository = repository
    
    def execute(self, calendar_id: int, doctor_id: int, room_id: int) -> bool:
         self._repository.update(calendar_id, doctor_id, room_id) 
         return True