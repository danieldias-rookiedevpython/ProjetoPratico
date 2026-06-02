from uuid import uuid4


class InMemoryBellNotificationRepository:
    _items: list[dict] = []

    def save(self, data) -> dict:
        notification = {
            "id": str(uuid4()),
            "user_id": data.user_id,
            "title": data.title,
            "message": data.message,
            "link": data.link,
            "read": False,
            "metadata": data.metadata,
        }
        self._items.append(notification)
        return notification

    def list_by_user(self, user_id: str) -> list[dict]:
        return [item for item in self._items if item["user_id"] == user_id]

    def find_by_id(self, notification_id: str) -> dict | None:
        for item in self._items:
            if item["id"] == notification_id:
                return item
        return None

    def mark_as_read(self, notification_id: str) -> dict | None:
        notification = self.find_by_id(notification_id)
        if notification:
            notification["read"] = True
        return notification

    def mark_all_as_read(self, user_id: str) -> None:
        for notification in self.list_by_user(user_id):
            notification["read"] = True

    def count_unread(self, user_id: str) -> int:
        return len([item for item in self.list_by_user(user_id) if not item["read"]])

