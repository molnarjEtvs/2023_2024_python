import os
os.system("cls")

lovesiTavolsag = input("Lövési távolság: ")
lovesiTavolsag = int(lovesiTavolsag)

lovesiMagassag = input("Lövési magasság: ")
lovesiMagassag = float(lovesiMagassag)

if lovesiTavolsag<=16 and lovesiMagassag<=2:
    pontszam = 1
elif lovesiTavolsag>16 and lovesiTavolsag<40 and lovesiMagassag>=2:
    pontszam = 2
elif lovesiTavolsag>40 and lovesiMagassag>=3:
    pontszam = 3
else:
    pontszam = 0

print(f"Pontszám :{pontszam}")