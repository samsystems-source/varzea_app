from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.time import TimeCreate, TimeOut
from app.crud import time as crud_time
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=TimeOut)
def criar_time(time: TimeCreate, db: Session = Depends(get_db)):
    return crud_time.criar_time(db, time)

@router.get("/", response_model=list[TimeOut])
def listar_times(db: Session = Depends(get_db)):
    return crud_time.listar_times(db)

@router.get("/{time_id}", response_model=TimeOut)
def buscar_time(time_id: str, db: Session = Depends(get_db)):
    db_time = crud_time.buscar_time_por_id(db, time_id)
    if not db_time:
        raise HTTPException(status_code=404, detail="Time não encontrado")
    return db_time
