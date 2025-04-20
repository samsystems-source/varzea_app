from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class FeedbackBase(BaseModel):
    jogo_id: str
    time_id: str
    nota: int
    comentario: Optional[str] = None

class FeedbackCreate(FeedbackBase):
    pass

class FeedbackOut(FeedbackBase):
    id: str
    criado_em: datetime

    class Config:
        orm_mode = True
