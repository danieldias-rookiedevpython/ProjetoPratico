from ...Infra.RepoAdapter.UserRepository import UserRepository
from .tokenJwt import TokenService 
from .validateLogin import ValidateLoginService 


def loginService(password: str, email: str='', name: str=''):

   if(email=='' and password=='' and name==''):
       raise ValueError(" valores invalidos")
   
   if(email=='' and name!='' and password!=''):
       user = UserRepository.find_by_username(name)
       if not user:
            raise ValueError(" valores invalidos")

   if(email!='' and name=='' and password!=''):
        user = UserRepository.find_by_email(email)
        if not user:
            raise ValueError(" valores invalidos")
        
   is_valid = ValidateLoginService.validate_password(password, user.password)
   if not is_valid:
            return None
        
   token = TokenService.generate_token(user.id)
   
   if not token:
            return None

   return {id:user.id, token: token}
    
  