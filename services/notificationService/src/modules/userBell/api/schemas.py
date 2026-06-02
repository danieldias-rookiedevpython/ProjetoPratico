from pydantic import BaseModel, Field


class BellNotificationRequest(BaseModel):
    user_id: str = Field(..., min_length=1)
    title: str = Field(..., min_length=1)
    message: str = Field(..., min_length=1)
    link: str | None = None
    metadata: dict | None = None


class BellNotificationResponse(BaseModel):
    id: str
    user_id: str
    title: str
    message: str
    link: str | None = None
    read: bool
    metadata: dict | None = None


class UnreadCountResponse(BaseModel):
    user_id: str
    count: int

