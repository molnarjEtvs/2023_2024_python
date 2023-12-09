import os
import random
os.system("cls")

jatekosok = []

db = input("Add meg a játékosok számát: ")
db = int(db)

for x in range(db):
    nev = input("Add meg a játékos nevét: ")
    dobasok = []
    osszDobas = 0
    for y in range(5):
        dobas = random.randint(1,6)
        osszDobas += dobas
        dobasok.append(dobas)
    jatekos = {}
    jatekos['nev'] = nev
    jatekos['osszDobas'] = osszDobas
    jatekos['dobasok'] = dobasok
    jatekosok.append(jatekos)

print(jatekosok)
pontszam = 0
nyertes = {}
for j in jatekosok:
    if j['osszDobas']>pontszam:
        nyertes = jatekos
        pontszam = jatekos['osszDobas']
print(nyertes)
