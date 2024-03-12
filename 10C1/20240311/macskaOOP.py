import random
class Macska:
    def __init__(self,nev,szin):
        self.nev = nev
        self.szin = szin
        self.suly = 9

    def nyavogas(self,ido):
        pass

macskak = []
f = open("macskak.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    macska1 = Macska(adatok[0],adatok[1])
    macska1.nyavogas(random.randint(5,10))
    macskak.append(macska1)
    del macska1
f.close()
