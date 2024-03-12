class Macska:
    def __init__(self,nev,szin):
        self.nev = nev
        self.szin = szin

macskak = []
f = open("macska.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    macska1 = Macska(adatok[0],adatok[1])
    macskak.append(macska1)
    del macska1
f.close()

print(f"{macskak[2].nev}")