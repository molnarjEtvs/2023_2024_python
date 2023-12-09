import os
os.system("cls")

utasok = []

while True:
    nev = input("Add meg a nevet: ")
    if nev == "":
        break
    szuletesiEv = input("Add meg a születési évet: ")
    szuletesiEv = int(szuletesiEv)
    km = input("Megtett km szám: ")
    km = int(km)
    utas = {}
    utas['nev'] = nev
    utas['szulEv'] = szuletesiEv
    utas['megtettkm'] = km
    utasok.append(utas)

print(utasok)