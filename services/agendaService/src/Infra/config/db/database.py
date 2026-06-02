import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parents[3]
DEFAULT_SQLITE_PATH = BASE_DIR / "agenda.sqlite3"


def get_database_url() -> str:
    return os.getenv("AGENDA_DATABASE_URL", f"sqlite:///{DEFAULT_SQLITE_PATH}")


def get_sqlite_path(database_url: str | None = None) -> Path:
    url = database_url or get_database_url()
    if not url.startswith("sqlite:///"):
        return DEFAULT_SQLITE_PATH
    return Path(url.replace("sqlite:///", "", 1))
