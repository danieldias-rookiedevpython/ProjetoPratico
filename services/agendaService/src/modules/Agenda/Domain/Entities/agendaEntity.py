from pydantic import BaseModel
from datetime import date, time
from typing import Optional


class AgendaBase(BaseModel):
    paciente: str
    profissional: str
    data: date
    horario: time
    observacao: Optional[str] = None


class AgendaCreate(AgendaBase):
    pass


class AgendaUpdate(BaseModel):
    paciente: Optional[str] = None
    profissional: Optional[str] = None
    data: Optional[date] = None
    horario: Optional[time] = None
    observacao: Optional[str] = None


class AgendaEntity(AgendaBase):
    id: int