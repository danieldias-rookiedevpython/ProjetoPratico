class DoctorDashboardService:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, doctor_id: str):
        return self.repository.get_dashboard(doctor_id)
