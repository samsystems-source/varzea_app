from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.convite import ConviteCreate, ConviteOut
from app.crud import convite as crud_convite
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=ConviteOut)
def criar_convite(convite: ConviteCreate, db: Session = Depends(get_db)):
    return crud_convite.criar_convite(db, convite)

@router.get("/", response_model=list[ConviteOut])
def listar_convites(db: Session = Depends(get_db)):
    return crud_convite.listar_convites(db)

@router.get("/{convite_id}", response_model=ConviteOut)
def buscar_convite(convite_id: str, db: Session = Depends(get_db)):
    convite = crud_convite.buscar_convite_por_id(db, convite_id)
    if not convite:
        raise HTTPException(status_code=404, detail="Convite não encontrado")
    return convite

@router.put("/{convite_id}/cancelar", response_model=ConviteOut)
def cancelar_convite(convite_id: str, db: Session = Depends(get_db)):
    convite = crud_convite.cancelar_convite(db, convite_id)
    if not convite:
        raise HTTPException(status_code=404, detail="Convite não encontrado ou já cancelado")
    return convite
