#macska = {}
#macska["nev"] = "Cirmi"
#macska["szin"] = "Szürke"

macskak = []

f = open("macska.txt","r",encoding="utf-8")
for row in f:
    row = row.strip() #row = Cirmi;szürke
    adatok = row.split(";")# adatok = ["Cirmi","szürke"]
    macska = {}
    macska["nev"] = adatok[0]
    macska["szin"] = adatok[1]
    macskak.append(macska)
f.close()

