import sqlite3
from fastapi import FastAPI, HTTPException
app = FastAPI()

@app.get("/utente")
def root():
    return {"nome":"ANDREA","cognome":"DI FRANCESCO"}

@app.get("/saluta/{nome}")
def saluta_utente(nome: str):
    return {"messaggio": f"Ciao {nome}!"}

@app.get("/ricerca")
def cerca(item: str, q: int = 1):
    return {"risultato": item, "quantita": q}

@app.get("/somma/{n1}/{n2}")
def somma(n1:int , n2:int,):
    addizione= n1+n2
    if n1==1 and n2==1:
        raise HTTPException (status_code=400, detail="Operazione non valida")
   # match variabile:
       # case "valore1" | "oAncheValore2":
          #  return {}
    return {"risultato": addizione}

@app.get("/prodotti")
def ottieni_prodotti():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row # Conversione attiva!
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM prodotti")
    risultato = cursor.fetchall()
    conn.close()
    return risultato

@app.get("/prodotti/ricerca")
def cerca_prodotto(keyword: str):
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM prodotti WHERE nome LIKE ?",
        (f"%{keyword}%",)
    )
    risultati = cursor.fetchall()
    conn.close()
    return risultati


