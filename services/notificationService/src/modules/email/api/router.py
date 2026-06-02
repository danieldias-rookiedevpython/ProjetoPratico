from fastapi import APIRouter, Depends, status

from ..service.context import EmailContext
from .schemas import EmailRequest, EmailResponse


router = APIRouter(prefix="/email", tags=["email"])


@router.post("/send", response_model=EmailResponse, status_code=status.HTTP_202_ACCEPTED)
def send_email(data: EmailRequest, service=Depends(EmailContext.send_email_service)):
    return service.execute(data)


@router.get("/sent", response_model=list[EmailResponse])
def list_sent_emails(service=Depends(EmailContext.list_sent_emails_service)):
    return service.execute()

