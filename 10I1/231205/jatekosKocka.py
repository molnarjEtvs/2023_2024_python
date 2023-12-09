import os
import random
os.system("cls")

jatekosok = []

jatekosokSzama = input("Add meg a játékosok számát: ")
jatekosokSzama = int(jatekosokSzama)

for _ in range(jatekosokSzama):
    nev = input("Add meg a nevet: ")
    jatekos = {}
    jatekos['nev'] = nev
    jatekos['dobasok'] = []
    for _ in range(5):
        dobas = random.randint(1,6)
        jatekos['dobasok'].append(dobas)
    jatekos['pontszam'] = sum(jatekos['dobasok'])

    jatekosok.append(jatekos)

print(jatekosok)

nyertes = {}
legnagyobb = 0
for jatekos in jatekosok:
    if legnagyobb<jatekos['pontszam']:
        legnagyobb = jatekos['pontszam']
        nyertes = jatekos

print(nyertes)
    