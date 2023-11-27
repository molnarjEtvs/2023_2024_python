import os
os.system("cls")

ar = input("Mennyibe kerül a métere: ")
ar = int(ar)
meter = input("Hány métert vett: ")
meter = int(meter)
szktsg = input("Szállítási költség: ")
szktsg = int(szktsg)

vegosszeg = (meter*1.1)*ar+szktsg
kiiras = str(vegosszeg)+"Ft"
kiiras = kiiras.center(30,"*")
print(kiiras)
