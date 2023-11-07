import os
os.system("cls")

szamok = []

while True:
    szam = input("Adj meg egy számot: ")
    szam = int(szam)
    if szam == 0:
        break
    szamok.append(szam)

db = len(szamok)
print(f"Az elemek száma: {db} db")

legnagyobb = max(szamok)
print(f"A legnagyobb érték: {legnagyobb}")

elsoElem = szamok[0]
print(f"Első elem: {elsoElem}")

utolsoElotti = szamok[db-2]
print(f"Az utolsó előtti elem: {utolsoElotti}")

szorzat = elsoElem*utolsoElotti
print(f"Szorzat: {szorzat}")

kulonb = szamok[1]-szamok[2]
print(f"Különség: {kulonb}")

dupla = min(szamok)*2
print(f"Dupla: {dupla}")

osszeg = sum(szamok)
print(f"Összeg: {osszeg}")

atlag = osszeg/db
print(f"Átlag: {atlag}")



