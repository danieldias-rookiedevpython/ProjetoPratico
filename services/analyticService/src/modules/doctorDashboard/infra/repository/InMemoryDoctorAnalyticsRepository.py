class InMemoryDoctorAnalyticsRepository:
    def get_dashboard(self, doctor_id: str) -> dict:
        return {
            "doctor_id": doctor_id,
            "period": "last_30_days",
            "productivity": {
                "scheduled_appointments": 128,
                "finished_appointments": 112,
                "canceled_appointments": 9,
                "average_delay_minutes": 7.4,
            },
            "patient_flow": {
                "new_patients": 31,
                "returning_patients": 81,
                "no_show_rate": 0.054,
            },
            "next_action": "review patients with recurring no-show behavior",
        }
