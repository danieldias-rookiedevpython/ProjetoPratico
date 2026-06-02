class ConsoleEmailSender:
    def send(self, *, to: str, subject: str, body: str) -> str:
        print(f"email sent to={to} subject={subject} body={body}")
        return "sent"

