from src.config import PROMETHEUS_URL

from ..infra.observability.PrometheusGateway import PrometheusGateway
from ..infra.repository.InMemoryBusinessAnalyticsRepository import InMemoryBusinessAnalyticsRepository
from .OperationsCenterService import BusinessDashboardService, PlatformDashboardService


class OperationsCenterContext:
    business_repository = InMemoryBusinessAnalyticsRepository()
    prometheus_gateway = PrometheusGateway(PROMETHEUS_URL)

    @staticmethod
    def business_dashboard_service():
        return BusinessDashboardService(OperationsCenterContext.business_repository)

    @staticmethod
    def platform_dashboard_service():
        return PlatformDashboardService(OperationsCenterContext.prometheus_gateway)
