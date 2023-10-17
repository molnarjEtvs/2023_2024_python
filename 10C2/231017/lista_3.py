import os
os.system("cls")

stoppolo = input("Add meg a stoppolot: ")
stoppolo = int(stoppolo)

szamok = []

while True:
    szam = input("Adj meg egy számot: ")
    szam = int(szam)
    if szam == stoppolo:
        break
    if szam not in szamok:
        szamok.append(szam)

print(szamok)