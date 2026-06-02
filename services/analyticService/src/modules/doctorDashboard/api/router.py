from fastapi import APIRouter, Depends

from ..service.context import DoctorDashboardContext
from .schemas import DoctorDashboardResponse


router = APIRouter(prefix="/doctors", tags=["doctor dashboard"])


@router.get("/{doctor_id}/dashboard", response_model=DoctorDashboardResponse)
def get_doctor_dashboard(doctor_id: str, service=Depends(DoctorDashboardContext.dashboard_service)):
    return service.execute(doctor_id)
