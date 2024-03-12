class Macska:
    def __init__(self,nev,szin):
        self.nev = nev
        self.szin = szin

macskak = []
f = open("macskak.txt","r",encoding="utf-8")
for row in f:
    row = row.strip() #Cirmi;szürke (nincs enter)
    row = row.split(";")# ["Cirmi","szürke"]
    macska1 = Macska(row[0],row[1])
    macskak.append(macska1)
    del macska1
f.close()

print(f"{macskak[1].szin}")
print(f"{macskak[2].nev}")