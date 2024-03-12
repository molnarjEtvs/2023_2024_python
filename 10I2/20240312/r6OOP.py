class Operator:
    def __init__(self,nev,fegyver,eletero):
        self.nev = nev
        self.fegyver = fegyver
        self.eletero = eletero

operatorok = []
f = open("r6.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip() #Tachanka|Nagypapi|3
    adatok = sor.split("|")#["Tachanka","Nagypapi","3"]
    operator1 = Operator(adatok[0],adatok[1],int(adatok[2]))
    operatorok.append(operator1)
    del operator1
f.close()