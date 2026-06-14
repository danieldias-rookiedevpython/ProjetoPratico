import os
def get_database_url() -> str:
    return os.getenv("AGENDA_DATABASE_URL", "postgresql://postgres:password@agenda-postgres:5432/agendadb")


<<<<<<< HEAD
def get_sqlite_path(database_url: str | None = None) -> Path:
    url = database_url or get_database_url()
    if not url.startswith("sqlite:///"):
        return DEFAULT_SQLITE_PATH
    return Path(url.replace("sqlite:///", "", 1))

=======
def get_sqlite_path(database_url: str | None = None):
    raise RuntimeError("agendaService now uses Postgres; use get_database_url instead")
>>>>>>> example
