import random
class Mosogep:
    def __init__(self,marka,kapacitas,kw):
        self.marka = marka
        self.kapacitas = kapacitas
        self.kw = kw
        self.allapot = False
        self.energiaFogyasztas = 0

    def bekapcsolas(self):
        if self.allapot == False:
            self.allapot = True
    
    def mosas(self,ido):
        if self.allapot == True:
            self.energiaFogyasztas += (ido/100*self.kw)
            return True
        else:
            return False

    def centrifugalas(self,fordulatszam):
        if fordulatszam<=800:
            self.energiaFogyasztas += 2
        else:
            self.energiaFogyasztas += 3

mosogepek = []
fordulatSzamok = [800,1000,1200]

f = open("mosogepek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    mosogep1 = Mosogep(adatok[0],float(adatok[1]),float(adatok[2]))
    mosogep1.bekapcsolas()
    mosogep1.mosas(random.randint(80,150))
    mosogep1.centrifugalas(random.choice(fordulatSzamok))
    mosogepek.append(mosogep1)
    del mosogep1
f.close()

i = open("mosasok.txt","w",encoding="utf-8")
for egyMosogep in mosogepek:
    i.write(f"Márka: {egyMosogep.marka}\n")
    i.write(f"Energia: {egyMosogep.kw} kw\n")
    i.write(f"Kapacitás: {egyMosogep.kapacitas} kg\n")
    i.write(f"Energia fogyasztás: {round(egyMosogep.energiaFogyasztas,2)} kw\n")
    if egyMosogep.energiaFogyasztas>4:
        i.write("MAGAS ENERGIAFELHASZNÁLÁS!\n")
    i.write("-----------------------------\n")
i.close()