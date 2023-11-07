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
print(f"Elemek száma: {db} db")

legnagyobb = max(szamok)
print(f"Legnagyobb érték: {legnagyobb}")

elsoElem = szamok[0]
print(f"Az első elem: {elsoElem}")

utolsoElotti = szamok[-2]
print(f"Utolsó előtti elem: {utolsoElotti}")

szorzat = elsoElem*utolsoElotti
print(f"Szorzat: {szorzat}")

kulonbseg = szamok[1]-szamok[2]
print(f"Különbség: {kulonbseg}")

dupla = min(szamok)*2
print(f"Dupla: {dupla}")

osszeg = sum(szamok)
print(f"Összeg: {osszeg}")

atlag = osszeg/db
print(f"Átlag: {atlag}")

