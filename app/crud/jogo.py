from sqlalchemy.orm import Session
from app.models.jogo import Jogo
from app.models.convite import Convite
from app.schemas.jogo import JogoCreate, JogoUpdate

def criar_jogo(db: Session, jogo: JogoCreate):
    # Atualiza status do convite
    convite = db.query(Convite).filter(Convite.id == jogo.convite_id).first()
    if convite:
        convite.status = "confirmado"
    novo_jogo = Jogo(**jogo.dict())
    db.add(novo_jogo)
    db.commit()
    db.refresh(novo_jogo)
    return novo_jogo

def listar_jogos(db: Session):
    return db.query(Jogo).all()

def buscar_jogo_por_id(db: Session, jogo_id: str):
    return db.query(Jogo).filter(Jogo.id == jogo_id).first()

def atualizar_placar(db: Session, jogo_id: str, update: JogoUpdate):
    jogo = buscar_jogo_por_id(db, jogo_id)
    if jogo:
        if update.placar_time_criador is not None:
            jogo.placar_time_criador = update.placar_time_criador
        if update.placar_time_convidado is not None:
            jogo.placar_time_convidado = update.placar_time_convidado
        db.commit()
        db.refresh(jogo)
    return jogo
