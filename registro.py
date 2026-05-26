voti=["1","2","3","4"]
voti.append("5")
for p in voti:
    print("voto registrato:")
    print (p)

    corso={
        "nome": "web dev",
        "studenti":[
            {"nome": "Luca", "id":1},
            {"nome": "Sara", "id":2}
        ]
    }
print(corso["studenti"]["1"]["nome"])