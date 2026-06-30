from pydantic import BaseModel
#Dichiaro l' ogetto per validare le richiesta
class ProdottoIn(BaseModel):
    nome:str
    prezzo: float