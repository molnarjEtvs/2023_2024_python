import os
os.system("cls")

ltavolsag = input("Add meg a lövési távolságot: ")
ltavolsag = int(ltavolsag)

lmagassag = input("Add meg a magasságot: ")
lmagassag = float(lmagassag)

if ltavolsag<=11 and lmagassag<=1:
    pontszam=2
elif ltavolsag>11 and ltavolsag<30 and lmagassag>=1:
    pontszam = 4
elif ltavolsag<30 and lmagassag>=2:
    pontszam = 6
else:
    pontszam = 0
print(f"pontszám: {pontszam}")