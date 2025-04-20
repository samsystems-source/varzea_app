from pydantic import BaseModel
from typing import Optional
from datetime import date, datetime

class ConviteBase(BaseModel):
    time_criador_id: str
    data: date
    horario: str
    local: str
    tipo_campo: Optional[str] = None
    observacoes: Optional[str] = None

class ConviteCreate(ConviteBase):
    pass

class ConviteOut(ConviteBase):
    id: str
    status: str
    criado_em: datetime

    class Config:
        orm_mode = True
