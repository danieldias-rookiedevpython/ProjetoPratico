import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from modules.notificacao.Application.UseCases.nameValidator import NameValidator


def test_name_valido():
    validator = NameValidator()

    result = validator.validate("Felipe")

    assert result is True


def test_name_vazio():
    validator = NameValidator()

    with pytest.raises(ValueError):
        validator.validate("")


def test_name_so_espaco():
    validator = NameValidator()

    with pytest.raises(ValueError):
        validator.validate("   ")