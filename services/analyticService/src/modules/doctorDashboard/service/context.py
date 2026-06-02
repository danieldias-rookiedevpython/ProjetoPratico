from ..infra.repository.InMemoryDoctorAnalyticsRepository import InMemoryDoctorAnalyticsRepository
from .DoctorDashboardService import DoctorDashboardService


class DoctorDashboardContext:
    repository = InMemoryDoctorAnalyticsRepository()

    @staticmethod
    def dashboard_service():
        return DoctorDashboardService(DoctorDashboardContext.repository)
