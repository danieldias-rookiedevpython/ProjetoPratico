from fastapi import FastAPI
from pydantic import BaseModel
from src.API.Controllers.UserController import routerUsers
from src.Auth.router import routerAuth

app = FastAPI()

#middleware global aki
'''
@app.middleware("http")
async def add_process_time_header(request, call_next):
    
   
    print("ANTES DA ROTA")

    response = await call_next(request)

    print("DEPOIS DA ROTA")

    return response
'''


app.include_router(routerUsers)
app.include_router(routerAuth)

def main():
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3004)