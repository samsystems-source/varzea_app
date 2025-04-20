from sqlalchemy.orm import Session
from app.models.convite import Convite
from app.schemas.convite import ConviteCreate

def criar_convite(db: Session, convite: ConviteCreate):
    novo_convite = Convite(**convite.dict())
    db.add(novo_convite)
    db.commit()
    db.refresh(novo_convite)
    return novo_convite

def listar_convites(db: Session):
    return db.query(Convite).filter(Convite.status == "aberto").all()

def buscar_convite_por_id(db: Session, convite_id: str):
    return db.query(Convite).filter(Convite.id == convite_id).first()

def cancelar_convite(db: Session, convite_id: str):
    convite = buscar_convite_por_id(db, convite_id)
    if convite:
        convite.status = "cancelado"
        db.commit()
    return convite
