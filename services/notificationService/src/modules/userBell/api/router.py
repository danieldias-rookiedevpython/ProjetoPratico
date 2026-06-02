from fastapi import APIRouter, Depends, Response, status

from ..service.context import UserBellContext
from .schemas import BellNotificationRequest, BellNotificationResponse, UnreadCountResponse


router = APIRouter(prefix="/notifications", tags=["user notifications"])


@router.post("/", response_model=BellNotificationResponse, status_code=status.HTTP_201_CREATED)
def create_notification(data: BellNotificationRequest, service=Depends(UserBellContext.create_notification_service)):
    return service.execute(data)


@router.get("/users/{user_id}", response_model=list[BellNotificationResponse])
def list_user_notifications(user_id: str, service=Depends(UserBellContext.list_user_notifications_service)):
    return service.execute(user_id)


@router.get("/users/{user_id}/unread-count", response_model=UnreadCountResponse)
def count_unread_notifications(user_id: str, service=Depends(UserBellContext.count_unread_notifications_service)):
    return {"user_id": user_id, "count": service.execute(user_id)}


@router.patch("/{notification_id}/read", response_model=BellNotificationResponse)
def mark_notification_as_read(notification_id: str, service=Depends(UserBellContext.mark_notification_as_read_service)):
    return service.execute(notification_id)


@router.patch("/users/{user_id}/read-all", status_code=status.HTTP_204_NO_CONTENT)
def mark_all_notifications_as_read(user_id: str, service=Depends(UserBellContext.mark_all_notifications_as_read_service)):
    service.execute(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

