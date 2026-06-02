from dataclasses import dataclass


@dataclass(frozen=True)
class GetByIdQuery:
    id: str


@dataclass(frozen=True)
class ListQuery:
    limit: int | None = None
    offset: int = 0


@dataclass(frozen=True)
class ListDaysQuery:
    year: int | None = None
    month: int | None = None
    limit: int | None = None
    offset: int = 0
