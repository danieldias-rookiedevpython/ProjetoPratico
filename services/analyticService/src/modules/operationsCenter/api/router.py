from fastapi import APIRouter, Depends

from ..service.context import OperationsCenterContext
from .schemas import BusinessDashboardResponse, PlatformDashboardResponse


router = APIRouter(prefix="/operations", tags=["operations center"])


@router.get("/business/dashboard", response_model=BusinessDashboardResponse)
def get_business_dashboard(service=Depends(OperationsCenterContext.business_dashboard_service)):
    return service.execute()


@router.get("/platform/dashboard", response_model=PlatformDashboardResponse)
def get_platform_dashboard(service=Depends(OperationsCenterContext.platform_dashboard_service)):
    return service.execute()
