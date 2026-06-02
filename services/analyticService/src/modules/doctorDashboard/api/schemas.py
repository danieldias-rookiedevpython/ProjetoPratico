from pydantic import BaseModel


class DoctorProductivity(BaseModel):
    scheduled_appointments: int
    finished_appointments: int
    canceled_appointments: int
    average_delay_minutes: float


class DoctorPatientFlow(BaseModel):
    new_patients: int
    returning_patients: int
    no_show_rate: float


class DoctorDashboardResponse(BaseModel):
    doctor_id: str
    period: str
    productivity: DoctorProductivity
    patient_flow: DoctorPatientFlow
    next_action: str
