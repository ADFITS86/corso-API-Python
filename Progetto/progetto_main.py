#importo progetto
from fastapi.middleware.cors import CORSMiddleware
from .progetto_db import dbinit
from .progetto_film import router as film_router

#inizializzo il DB
dbinit()
from fastapi import FastAPI
# 1. Importiamo l'oggetto router dal file progetto_prodotti.py
from .progetto_prodotti import router as prodotti_router
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)
app.include_router(film_router)
# 2. Agganciamo il router all'applicazione principale
app.include_router(prodotti_router)
@app.get("/")
def home() :
    return {"info": "Server principale attivo"}