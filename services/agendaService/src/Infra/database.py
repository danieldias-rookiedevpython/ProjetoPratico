import sqlite3
from contextlib import contextmanager

from src.infra.config.db.database import get_sqlite_path


class Database:
    def __init__(self, database_url: str | None = None):
        self.path = get_sqlite_path(database_url)
        self.path.parent.mkdir(parents=True, exist_ok=True)

    @contextmanager
    def connect(self):
        connection = sqlite3.connect(self.path)
        connection.row_factory = sqlite3.Row
        try:
            yield connection
            connection.commit()
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()


database = Database()
