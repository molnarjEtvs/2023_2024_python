szamok = []
stoppolo = input("Add meg a stoppoló számot: ")
stoppolo = int(stoppolo)

while True:
    szam = input("Adj meg egy számot: ")
    szam = int(szam)
    if szam == stoppolo:
        break
    if szam not in szamok:
        szamok.append(szam)
print(szamok)
