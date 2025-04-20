from sqlalchemy import Column, String, DateTime, ForeignKey, Integer
from uuid import uuid4
from datetime import datetime
from app.database import Base

class Jogo(Base):
    __tablename__ = "jogos"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    convite_id = Column(String, ForeignKey("convites.id"), nullable=False)
    time_convidado_id = Column(String, ForeignKey("times.id"), nullable=False)
    confirmado_em = Column(DateTime, default=datetime.utcnow)

    placar_time_criador = Column(Integer, nullable=True)
    placar_time_convidado = Column(Integer, nullable=True)
