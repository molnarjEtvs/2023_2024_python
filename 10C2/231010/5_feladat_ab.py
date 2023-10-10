import os
os.system("cls")

tavolsag = input("Add meg a távolságot: ")
tavolsag = int(tavolsag)

magassag = input("Add meg a magasságot: ")
magassag = float(magassag)

if tavolsag<=16 and magassag<=2:
    pontszam = 1
elif tavolsag>16 and tavolsag<40 and magassag>=2:
    pontszam = 2
elif tavolsag>40 and magassag>=3:
    pontszam = 3
else:
    pontszam = 0

print(f"A pontszám {pontszam}")