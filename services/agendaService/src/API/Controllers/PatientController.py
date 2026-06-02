from fastapi import APIRouter, Depends, HTTPException, status

from src.api.provider import (
    get_create_patient_use_case,
    get_delete_patient_use_case,
    get_patient_by_id_query_use_case,
    get_patient_repository,
    get_list_patients_query_use_case,
)
from src.modules.agenda.aplication.dtos.useCase.command.PatientUseCasesDTO import (
    CreatePatientCommand,
    UpdatePatientCommand,
)
from src.modules.agenda.aplication.dtos.useCase.query import GetByIdQuery, ListQuery


routerPatient = APIRouter(prefix="/patients", tags=["Patients"])


@routerPatient.post("/", status_code=status.HTTP_201_CREATED)
async def create_patient(command: CreatePatientCommand, use_case=Depends(get_create_patient_use_case)):
    result = await use_case.execute(command)
    return {"created": result}


@routerPatient.get("/{patient_id}")
async def get_patient(patient_id: str, use_case=Depends(get_patient_by_id_query_use_case)):
    patient = await use_case.execute(GetByIdQuery(id=patient_id))
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    return patient


@routerPatient.get("/")
async def list_patients(
    limit: int | None = None,
    offset: int = 0,
    use_case=Depends(get_list_patients_query_use_case),
):
    return await use_case.execute(ListQuery(limit=limit, offset=offset))


@routerPatient.put("/{patient_id}")
async def update_patient(
    patient_id: str,
    command: UpdatePatientCommand,
    repository=Depends(get_patient_repository),
    query_use_case=Depends(get_patient_by_id_query_use_case),
):
    patient = await query_use_case.execute(GetByIdQuery(id=patient_id))
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")
    await repository.update(command)
    return {"updated": True}


@routerPatient.delete("/{patient_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_patient(patient_id: str, use_case=Depends(get_delete_patient_use_case)):
    await use_case.execute(patient_id)
