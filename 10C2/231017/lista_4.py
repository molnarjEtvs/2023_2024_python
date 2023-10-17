import os
os.system("cls")

lebegok = []

while True:
    szam = input("Adj meg egy lebegőpontos számot: ")
    szam = float(szam)
    if szam in lebegok:
        break
    else:
        lebegok.append(szam)
print(lebegok)