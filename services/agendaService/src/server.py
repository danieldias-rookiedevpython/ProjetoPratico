from fastapi import FastAPI
from pydantic import BaseModel
from Agenda.API.provider import  router_factory


app = FastAPI()

app.include_router(router_factory())

def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)