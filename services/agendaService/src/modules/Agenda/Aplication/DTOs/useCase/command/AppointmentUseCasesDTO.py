from dataclasses import dataclass


@dataclass(frozen=True)
class CreateAppointmentCommand:
    scheduler_id: str
    date:str
    weekday:str
    doctor:str
    patient:str
    time:str
    type:str
    room: str | None = None
    
    
@dataclass(frozen=True)
class DeleteAppointmentCommand:
    id: str
    
@dataclass(frozen=True)
class UpdateAppointmentCommand:
    id: str

@dataclass(frozen=True)
class UpdateAppointmentDateCommand:
    id: str
    nome:str 
    time:str
    date:str
    
@dataclass(frozen=True)
class CreateAppointmentTypeCommand:
    name: str
    duration: int
    description: str 
