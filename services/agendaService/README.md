# Guia de Comandos — Projeto com Poetry, FastAPI e Mypy

Este documento reúne os principais comandos para criar, configurar e executar um projeto utilizando **Poetry**, **FastAPI** e **Mypy**.

---

## 1. Instalar o Poetry

```bash
pip install poetry
```

Verificar instalação:

```bash
poetry --version
```

---

## 2. Criar um novo projeto

```bash
poetry new nome_do_projeto
```

Ou iniciar em um diretório existente:

```bash
poetry init
```

Entrar no diretório:

```bash
cd nome_do_projeto
```

---

## 3. Criar ambiente virtual

```bash
poetry install
```

---

## 4. Adicionar dependências

### FastAPI

```bash
poetry add fastapi
```

### Uvicorn (servidor ASGI)

```bash
poetry add uvicorn
```

### Mypy (como dependência de desenvolvimento)

```bash
poetry add --group dev mypy
```

---

## 5. Estrutura básica do projeto

Exemplo de estrutura:

```
nome_do_projeto/
├── pyproject.toml
├── nome_do_projeto/
│   └── main.py
└── tests/
```

---

## 6. Exemplo básico de aplicação FastAPI

`main.py`

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Hello World"}
```

---

## 7. Executar a aplicação

```bash
poetry run uvicorn nome_do_projeto.main:app --reload
```

---

## 8. Executar o Mypy

Verificação simples:

```bash
poetry run mypy .
```

Criar arquivo de configuração opcional:

`mypy.ini`

```ini
[mypy]
python_version = 3.11
strict = True
ignore_missing_imports = True
```

Executar novamente:

```bash
poetry run mypy nome_do_projeto
```

---

## 9. Scripts no pyproject.toml

Você pode adicionar atalhos no `pyproject.toml`:

```toml
[tool.poetry.scripts]
start = "uvicorn nome_do_projeto.main:app --reload"
check = "mypy nome_do_projeto"
```

Executar:

```bash
poetry run start
poetry run check
```

---

## 10. Atualizar dependências

```bash
poetry update
```

---

## 11. Exportar requirements.txt (opcional)

```bash
poetry export -f requirements.txt --output requirements.txt --without-hashes
```

---

## 12. Remover dependência

```bash
poetry remove nome_da_dependencia
```

---

## 13. Ver dependências instaladas

```bash
poetry show
```

---

# Fluxo Resumido

```bash
poetry new api
cd api
poetry add fastapi uvicorn
poetry add --group dev mypy
poetry install
poetry run uvicorn api.main:app --reload
poetry run mypy .
```

---

# 14. Como fazer o Poetry rodar scripts no terminal

Existem **duas formas corretas** de rodar scripts com Poetry:

## ✅ 1) Usando `poetry run` (forma mais simples)

Você pode executar qualquer comando instalado no ambiente virtual assim:

```bash
poetry run python main.py
poetry run uvicorn api.main:app --reload
poetry run mypy .
```

Isso garante que o comando será executado dentro do ambiente virtual gerenciado pelo Poetry.

---

## ✅ 2) Criando comandos próprios (entry points)

No `pyproject.toml`, você pode definir comandos que chamam **funções Python**, não comandos shell diretos:

```toml
[tool.poetry.scripts]
start = "api.main:main"
```

E no seu `main.py`:

```python
from fastapi import FastAPI
import uvicorn

app = FastAPI()


def main() -> None:
    uvicorn.run("api.main:app", reload=True)
```

Agora você pode executar:

```bash
poetry run start
```

⚠️ Importante: `tool.poetry.scripts` funciona como `console_scripts` do setuptools — ele precisa apontar para uma função Python executável.

---

## ✅ 3) Criando "atalhos" para comandos (melhor prática)

Se você quiser criar atalhos como `start`, `check`, `lint`, etc., uma abordagem mais limpa é usar plugins como **taskipy**:

```bash
poetry add --group dev taskipy
```

No `pyproject.toml`:

```toml
[tool.taskipy.tasks]
start = "uvicorn api.main:app --reload"
check = "mypy ."
```

Executar:

```bash
poetry run task start
poetry run task check
```

Essa abordagem é mais flexível para projetos maiores.

---

Documento base para projetos Python modernos com tipagem estática e API REST utilizando FastAPI.
