import random
class Jatekos:
    def __init__(self,nev,rang,szint,hatekonysag):
        self.nev = nev
        self.rang = rang
        self.szint = szint
        self.hatekonysag = hatekonysag

    def teljesitmenyGeneralas(self):
        self.telsitmenyek = []
        for _ in range(5):
            self.telsitmenyek.append(round(random.uniform(1.1,5.0),1))
    
    def hatekonysagNoveles(self):
        atlag = sum(self.telsitmenyek)/len(self.telsitmenyek)
        self.hatekonysag += atlag

    def rangFrissites(self,ujRang):
        if ujRang>self.rang:
            self.rang = ujRang
            return True
        else:
            return False
        
karakterek = []
f = open("karakterek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    karakter1 = Jatekos(adatok[0],int(adatok[1]),adatok[2],float(adatok[3]))
    karakter1.teljesitmenyGeneralas()
    karakter1.hatekonysagNoveles()
    karakter1.rangFrissites(random.randint(20,50))
    karakterek.append(karakter1)
    del karakter1
f.close()

w = open("ujKarakterek.txt","w",encoding="utf-8")
for egy in karakterek:
    w.write(f"Név: {egy.nev}\n")
    w.write(f"Rang: {egy.rang}\n")
    w.write(f"Szint: {egy.szint}\n")
    w.write(f"Hatékonyság: {egy.hatekonysag}\n")
    print(egy.telsitmenyek)
    if sum(egy.telsitmenyek)>10:
        w.write("Kiváló\n")
    w.write("#######################\n")
w.close()