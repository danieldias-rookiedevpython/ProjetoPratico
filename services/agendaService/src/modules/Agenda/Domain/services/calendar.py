from src.Modules.Agenda.Domain.Entities.slot import Slot


class Calendar:
    slots: list[Slot]
    clinicRules: list[int]
    

    def __init__(self, clinicRules: list[int], slots: list[Slot] = []):
        self.slots = slots
        self.clinicRules = clinicRules
        
    
    def createSlots(self, data:list[dict]):
        
        for element in data:
            tamanho1 = len(self.slots)
            self.slots.append(Slot.selfCreate(element['room_id'], element['date'], element['weekday'], element['availability'], element['status'], element['hoursRange'], element['hoursExceptions']))
            tamanho2 = len(self.slots)
            if tamanho2 != tamanho1 + 1:
                raise Exception("Erro ao criar slot \n" + element)  
            
             
        return True
        
    
    def updateSlots(self, data:list[dict]):
        
        for element in data:
            slot = next((s for s in self.slots if s.id == element['id']), None)
            if slot:
                slot.updateState(element['status'])
                slot.createExceptions(element['hoursExceptions'])
    
    
    
    def getCalendar(self):
        return self.slots