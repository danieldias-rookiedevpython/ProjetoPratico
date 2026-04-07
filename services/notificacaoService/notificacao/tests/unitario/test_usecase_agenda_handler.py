import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../src")))

from modules.notificacao.Application.UseCases.exampleHandler import UseCasesAgenda

@pytest.mark.parametrize("name", ["Ana", "Carlos", "Maria"])
def test_create_agendamento_varios_nomes(name):
    usecase = UseCasesAgenda()

    result = usecase.create_agendamento(name)

    assert result["message"] == f"Agendamento criado para {name}"

def test_create_agendamento_sucesso():
    usecase = UseCasesAgenda()
    result = usecase.create_agendamento("Felipe")

    assert result["message"] == "Agendamento criado para Felipe"


def test_create_agendamento_sem_nome_deve_erro():
    usecase = UseCasesAgenda()

    with pytest.raises(ValueError):
        usecase.create_agendamento("")


@pytest.mark.parametrize("name", ["Ana", "Carlos", "Maria"])
def test_create_agendamento_varios_nomes(name):
    usecase = UseCasesAgenda()

    result = usecase.create_agendamento(name)

    assert result["message"] == f"Agendamento criado para {name}"