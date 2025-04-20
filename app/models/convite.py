from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from sqlalchemy.dialects.sqlite import JSON
from uuid import uuid4
from datetime import datetime
from app.database import Base

class Convite(Base):
    __tablename__ = "convites"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    time_criador_id = Column(String, ForeignKey("times.id"), nullable=False)
    data = Column(Date, nullable=False)
    horario = Column(String, nullable=False)  # "15:00"
    local = Column(String, nullable=False)
    tipo_campo = Column(String, nullable=True)  # "Campo grande", "Society"
    observacoes = Column(String, nullable=True)
    status = Column(String, default="aberto")  # "aberto", "confirmado", "cancelado"
    criado_em = Column(DateTime, default=datetime.utcnow)
