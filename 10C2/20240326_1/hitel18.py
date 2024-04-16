import random
class Hitel:
    def __init__(self,nev,osszeg,thm,futamido):
        self.nev = nev
        self.osszeg = osszeg
        self.thm = thm
        self.futamido = futamido
        self.kedvezmeny = 0

    def kamatKedvezmeny(self,kedvezmeny):
        self.thm-=kedvezmeny
        self.kedvezmeny = kedvezmeny

    def torelesztoSzamitas(self):
        self.haviTorleszto = round(self.osszeg*(1+self.thm)/self.futamido)

    def ugyfelszamKeszites(self):
        self.ugyfelszam = random.randint(11111,99999)

hitelek = []
f = open("hitelek.htx","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    hitel1 = Hitel(adatok[0],int(adatok[1]),float(adatok[2]),int(adatok[3]))
    hitel1.ugyfelszamKeszites()
    hitel1.kamatKedvezmeny(random.randint(0,2))
    hitel1.torelesztoSzamitas()
    hitelek.append(hitel1)
    del hitel1
f.close()


i = open("hitelAdatok.txt","w",encoding="utf-8")
for egyhitel in hitelek:
    i.write(f"Ügyfélszám: {egyhitel.ugyfelszam}\n")
    i.write(f"Név: {egyhitel.nev}\n")
    i.write(f"Összeg: {egyhitel.osszeg} Ft\n")
    i.write(f"Futamidő: {egyhitel.futamido} hó\n")
    i.write(f"THM: {egyhitel.thm} %\n")
    i.write(f"Kamatkedvezmény: {egyhitel.kedvezmeny} %\n")
    i.write(f"Havi törlesztő: {egyhitel.haviTorleszto} Ft\n")
    i.write("+++++++++++++++++++++++++++++++\n")
    

i.close()