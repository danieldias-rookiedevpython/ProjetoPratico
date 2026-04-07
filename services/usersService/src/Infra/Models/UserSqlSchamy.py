import enum
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SAEnum
from ..Config.db.liteSql.liteSql import Base  # seu Base

# ==============================
# Enums
# ==============================
class UserRoleEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    SUPERADMIN = "SUPERADMIN"
    USER = "USER"
    FUNCIONARIO = "FUNCIONARIO"
    MEDICO = "MEDICO"


class CargoEnum(str, enum.Enum):
    MEDICO = "MEDICO"
    ATENDENTE = "ATENDENTE"
    GERENTE = "GERENTE"
    SUPERVISOR = "SUPERVISOR"
    PACIENTE = "PACIENTE"
    
    
# ==============================
# Modelo de Usuário
# ==============================
class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userName: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String, nullable=False)

    role: Mapped[UserRoleEnum] = mapped_column(
        SAEnum(UserRoleEnum, name="user_role"),
        nullable=False,
        default=UserRoleEnum.USER,  # default corrigido
    )

    cargo: Mapped[CargoEnum] = mapped_column(
        SAEnum(CargoEnum, name="cargo_enum"),
        nullable=False,
        default=CargoEnum.PACIENTE,  # default corrigido
    )