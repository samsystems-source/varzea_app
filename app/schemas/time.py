from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class TimeBase(BaseModel):
    nome: str
    bairro: str
    responsavel: str
    contato: str
    dias_disponiveis: Optional[List[str]] = None
    horario_preferido: Optional[str] = None
    local_fixo: Optional[str] = None

class TimeCreate(TimeBase):
    pass

class TimeOut(TimeBase):
    id: str
    criado_em: datetime

    class Config:
        orm_mode = True
