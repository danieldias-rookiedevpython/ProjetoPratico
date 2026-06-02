from fastapi import APIRouter, Depends, status
from pydantic import BaseModel

from src.api.provider import (
    get_create_calendar_use_case,
    get_delete_calendar_use_case,
    get_day_by_id_query_use_case,
    get_list_days_query_use_case,
    get_update_day_use_case,
)
from src.modules.agenda.aplication.dtos.useCase.query import GetByIdQuery, ListDaysQuery
from src.modules.agenda.aplication.useCases.commands.calendar.CreateCalendar import CreateCalendarCommand
from src.modules.agenda.aplication.useCases.commands.calendar.UpdateDay import UpdateDayCommand


class CreateCalendarRequest(BaseModel):
    mes: int
    ano: int


class UpdateDayRequest(BaseModel):
    id: str
    data: dict


routerCalendar = APIRouter(prefix="/calendars", tags=["Calendars"])


@routerCalendar.post("/", status_code=status.HTTP_201_CREATED)
async def create_calendar(
    command: CreateCalendarRequest,
    use_case=Depends(get_create_calendar_use_case),
):
    return await use_case.execute(CreateCalendarCommand(day=command.mes, ano=command.ano))


@routerCalendar.get("/days/{day_id}")
async def get_day(day_id: str, use_case=Depends(get_day_by_id_query_use_case)):
    return await use_case.execute(GetByIdQuery(id=day_id))


@routerCalendar.get("/days")
async def list_days(
    year: int | None = None,
    month: int | None = None,
    limit: int | None = None,
    offset: int = 0,
    use_case=Depends(get_list_days_query_use_case),
):
    return await use_case.execute(ListDaysQuery(year=year, month=month, limit=limit, offset=offset))


@routerCalendar.patch("/days/{day_id}")
async def update_day(
    day_id: str,
    command: UpdateDayRequest,
    use_case=Depends(get_update_day_use_case),
):
    current = await use_case.execute(UpdateDayCommand(id=day_id, data=command.data))
    if current is None:
        return {"updated": False}
    return {"updated": True, "day": current}


@routerCalendar.delete("/{ano}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_calendar(ano: int, use_case=Depends(get_delete_calendar_use_case)):
    await use_case.execute(str(ano))
