from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JogoBase(BaseModel):
    convite_id: str
    time_convidado_id: str

class JogoCreate(JogoBase):
    pass

class JogoUpdate(BaseModel):
    placar_time_criador: Optional[int]
    placar_time_convidado: Optional[int]

class JogoOut(JogoBase):
    id: str
    confirmado_em: datetime
    placar_time_criador: Optional[int]
    placar_time_convidado: Optional[int]

    class Config:
        orm_mode = True
    