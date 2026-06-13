from unittest.mock import AsyncMock

from fastapi.testclient import TestClient

from src.server import app
from src.API.provider import (
    get_create_doctor_use_case,
    get_delete_doctor_use_case,
    get_doctor_by_id_query_use_case,
    get_list_doctors_query_use_case,
    get_update_doctor_use_case,
)

client = TestClient(app)


def setup_function():
    app.dependency_overrides.clear()


def test_create_doctor():
    mock_use_case = AsyncMock()
    mock_use_case.execute.return_value = True

    app.dependency_overrides[get_create_doctor_use_case] = lambda: mock_use_case

    response = client.post(
        "/agenda/doctors/",
        json={
            "id_extern": "123",
            "name": "Dr House",
        },
    )

    assert response.status_code == 201
    assert response.json() == {"created": True}