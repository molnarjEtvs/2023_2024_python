import random
class Suti:
    def __init__(self,nev,tipus,ar,egyseg):
        self.nev = nev
        self.tipus = tipus
        self.ar = ar
        self.egyseg = egyseg
        self.eladas = 0
        self.bevetel = 0
    
    def EladasGeneralas(self):
        return random.randint(100,500)
    
    def BevetelSzamitas(self):
        self.bevetel = self.eladas*self.ar

sutemenyek = []

f = open("cuki.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    suti1 = Suti(adatok[0],adatok[1],int(adatok[2]),adatok[3])
    suti1.eladas = suti1.EladasGeneralas()
    suti1.BevetelSzamitas()
    sutemenyek.append(suti1)
    del suti1
f.close()

i = open("sutik.txt","w",encoding="utf-8")
for sutike in sutemenyek:
    i.write(f"Sütemény neve: {sutike.nev}\n")
    i.write(f"A sütemény kiszerelése: {sutike.egyseg}\n")
    i.write(f"Eladott mennyiség: {sutike.eladas} {sutike.egyseg}\n")
    i.write(f"Bevétel: {sutike.bevetel} Ft\n")
    if sutike.bevetel>150000:
        i.write(f"NÉPSZERŰ\n")
    i.write("------------------------------\n")
i.close()