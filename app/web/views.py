from fastapi import APIRouter, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models.time import Time
from app.schemas.time import TimeCreate
from app.crud import time as crud_time

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/login", response_class=HTMLResponse)
def login_get(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.post("/login")
def login_post(request: Request, nome: str = Form(...), db=Depends(get_db)):
    time = db.query(Time).filter(Time.nome == nome).first()
    if time:
        response = RedirectResponse(url=f"/dashboard/{time.id}", status_code=302)
        return response
    return templates.TemplateResponse("login.html", {"request": request, "erro": "Time não encontrado"})

@router.get("/dashboard/{time_id}", response_class=HTMLResponse)
def dashboard(request: Request, time_id: str, db=Depends(get_db)):
    time = db.query(Time).filter(Time.id == time_id).first()
    return templates.TemplateResponse("dashboard.html", {"request": request, "time": time})


@router.get("/cadastro", response_class=HTMLResponse)
def cadastro_get(request: Request):
    return templates.TemplateResponse("cadastro.html", {"request": request})

@router.post("/cadastro")
def cadastro_post(
    request: Request,
    nome: str = Form(...),
    bairro: str = Form(...),
    responsavel: str = Form(...),
    contato: str = Form(...),
    dias_disponiveis: str = Form(...),  # exemplo: "sábado,domingo"
    horario_preferido: str = Form(""),
    local_fixo: str = Form(""),
    db: Session = Depends(get_db)
):
    dados = TimeCreate(
        nome=nome,
        bairro=bairro,
        responsavel=responsavel,
        contato=contato,
        dias_disponiveis=[d.strip() for d in dias_disponiveis.split(",") if d.strip()],
        horario_preferido=horario_preferido or None,
        local_fixo=local_fixo or None,
    )
    novo_time = crud_time.criar_time(db, dados)
    return RedirectResponse(url=f"/dashboard/{novo_time.id}", status_code=302)
