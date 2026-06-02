from fastapi import FastAPI

from src.modules.email.api.router import router as email_router
from src.modules.userBell.api.router import router as user_bell_router


app = FastAPI(
    title="Notification Service",
    version="1.0.0",
    description="Servico de notificacoes orientado a features.",
)

app.include_router(email_router)
app.include_router(user_bell_router)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}


def main():
    import uvicorn

    uvicorn.run("src.server:app", host="127.0.0.1", port=8003, reload=True)
