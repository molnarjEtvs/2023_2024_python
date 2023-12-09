import os
os.system("cls")

utasok = []

while True:
    nev = input("Add meg a nevet: ")
    if nev == "":
        break
    szuletesiEv = input("Add meg a születési év: ")
    szuletesiEv = input(szuletesiEv)
    megtettKm = input("Megtett km: ")
    megtettKm = int(megtettKm)
    utas = {}
    utas['nev'] = nev
    utas['szuletesi_ev'] = szuletesiEv
    utas['megtett_km'] = megtettKm
    utasok.append(utas)

print(utasok)