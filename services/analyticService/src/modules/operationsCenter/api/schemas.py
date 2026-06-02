from pydantic import BaseModel


class BusinessRevenue(BaseModel):
    gross_amount: float
    pending_amount: float
    canceled_amount: float


class BusinessAppointments(BaseModel):
    scheduled: int
    finished: int
    canceled: int
    occupancy_rate: float


class BusinessDashboardResponse(BaseModel):
    period: str
    revenue: BusinessRevenue
    appointments: BusinessAppointments
    top_clinics: list[dict]
    alerts: list[str]


class ServiceHealth(BaseModel):
    service: str
    availability: float
    p95_latency_ms: float
    error_rate: float


class PlatformDashboardResponse(BaseModel):
    period: str
    source: str
    network_health_score: float
    services: list[ServiceHealth]
    queue_depth: dict
    infra_notes: list[str]
