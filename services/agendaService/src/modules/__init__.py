import sys

from . import Agenda as _agenda
from .Agenda import Aplication as _aplication
from .Agenda import Domain as _domain
from .Agenda.Aplication import UseCases as _use_cases
from .Agenda.Domain import Entities as _entities

sys.modules[f"{__name__}.Agenda"] = _agenda
sys.modules[f"{__name__}.Agenda.Aplication"] = _aplication
sys.modules[f"{__name__}.Agenda.Aplication.UseCases"] = _use_cases
sys.modules[f"{__name__}.Agenda.Domain"] = _domain
sys.modules[f"{__name__}.Agenda.Domain.Entities"] = _entities

