import sys
<<<<<<< HEAD
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

=======
from pathlib import Path
from types import ModuleType


_SRC_DIR = Path(__file__).resolve().parent


def _alias_package(alias: str, target: str) -> ModuleType:
    module = sys.modules.get(alias)
    if module is None:
        module = ModuleType(alias)
        module.__file__ = str(_SRC_DIR / target / "__init__.py")
        module.__path__ = [str(_SRC_DIR / target)]
        module.__package__ = alias
        sys.modules[alias] = module
    parent_name, _, attr = alias.rpartition(".")
    parent = sys.modules.get(parent_name)
    if parent is not None:
        setattr(parent, attr, module)
    return module


_alias_package(f"{__name__}.API", "api")
_alias_package(f"{__name__}.API.Controllers", "api/controllers")
_alias_package(f"{__name__}.API.Interfaces", "api/interfaces")
_alias_package(f"{__name__}.Infra", "infra")
_alias_package(f"{__name__}.Infra.Mapper", "infra/mapper")
>>>>>>> example
