class InMemoryBusinessAnalyticsRepository:
    def get_dashboard(self) -> dict:
        return {
            "period": "last_30_days",
            "revenue": {
                "gross_amount": 182450.75,
                "pending_amount": 21400.0,
                "canceled_amount": 8300.5,
            },
            "appointments": {
                "scheduled": 1840,
                "finished": 1593,
                "canceled": 118,
                "occupancy_rate": 0.82,
            },
            "top_clinics": [
                {"clinic_id": "clinic-01", "name": "Matriz", "appointments": 624, "revenue": 68220.0},
                {"clinic_id": "clinic-02", "name": "Zona Sul", "appointments": 431, "revenue": 45280.0},
            ],
            "alerts": [
                "cancellation rate increased 3.1% over previous period",
                "clinic-02 has occupancy below target on Fridays",
            ],
        }
