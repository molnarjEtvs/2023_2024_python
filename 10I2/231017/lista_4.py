import os
os.system("cls")

szamok = []

while True:
    szam = input("Adj meg egy lebegőpontos számot: ")
    szam = float(szam)
    if szam not in szamok:
        szamok.append(szam)
    else:
        break
print(szamok)