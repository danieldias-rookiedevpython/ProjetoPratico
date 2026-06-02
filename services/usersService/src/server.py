from fastapi import FastAPI

from services.usersService.src.api.controllers import routerAdmins, routerAtendents, routerMedics, routerPacients


app = FastAPI(title="Users Service")

app.include_router(routerAdmins)
app.include_router(routerAtendents)
app.include_router(routerMedics)
app.include_router(routerPacients)


@app.get("/health", tags=["health"])
def health_check():
    return {"status": "ok"}


def main():
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=3004)
