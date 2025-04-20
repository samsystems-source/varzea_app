from fastapi import FastAPI
from app.database import engine, Base
from app.routers import time_router, convite_router, jogo_router, feedback_router

from fastapi.staticfiles import StaticFiles
from app.web import views as web_views

app = FastAPI(title="Varzea App - Marcação de Jogos")

Base.metadata.create_all(bind=engine)

app.include_router(time_router.router, prefix="/times", tags=["Times"])
app.include_router(convite_router.router, prefix="/convites", tags=["Convites"])
app.include_router(jogo_router.router, prefix="/jogos", tags=["Jogos"])
app.include_router(feedback_router.router, prefix="/feedbacks", tags=["Feedbacks"])

app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.include_router(web_views.router)