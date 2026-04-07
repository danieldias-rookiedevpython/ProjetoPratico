from sqlalchemy.orm import Session
from sqlalchemy import select
from ..Config.db.liteSql.liteSql import get_query  # função que retorna Session ou contexto
from ..Models.UserSqlSchamy import Usuario  # seu modelo de usuário

class UserRepository:
    
    # ========================
    # CREATE
    # ========================
    def save(
        self, 
        userName:str,
        name: str, 
        email: str, 
        senha: str, 
        role=None, 
        cargo=None, 
        query=get_query
    ) -> Usuario:
        """Cria um usuário e retorna o objeto."""
        with query() as session:
            user = Usuario(
                nome=name,
                email=email,
                senha=senha,
                role=role if role else Usuario.role.default.arg,
                cargo=cargo if cargo else Usuario.cargo.default.arg
            )
            session.add(user)
            session.commit()
            session.refresh(user)
            return user

    # ========================
    # READ
    # ========================
    def find_all(self, name: str, query=get_query) -> Usuario | None:
        with query() as session:
            return session.query(Usuario).all()

    def find_by_id(self, id: int, query=get_query) -> Usuario | None:
        with query() as session:
            return session.query(Usuario).filter(Usuario.id == id).first()

    def find_by_email(self, email: str, query=get_query) -> Usuario | None:
        with query() as session:
            return session.query(Usuario).filter(Usuario.email == email).first()

    def find_by_username(self, name: str, query=get_query) -> Usuario | None:
        # alias de get_user
          with query() as session:
             return session.query(Usuario).filter(Usuario.userName == name).first()


    # ========================
    # UPDATE
    # ========================
    def update(self, id: int, *kwargs, query=get_query) -> Usuario | None:
        """
        Atualiza campos do usuário pelo id.
        Ex: update_user(1, nome="Novo Nome", role=UserRoleEnum.ADMIN)
        """
        with query() as session:
            user = session.query(Usuario).filter(Usuario.id == id).first()
            if not user:
                return None
            for key, value in kwargs.items():
                if hasattr(user, key):
                    setattr(user, key, value)
            session.commit()
            session.refresh(user)
            return user

    # ========================
    # DELETE
    # ========================
    def delete(self, id: int, query=get_query) -> bool:
        with query() as session:
            user = session.query(Usuario).filter(Usuario.id == id).first()
            if not user:
                return False
            session.delete(user)
            session.commit()
            return True

    # ========================
    # LIST
    # ========================
