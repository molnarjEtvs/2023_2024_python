import random
class Hitel:
    def __init__(self,nev,osszeg,thm,futamido):
        self.nev = nev
        self.osszeg = osszeg
        self.thm = thm
        self.futamido = futamido
        self.kedvezmeny = 0

    def kamatKedvezmeny(self,kedvezmeny):
        self.thm -= kedvezmeny
        self.kedvezmeny = kedvezmeny

    def torlesztoSzamitas(self):
        self.haviTorleszto = round(self.osszeg*(1+self.thm/100)/self.futamido)

    def ugyfelSzamKeszites(self):
        self.ugyfelszam = random.randint(11111,99999)

hitelek = []
f = open("hitelek.htx","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    hitel1 = Hitel(adatok[0],int(adatok[1]),float(adatok[2]),int(adatok[3]))
    hitel1.ugyfelSzamKeszites()
    hitel1.kamatKedvezmeny(random.randint(0,2))
    hitel1.torlesztoSzamitas()
    hitelek.append(hitel1)
    del hitel1
f.close()


i = open("hitelAdatok.txt","w",encoding="utf-8")
for egyHitel in hitelek:
    i.write(f"Ügyfélszám: {egyHitel.ugyfelszam}\n")
    i.write(f"Név: {egyHitel.nev}\n")
    i.write(f"Összeg: {egyHitel.osszeg} Ft\n")
    i.write(f"Futamidő: {egyHitel.futamido} hó\n")
    i.write(f"THM: {egyHitel.thm}%\n")
    i.write(f"Kamatkedvezmény: {egyHitel.kedvezmeny}%\n")
    i.write(f"Havi törlesztő: {egyHitel.haviTorleszto} Ft\n")
    i.write("++++++++++++++++++++++++++++++++++++\n")
i.close()