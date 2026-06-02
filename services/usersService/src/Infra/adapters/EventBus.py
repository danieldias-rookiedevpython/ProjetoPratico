class InMemoryEventBus:
    def __init__(self):
        self.events = []

    def publish(self, event) -> None:
        self.events.append(event)
