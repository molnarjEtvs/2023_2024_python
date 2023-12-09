import os
os.system("cls")

koleszosok = []

while len(koleszosok)<10:
    nev = input("Add meg a nevet: ")
    atlag = input("Add meg az átlagot: ")
    atlag = float(atlag)
    km = input("Add meg a km: ")
    km = int(km)
    if km>=50 and atlag>2.7:
        diak = {}
        diak['nev'] = nev
        diak['atlag'] = atlag
        diak['km'] = km
        koleszosok.append(diak)
        print(f"rögzítve. szabad helyek száma: {10-len(koleszosok)}db ")
    else:
        print("megtagadva")
print(koleszosok)