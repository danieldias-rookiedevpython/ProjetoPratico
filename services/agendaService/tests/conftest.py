<<<<<<< HEAD
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
=======
import pytest

from tests.provider import AgendaTestProvider


@pytest.fixture
def agenda_provider() -> AgendaTestProvider:
    return AgendaTestProvider()
>>>>>>> example
