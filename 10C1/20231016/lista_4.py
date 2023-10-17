szamok = []
while True:
    szam = input("Adj meg egy számot: ")
    szam = float(szam)
    if szam not in szamok:
        szamok.append(szam)
    else:
        break

print(szamok)