import uuid

class ID:

    id: str

    def __init__(self):
        self.id = ID.generate_id()
        
    def __str__(self):
        return self.id
    
    @staticmethod
    def generate_id():
        return str(uuid.uuid4())
    
    def compare(self, other_id):
        if isinstance(other_id, ID):
            return self.id == other_id.id
        elif isinstance(other_id, str):
            return self.id == other_id
        else:
            raise ValueError("Invalid ID type for comparison")