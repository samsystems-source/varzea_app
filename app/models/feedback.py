from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from uuid import uuid4
from datetime import datetime
from app.database import Base

class Feedback(Base):
    __tablename__ = "feedbacks"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid4()))
    jogo_id = Column(String, ForeignKey("jogos.id"), nullable=False)
    time_id = Column(String, ForeignKey("times.id"), nullable=False)
    nota = Column(Integer, nullable=False)  # 1 a 5
    comentario = Column(String, nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)
