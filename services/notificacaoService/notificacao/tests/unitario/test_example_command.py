import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from modules.notificacao.Application.UseCases.exampleCommand import ExampleCommand


def test_execute_sucesso():
    command = ExampleCommand()
    data = {"name": "Felipe"}

    result = command.execute(data)

    assert result["status"] == "success"
    assert result["data"] == data


def test_execute_sem_dados_deve_erro():
    command = ExampleCommand()

    with pytest.raises(ValueError):
        command.execute({})