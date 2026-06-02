class BusinessDashboardService:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        return self.repository.get_dashboard()


class PlatformDashboardService:
    def __init__(self, observability_gateway):
        self.observability_gateway = observability_gateway

    def execute(self):
        snapshot = self.observability_gateway.network_snapshot()
        snapshot["period"] = "last_5_minutes"
        return snapshot
