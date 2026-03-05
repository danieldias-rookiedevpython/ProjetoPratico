from ValueObjects.message import Message

class notificacaoEntity:
    def __init__(self, id, message):
        self.id = id
        self.message = Message(message)