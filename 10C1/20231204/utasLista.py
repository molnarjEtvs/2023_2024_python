import os
os.system("cls")

utasLista = []

while True:
    nev = input("Add meg az utas nevét: ")
    if nev == "":
        break
    szuletesiEv = input("Add meg a születési évet: ")
    szuletesiEv = int(szuletesiEv)
    megtettKm = input("Add meg a megtett km-t: ")
    megtettKm = int(megtettKm)
    utas = {}
    utas['nev'] = nev
    utas['szuletesiEv'] = szuletesiEv
    utas['megtettKm'] = megtettKm
    utasLista.append(utas)
print(utasLista)