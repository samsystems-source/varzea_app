from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.jogo import JogoCreate, JogoOut, JogoUpdate
from app.crud import jogo as crud_jogo
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=JogoOut)
def criar_jogo(jogo: JogoCreate, db: Session = Depends(get_db)):
    return crud_jogo.criar_jogo(db, jogo)

@router.get("/", response_model=list[JogoOut])
def listar_jogos(db: Session = Depends(get_db)):
    return crud_jogo.listar_jogos(db)

@router.get("/{jogo_id}", response_model=JogoOut)
def buscar_jogo(jogo_id: str, db: Session = Depends(get_db)):
    jogo = crud_jogo.buscar_jogo_por_id(db, jogo_id)
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return jogo

@router.put("/{jogo_id}/placar", response_model=JogoOut)
def atualizar_placar(jogo_id: str, update: JogoUpdate, db: Session = Depends(get_db)):
    jogo = crud_jogo.atualizar_placar(db, jogo_id, update)
    if not jogo:
        raise HTTPException(status_code=404, detail="Jogo não encontrado")
    return jogo
