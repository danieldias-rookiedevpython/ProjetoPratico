import sys

from . import agenda as _agenda
from .agenda import aplication as _aplication
from .agenda import domain as _domain
from .agenda.aplication import useCases as _use_cases
from .agenda.domain import entities as _entities

sys.modules[f"{__name__}.Agenda"] = _agenda
sys.modules[f"{__name__}.Agenda.Aplication"] = _aplication
sys.modules[f"{__name__}.Agenda.Aplication.UseCases"] = _use_cases
sys.modules[f"{__name__}.Agenda.Domain"] = _domain
sys.modules[f"{__name__}.Agenda.Domain.Entities"] = _entities
