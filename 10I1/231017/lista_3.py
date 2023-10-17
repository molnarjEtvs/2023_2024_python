import os
os.system("cls")

szamok = []
stoppolo = input("Add meg melyi számnál álljak meg: ")
stoppolo = int(stoppolo)

while True:
    szam = input("Add meg a számot: ")
    szam = int(szam)
    if szam == stoppolo:
        break
    
    if szam not in szamok:
        szamok.append(szam)

print(szamok)

