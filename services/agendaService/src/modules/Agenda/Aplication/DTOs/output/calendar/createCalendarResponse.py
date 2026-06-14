from asyncio import Protocol




class ResponseCreateCalendarDTO():
    id: int
    clinic_id: int
    doctor_id: int
    room_id: int