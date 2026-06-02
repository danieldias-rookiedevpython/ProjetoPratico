from ..infra.mailer.ConsoleEmailSender import ConsoleEmailSender
from ..infra.repository.InMemoryEmailRepository import InMemoryEmailRepository
from .EmailService import ListSentEmailsService, SendEmailService


class EmailContext:
    repository = InMemoryEmailRepository()
    sender = ConsoleEmailSender()

    @staticmethod
    def send_email_service():
        return SendEmailService(EmailContext.repository, EmailContext.sender)

    @staticmethod
    def list_sent_emails_service():
        return ListSentEmailsService(EmailContext.repository)

