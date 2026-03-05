FROM python:3.12-slim

WORKDIR /app

# Instala Poetry
RUN pip install poetry

# Copia apenas arquivos de dependência primeiro (cache inteligente)
COPY pyproject.toml poetry.lock* ./

# Instala dependências sem criar virtualenv
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copia código
COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]