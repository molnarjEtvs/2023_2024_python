import os
os.system("cls")

szamok = []
while True:
    szam = input("Adj meg egy számot: ")
    szam = float(szam)
    if szam in szamok:
        break
    else:
        szamok.append(szam)
print(szamok)