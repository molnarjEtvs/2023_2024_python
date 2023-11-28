import os
os.system("cls")

meter = input("Méter: ")
meter = float(meter)

ar = input("Ar: ")
ar = float(ar)

szallitas = input("Szállítás: ")
szallitas = float(szallitas)

eladasiAr = (meter*1.1)*ar+szallitas

txt = str(eladasiAr)+" Ft"
print(txt.center(30,"*"))

