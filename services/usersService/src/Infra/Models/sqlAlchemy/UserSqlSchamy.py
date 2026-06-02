import enum

from sqlalchemy import Enum as SAEnum
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from ...config.db.liteSql.LiteSql import Base


class CargoEnum(str, enum.Enum):
    ADMIN = "ADMIN"
    MEDICO = "MEDICO"
    ATENDENTE = "ATENDENTE"
    GERENTE = "GERENTE"
    SUPERVISOR = "SUPERVISOR"
    PACIENTE = "PACIENTE"


class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    userName: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    nome: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(String, nullable=False)
    cargo: Mapped[CargoEnum] = mapped_column(
        SAEnum(CargoEnum, name="cargo_enum"),
        nullable=False,
        default=CargoEnum.PACIENTE,
    )
