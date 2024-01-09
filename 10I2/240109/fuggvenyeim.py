import random
def eldont(szam):
    if szam>0:
        print("Pozitív")
    elif szam<0:
        print("Negatív")
    else:
        print("Nulla")

def muvelet(mjel,szam1,szam2):
    if mjel == "*":
        return szam1*szam2
    elif mjel == "+":
        return szam1+szam2
    elif mjel == "-":
        return szam1-szam2
    elif mjel == "/":
        if szam2 == 0:
            return "Nullával nem osztunk"
        else:
            return szam1/szam2
    else:
        return "nincs ilyen művelet"

def veletlenSzamok(db,mettol,meddig):
    szamok = []
    for _ in range(db):
        szam = random.randint(mettol,meddig)
        szamok.append(szam)
    return szamok

def parosSzamok(szamok):
    csakParos = []
    for szam in szamok:
        if szam%2==0:
            csakParos.append(szam)
    return csakParos