from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
import structlog

from src.API.Controllers.AgendaController import routerAgenda

logger = structlog.get_logger()

app = FastAPI(
    title="Agenda Service",
    version="1.0.0",
    description="CRUD de agendamento"
)

app.include_router(routerAgenda)

@app.get("/health")
def health():
    logger.info("health_check_executado")

    return {
        "status": "Healthy"
    }

Instrumentator().instrument(app).expose(app)

# Main
def main():
    import uvicorn

    logger.info("iniciando_servidor")

    uvicorn.run(
        "src.server:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )

if __name__ == "__main__":
    main()