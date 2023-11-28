import os
os.system("cls")

meter = input("Mennyi kötelet vettek: ")
meter = int(meter)
ar = input("Add meg a méter árát: ")
ar = int(ar)
szallitas = input("Add meg a szállítási díjat: ")
szallitas = int(szallitas)
vegosszeg = (meter*1.1)*ar+szallitas
y = str(vegosszeg)+" Ft"
print(y.center(30,"*"))
