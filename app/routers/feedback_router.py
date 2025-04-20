from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.feedback import FeedbackCreate, FeedbackOut
from app.crud import feedback as crud_feedback
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=FeedbackOut)
def criar_feedback(feedback: FeedbackCreate, db: Session = Depends(get_db)):
    return crud_feedback.criar_feedback(db, feedback)

@router.get("/jogo/{jogo_id}", response_model=list[FeedbackOut])
def feedbacks_do_jogo(jogo_id: str, db: Session = Depends(get_db)):
    return crud_feedback.listar_feedbacks_por_jogo(db, jogo_id)

@router.get("/time/{time_id}", response_model=list[FeedbackOut])
def feedbacks_do_time(time_id: str, db: Session = Depends(get_db)):
    return crud_feedback.listar_feedbacks_por_time(db, time_id)
