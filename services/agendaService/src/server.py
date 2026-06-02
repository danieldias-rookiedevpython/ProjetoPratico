from fastapi import FastAPI

from src.api.router import api_router
from src.infra.clients import DatadogClient


DatadogClient().configure()


app = FastAPI(
    title="Agenda Service",
    version="1.0.0",
    description="servico de agendamento de consultas medicas",
)

app.include_router(api_router)


def main():
    import uvicorn

    uvicorn.run("src.server:app", host="127.0.0.1", port=8000, reload=True)
