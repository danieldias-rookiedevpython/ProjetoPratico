from fastapi import HTTPException, status


class CreateNotificationService:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, data):
        return self.repository.save(data)


class ListUserNotificationsService:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_id: str):
        return self.repository.list_by_user(user_id)


class CountUnreadNotificationsService:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_id: str):
        return self.repository.count_unread(user_id)


class MarkNotificationAsReadService:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, notification_id: str):
        notification = self.repository.mark_as_read(notification_id)
        if not notification:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="notification not found")
        return notification


class MarkAllNotificationsAsReadService:
    def __init__(self, repository):
        self.repository = repository

    def execute(self, user_id: str):
        self.repository.mark_all_as_read(user_id)

