
from fastapi import APIRouter, Header
from .services.tokenJwt import TokenService
from .services.login import loginService
from .bodyTypes import LoginBody



routerAuth = APIRouter(
    prefix="/Auth", 
    tags=["Auth"],
    #dependencies= Depends(hookFunction)
)



@routerAuth.get("/validate")
def validate_token(authorization: str = Header()):
   return TokenService.validate_token(authorization)


@routerAuth.post("/login")
def login(self, body:LoginBody):
    return loginService(body.password, body.email, body.name)