from fastapi import FastAPI
from pydantic import BaseModel
from router import router

from Controllers import AgendaController

app = FastAPI()

app.include_router(router)

def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)