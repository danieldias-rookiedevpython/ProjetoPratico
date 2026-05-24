from fastapi import APIRouter
routerAgenda = APIRouter(
    prefix="/agenda", 
    tags=["Agenda"],
    #dependencies= Depends(hookFunction)
)