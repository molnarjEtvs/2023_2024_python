import os
import random
os.system("cls")

jatekosok = []
db = input("Add meg hány játékos van: ")
db = int(db)

for _ in range(db):
    nev = input("Add meg a játékos nevét: ")
    jatekos = {}
    jatekos['nev'] = nev
    jatekos['dobasai'] = []
    for _ in range(5):
        dobas = random.randint(1,6)
        jatekos['dobasai'].append(dobas)
    jatekos['osszertek'] = sum(jatekos['dobasai'])
    jatekosok.append(jatekos)

print(jatekosok)
nyertes = {}
legNagyobb = 0
for jatekos in jatekosok:
    if jatekos['osszertek']>legNagyobb:
        nyertes = jatekos
        legNagyobb = jatekos['osszertek']
print(nyertes)