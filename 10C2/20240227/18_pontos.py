import math,random
class BankSzamla:
    def __init__(self,nev,egyenleg):
        self.nev = nev
        self.egyenleg = egyenleg
        self.dij = 0
    
    def befizetes(self,osszeg):
        self.egyenleg += osszeg
        self.dij -= 10
        if self.dij<0:
            self.dij = 0

    def kivetel(self,osszeg):
        if self.egyenleg>=osszeg:
            self.egyenleg-=osszeg
            self.dij += math.ceil(osszeg*0.0085)
            return True
        else:
            return False

szamlak = []
f = open("bankszamlak.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    szamla1 = BankSzamla(adatok[0],int(adatok[1]))
    szamla1.befizetes(random.randint(1000,10000))
    for _ in range(3):
        szamla1.kivetel(random.randint(1000,3000))
    szamlak.append(szamla1)
    del szamla1
f.close()

i = open("szamlaAdatok.txt","w",encoding="utf-8")
for egySzamla in szamlak:
    i.write(f"Ügyfél neve: {egySzamla.nev}\n")
    i.write(f"Egyenleg: {egySzamla.egyenleg} Ft\n")
    i.write(f"Számlavezetési díj: {egySzamla.dij} Ft\n")
    i.write("#######################\n")
i.close()
