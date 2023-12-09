import os
os.system("cls")

koleszosok = []

while len(koleszosok)<10:
    nev = input("Név: ")
    tavolsag = input("Távolság: ")
    tavolsag = int(tavolsag)
    atlag = input("Átlag: ")
    atlag = float(atlag)
    if atlag>2.7 and tavolsag>50:
        diak = {}
        diak['nev'] = nev
        diak['atlag'] = atlag
        diak['tavolsag'] = tavolsag
        koleszosok.append(diak)

print(koleszosok)