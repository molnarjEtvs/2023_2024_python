import random
class Jatekos:
    def __init__(self,nev,rang,szint,hatekonysag):
        self.nev = nev
        self.rang = rang
        self.szint = szint
        self.hatekonysag = hatekonysag

    def teljesitmenyGeneralas(self):
        self.teljesitmenyek = []
        for _ in range(5):
            self.teljesitmenyek.append(round(random.uniform(1.1,5.0),1))
    
    def hatekonysagNoveles(self):
        hatekonysag = sum(self.teljesitmenyek)/len(self.teljesitmenyek)
        self.hatekonysag += hatekonysag
    
    def rangFrissites(self,ujRang):
        if ujRang>self.rang:
            self.rang = ujRang
            return True
        else:
            return False
        
jatekosok = []

f = open("karakterek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    jatekos1 = Jatekos(adatok[0],int(adatok[1]),adatok[2],float(adatok[3]))
    jatekos1.teljesitmenyGeneralas()
    jatekos1.hatekonysagNoveles()
    jatekos1.rangFrissites(random.randint(20,50))
    jatekosok.append(jatekos1)
    del jatekos1
f.close()

i = open("ujKarakterek.txt","w",encoding="utf-8")
for jatekoska in jatekosok:
    i.write(f"Név: {jatekoska.nev}\n")
    i.write(f"Rang: {jatekoska.rang}\n")
    i.write(f"Szint: {jatekoska.szint}\n")
    i.write(f"Hatékonysag: {jatekoska.hatekonysag}%\n")
    if sum(jatekoska.teljesitmenyek)>10:
        i.write("KIVÁLÓ\n")
    i.write("#################################\n")
i.close()



