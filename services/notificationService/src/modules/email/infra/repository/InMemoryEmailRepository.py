from uuid import uuid4


class InMemoryEmailRepository:
    _items: list[dict] = []

    def save(self, data) -> dict:
        email = {
            "id": str(uuid4()),
            "to": data.to,
            "subject": data.subject,
            "body": data.body,
            "status": "pending",
            "metadata": data.metadata,
        }
        self._items.append(email)
        return email

    def update_status(self, email_id: str, status: str) -> dict | None:
        for email in self._items:
            if email["id"] == email_id:
                email["status"] = status
                return email
        return None

    def list_all(self) -> list[dict]:
        return list(self._items)

