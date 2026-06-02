from fastapi import APIRouter, Depends, HTTPException, status

from src.api.provider import (
    get_create_doctor_use_case,
    get_delete_doctor_use_case,
    get_doctor_by_id_query_use_case,
    get_list_doctors_query_use_case,
    get_update_doctor_use_case,
)
from src.modules.agenda.aplication.dtos.useCase.command.DoctorUseCasesDTO import (
    CreateDoctorCommand,
    UpdateDoctorCommand,
)
from src.modules.agenda.aplication.dtos.useCase.query import GetByIdQuery, ListQuery


routerDoctor = APIRouter(prefix="/doctors", tags=["Doctors"])


@routerDoctor.post("/", status_code=status.HTTP_201_CREATED)
async def create_doctor(command: CreateDoctorCommand, use_case=Depends(get_create_doctor_use_case)):
    result = await use_case.execute(command)
    return {"created": result}


@routerDoctor.get("/{doctor_id}")
async def get_doctor(doctor_id: str, use_case=Depends(get_doctor_by_id_query_use_case)):
    doctor = await use_case.execute(GetByIdQuery(id=doctor_id))
    if not doctor:
        raise HTTPException(status_code=404, detail="Doctor not found")
    return doctor


@routerDoctor.get("/")
async def list_doctors(
    limit: int | None = None,
    offset: int = 0,
    use_case=Depends(get_list_doctors_query_use_case),
):
    return await use_case.execute(ListQuery(limit=limit, offset=offset))


@routerDoctor.put("/{doctor_id}")
async def update_doctor(
    doctor_id: str,
    command: UpdateDoctorCommand,
    use_case=Depends(get_update_doctor_use_case),
):
    await use_case.execute(command)
    return {"updated": True}


@routerDoctor.delete("/{doctor_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_doctor(doctor_id: str, use_case=Depends(get_delete_doctor_use_case)):
    await use_case.execute(doctor_id)
