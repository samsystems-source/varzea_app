from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.sqlite import JSON
from uuid import uuid4
from datetime import datetime

from app.database import Base

class Time(Base):
    __tablename__ = "times"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    nome = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    responsavel = Column(String, nullable=False)
    contato = Column(String, nullable=False)
    dias_disponiveis = Column(JSON, nullable=True)
    horario_preferido = Column(String, nullable=True)
    local_fixo = Column(String, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)
