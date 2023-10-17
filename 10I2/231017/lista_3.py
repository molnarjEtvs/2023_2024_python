import os
os.system("cls")

stoppolo = input("Add meg a stop számot: ")
stoppolo = int(stoppolo)

szamok = []

while True:
    szam = input("adj meg egy számot: ")
    szam = int(szam)
    if stoppolo == szam:
        break
    if szam not in szamok:
         szamok.append(szam)
print(szamok)
