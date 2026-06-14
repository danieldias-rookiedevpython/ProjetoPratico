import sys

from . import Controllers as _controllers

sys.modules[f"{__name__}.controllers"] = _controllers
sys.modules[f"{__name__}.Controllers"] = _controllers