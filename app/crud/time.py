from sqlalchemy.orm import Session
from app.models.time import Time
from app.schemas.time import TimeCreate

def criar_time(db: Session, time: TimeCreate):
    novo_time = Time(**time.dict())
    db.add(novo_time)
    db.commit()
    db.refresh(novo_time)
    return novo_time

def listar_times(db: Session):
    return db.query(Time).all()

def buscar_time_por_id(db: Session, time_id: str):
    return db.query(Time).filter(Time.id == time_id).first()
