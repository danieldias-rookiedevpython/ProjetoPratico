import enum
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Enum as SAEnum
from ...Config.db.liteSql.liteSql import Base  # seu Base

# ==============================
# Enums
# ==============================

class CargoEnum(str, enum.Enum):
    MEDICO = "MEDICO"
    ATENDENTE = "ATENDENTE"
    GERENTE = "GERENTE"
    SUPERVISOR = "SUPERVISOR"
    PACIENTE = "PACIENTE"
    
    
# ==============================
# Modelo de Usuário
# ==============================
class Medic(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userName: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String, nullable=False)


    cargo: Mapped[CargoEnum] = mapped_column(
        SAEnum(CargoEnum, name="cargo_enum"),
        nullable=False,
        default=CargoEnum.PACIENTE,  # default corrigido
    )
    



class Atendente(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userName: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String, nullable=False)



    cargo: Mapped[CargoEnum] = mapped_column(
        SAEnum(CargoEnum, name="cargo_enum"),
        nullable=False,
        default=CargoEnum.PACIENTE,  # default corrigido
    )
    
    



class Paciente(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userName: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String, nullable=False)


    cargo: Mapped[CargoEnum] = mapped_column(
        SAEnum(CargoEnum, name="cargo_enum"),
        nullable=False,
        default=CargoEnum.PACIENTE,  # default corrigido
    )
    
    
    
    
    
    
class softPaciente(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userName: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String, nullable=False)

    cargo: Mapped[CargoEnum] = mapped_column(
        SAEnum(CargoEnum, name="cargo_enum"),
        nullable=False,
        default=CargoEnum.PACIENTE,  # default corrigido
    )