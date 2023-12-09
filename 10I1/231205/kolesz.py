import os
os.system("cls")

koleszosok = []

while len(koleszosok)<10:
    nev = input("Add meg a nevet: ")
    tav = input("Add meg a távolságot: ")
    tav = int(tav)
    atlag = input("Add meg az átlagot: ")
    atlag = float(atlag)
    if atlag>2.7 and km>=50:
        diak = {}
        diak['nev'] = nev
        diak['atlag'] = atlag
        diak['tav'] = tav
        koleszosok.append(diak)
print(koleszosok)
