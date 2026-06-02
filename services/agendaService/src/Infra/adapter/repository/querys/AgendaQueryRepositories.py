from typing import Any

from src.infra.adapter.repository.base import SQLiteRepository
from src.modules.agenda.aplication.dtos.useCase.query import ListDaysQuery, ListQuery


class BaseQueryRepository(SQLiteRepository):
    table_name: str

    async def get_by_id(self, entity_id: str) -> dict | None:
        return await self._fetch_json_cached(self.table_name, entity_id)

    async def list(self, query: ListQuery) -> list[dict]:
        cache_key = self._list_cache_key(self.table_name, f"limit:{query.limit}:offset:{query.offset}")
        cached = await self._redis.get_json(cache_key)
        if isinstance(cached, list):
            return cached
        sql = f"SELECT data FROM {self.table_name} ORDER BY created_at DESC"
        params: list[Any] = []
        if query.limit is not None:
            sql += " LIMIT ? OFFSET ?"
            params.extend([query.limit, query.offset])
        with self._db.connect() as connection:
            rows = connection.execute(sql, tuple(params)).fetchall()
            result = [self._load(row["data"]) for row in rows]
            await self._redis.set_json(cache_key, result)
            return result


class AppointmentQueryRepository(BaseQueryRepository):
    table_name = "appointments"


class ClinicQueryRepository(BaseQueryRepository):
    table_name = "clinics"


class DoctorQueryRepository(BaseQueryRepository):
    table_name = "doctors"


class PatientQueryRepository(BaseQueryRepository):
    table_name = "patients"


class RoomQueryRepository(BaseQueryRepository):
    table_name = "rooms"


class RuleQueryRepository(BaseQueryRepository):
    table_name = "rules"


class CalendarQueryRepository(SQLiteRepository):
    async def get_by_id(self, day_id: str) -> dict | None:
        return await self._fetch_json_cached("days", day_id)

    async def list(self, query: ListDaysQuery) -> list[dict]:
        cache_key = self._list_cache_key(
            "days",
            f"year:{query.year}:month:{query.month}:limit:{query.limit}:offset:{query.offset}",
        )
        cached = await self._redis.get_json(cache_key)
        if isinstance(cached, list):
            return cached
        sql = "SELECT data FROM days"
        params: list[Any] = []
        filters: list[str] = []

        if query.year is not None:
            filters.append("year = ?")
            params.append(query.year)
        if query.month is not None:
            filters.append("month = ?")
            params.append(query.month)

        if filters:
            sql += " WHERE " + " AND ".join(filters)

        sql += " ORDER BY year DESC, month DESC, day DESC"

        if query.limit is not None:
            sql += " LIMIT ? OFFSET ?"
            params.extend([query.limit, query.offset])

        with self._db.connect() as connection:
            rows = connection.execute(sql, tuple(params)).fetchall()
            result = [self._load(row["data"]) for row in rows]
            await self._redis.set_json(cache_key, result)
            return result
