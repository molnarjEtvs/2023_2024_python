import os
os.system("cls")

koleszosok = []

while len(koleszosok)<10:
    nev = input("Add meg a nevet: ")
    atlag = input("Átlag")
    atlag = float(atlag)
    km = input("add meg a távot: ")
    km = int(km)
    if atlag>2.7 and km>=50:
        diak = {}
        diak['nev'] = nev
        diak['atlag'] = atlag
        diak['km'] = km
        koleszosok.append(diak)

print(koleszosok)