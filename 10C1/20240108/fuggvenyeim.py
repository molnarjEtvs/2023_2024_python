import random
def eldontes(szam):
    if szam>0:
        print("Pozitív szám")
    elif szam<0:
        print("Negatív szám")
    else:
        print("ez nulla")

def eredmeny(muveletiJel,szam1,szam2):
    if muveletiJel == "*":
        return szam1*szam2
    elif muveletiJel == "+":
        return szam1+szam2
    elif muveletiJel == "-":
        return szam1-szam2
    else:
        if szam2==0:
            return "0-val nem osztunk"
        return szam1/szam2
    
def veletlenSzamok(db,mettol,meddig):
    szamok = []
    for _ in range(db):
        vszam = random.randint(mettol,meddig)
        szamok.append(vszam)
    return szamok


def parosak(lista):
    parosak = []
    for szam in lista:
        if szam%2==0:
            parosak.append(szam)
    return parosak

def legrovidebbSzo(szavak):
    lSzo = szavak[0]
    for szo in szavak:
        if len(lSzo)>len(szo):
            lSzo = szo
    return lSzo