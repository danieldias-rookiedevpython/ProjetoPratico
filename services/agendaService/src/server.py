from fastapi import FastAPI
from src.API.Controllers.AgendaController import routerAgenda

app = FastAPI(
    title="Agenda Service",
    version="1.0.0",
    description="CRUD de agendamento"
)

app.include_router(routerAgenda)


def main():
    import uvicorn
    uvicorn.run("src.server:app", host="127.0.0.1", port=8000, reload=True)