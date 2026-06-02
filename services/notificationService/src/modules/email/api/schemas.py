from pydantic import BaseModel, Field


class EmailRequest(BaseModel):
    to: str = Field(..., min_length=3)
    subject: str = Field(..., min_length=1)
    body: str = Field(..., min_length=1)
    metadata: dict | None = None


class EmailResponse(BaseModel):
    id: str
    to: str
    subject: str
    body: str
    status: str
    metadata: dict | None = None

