import random
def eldont(szam):
    if szam>0:
        print('Pozitív')
    elif szam<0:
        print("Negatív")
    else:
        print("nulla")

def muvelet(mjel,szam1,szam2):
    if mjel == "+":
        return szam1+szam2
    elif mjel == "-":
        return szam1-szam2
    elif mjel == "*":
        return szam1*szam2
    elif mjel == "/":
        if szam2 == 0:
            return "Nullával nem osztunk"
        else:
            return szam1/szam2
    else:
        return "Ismeretlen művelet"
def veletlenSzamok(db,mettol,meddig):
    szamok = []
    for _ in range(db):
        szam = random.randint(mettol,meddig)
        szamok.append(szam)
    return szamok
def parosValogatas(szamok):
    parosak = []
    for szam in szamok:
        if szam%2==0:
            parosak.append(szam)
    return parosak

'''
Alma 4
Körte 5
Barack 6
ab 2
dinnye 6
'''

def legRovidebbSzo(szavak):
    szo = szavak[0]
    for egy in szavak:
        if len(egy)<len(szo):
            szo = egy
    print(szo)