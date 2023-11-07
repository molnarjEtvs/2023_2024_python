import os
os.system("cls")

szamok = []

while True:
    szam = input("Add meg a számot: ")
    szam = int(szam)
    if szam != 0:
        szamok.append(szam)
    else:
        break

db = len(szamok)
legnagyobb = max(szamok)
elosElem = szamok[0]
utolsoElotti = szamok[db-2]
utolso = szamok[db-1]
szorzat = elosElem*utolso
kulonbseg = szamok[1]-szamok[2]
dupla = min(szamok)*2
osszeg = sum(szamok)
atlag = osszeg/db
print(f"Elemek száma: {db} db")
print(f"Legnagyobb érték: {legnagyobb}")
print(f"Első elem: {elosElem}")
print(f"Utolsó előtti elem: {utolsoElotti}")
print(f"Első*Utolsó: {szorzat}")
print(f"Különbség: {kulonbseg}")
print(f"Dupla: {dupla}")
print(f"Összeg: {osszeg}")
print(f"Átlag: {atlag}")
