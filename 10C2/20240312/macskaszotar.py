macskak = []
#macska = {}
#macska["nev"] = "Cirmi"
#macska["szin"] = "Szürke"
#macskak.append(macska)
f = open("macskak.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip() #Cirmi;szürke
    sor = sor.split(";")#["Cirmi","szürke"]
    macska = {}
    macska["nev"] = sor[0]
    macska["szin"] = sor[1]
    macskak.append(macska)
f.close()

print(macskak)