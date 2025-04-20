from sqlalchemy.orm import Session
from app.models.feedback import Feedback
from app.schemas.feedback import FeedbackCreate

def criar_feedback(db: Session, feedback: FeedbackCreate):
    novo_feedback = Feedback(**feedback.dict())
    db.add(novo_feedback)
    db.commit()
    db.refresh(novo_feedback)
    return novo_feedback

def listar_feedbacks_por_jogo(db: Session, jogo_id: str):
    return db.query(Feedback).filter(Feedback.jogo_id == jogo_id).all()

def listar_feedbacks_por_time(db: Session, time_id: str):
    return db.query(Feedback).filter(Feedback.time_id == time_id).all()
