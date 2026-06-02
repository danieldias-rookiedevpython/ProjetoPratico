class SendEmailService:
    def __init__(self, repository, sender):
        self.repository = repository
        self.sender = sender

    def execute(self, data):
        email = self.repository.save(data)
        status = self.sender.send(to=email["to"], subject=email["subject"], body=email["body"])
        return self.repository.update_status(email["id"], status)


class ListSentEmailsService:
    def __init__(self, repository):
        self.repository = repository

    def execute(self):
        return self.repository.list_all()

