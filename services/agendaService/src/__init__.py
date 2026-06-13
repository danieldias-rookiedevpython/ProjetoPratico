import sys
import types

infra_alias = types.ModuleType("src.infra")
infra_alias.__path__ = []
sys.modules["src.infra"] = infra_alias

from . import Infra as _infra

sys.modules["src.infra"] = _infra
sys.modules["src.Infra"] = _infra

from . import API as _api

sys.modules["src.api"] = _api
sys.modules["src.API"] = _api

