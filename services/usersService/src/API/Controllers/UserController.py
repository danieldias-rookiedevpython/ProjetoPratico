from ..Interfaces.UseCasesUserInterface import IUseCasesCreateUser, IUseCasesDetailUser, IUseCasesListUser, IUseCasesDeleteUser, IUseCasesUpdateUser
from fastapi import APIRouter, Depends
from ..provider import useCaseCreateUser_factory, useCaseDeleteUser_factory, useCaseUpdateUser_factory, useCaseDetailUser_factory, useCaseListUser_factory 




routerUsers = APIRouter(
    prefix="/user", 
    tags=["uaser"],
    #dependencies= Depends(hookFunction)
)


@routerUsers.post(
        "/",
        #dependencies= Depends(hookFunction)
    )

def create_User(self, name: str,  useCase: IUseCasesCreateUser = Depends(useCaseCreateUser_factory)):
        return useCase.execute(name)
    



@routerUsers.put(
        "/",
        #dependencies= Depends(hookFunction)
    )
def update_User(self, name: str,  useCase: IUseCasesUpdateUser = Depends(useCaseUpdateUser_factory)):
        return useCase.execute(name)
    
    
    



@routerUsers.delete(
        "/",
        #dependencies= Depends(hookFunction)
    )
def delete_User(self, name: str,  useCase: IUseCasesDeleteUser = Depends(useCaseDeleteUser_factory)):
        return useCase.execute(name)
    



@routerUsers.get(
        "/",
        #dependencies= Depends(hookFunction)
    )
def list_User(self, name: str,  useCase: IUseCasesListUser = Depends(useCaseListUser_factory)):
            return useCase.execute(name)
    


@routerUsers.get(
        "/{userId}",
        #dependencies= Depends(hookFunction)
    )
def detail_User(self, name: str,  useCase: IUseCasesDetailUser = Depends(useCaseDetailUser_factory)):
            return useCase.execute(name)
    



    

    #admin metodes

    #super admin metodes