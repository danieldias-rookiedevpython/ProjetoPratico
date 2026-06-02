

from src.modules.agenda.domain.valueObjects.Id import ID


class Patient:
    


    def __init__(self, id: str | None, name: str, extern_id: str | None = None, appointments: list[str] | None = None):
        self.id = ID(id)
        self.name = name
        self.appoiments = appointments or []
        self.extern_id = extern_id or str(self.id)
        
    def add_appoiment(self, appoiment: str):
        self.appoiments.append(appoiment)

    def update(self, name: str | None = None):
        if name is not None:
            self.name = name
        return self

    def destroy(self) -> bool:
        return True
 
