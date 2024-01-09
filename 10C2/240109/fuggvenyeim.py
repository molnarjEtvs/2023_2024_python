import random
def eldont(szam):
    if szam>0:
        print("Pozitív")
    elif szam<0:
        print("Negatív")
    else:
        print("Nullla")


def muveletVegzes(muveletiJel,szam1,szam2):
    if muveletiJel == "*":
        return szam1*szam2
    elif muveletiJel == "+":
        return szam1+szam2
    elif muveletiJel == "-":
        return szam1-szam2
    elif muveletiJel=="/":
        if szam2==0:
            return "nullával nem osztunk"
        else:
            return szam1/szam2
    else:
        return "Nincs ilyen művelet jel"
    
def veletlenSzamok(db,mettol,meddig):
    szamok = []
    for _ in range(db):
        szam = random.randint(mettol,meddig)
        szamok.append(szam)
    return szamok

def parosSzamok(szamok):
    parosak = []
    for egy in szamok:
        if egy%2==0:
            parosak.append(egy)
    return parosak 