import os
import random
os.system("cls")

jatekosokSzama = input("Add meg a játékosok számát: ")
jatekosokSzama = int(jatekosokSzama)

jatekosok = []

for _ in range(jatekosokSzama):
    nev = input("Add meg a játékos nevét: ")
    jatekos = {}
    jatekos['nev'] = nev
    jatekos['dobasai'] = []
    for _ in range(5):
        dobas = random.randint(1,6)
        jatekos["dobasai"].append(dobas)
    jatekos['pontszam'] = sum(jatekos["dobasai"])
    jatekosok.append(jatekos)

print(jatekosok)
nyertes = {}
legnagyobbPontszam = 0
for jatekos in jatekosok:
    if jatekos['pontszam']>legnagyobbPontszam:
        nyertes = jatekos
        legnagyobbPontszam = jatekos['pontszam']
print(nyertes)
