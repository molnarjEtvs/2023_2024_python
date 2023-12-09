import os
os.system("cls")

zeneLista = []

while True:
    eloado = input("Add meg az előadót: ").title()
    if eloado == "":
        break
    cim = input("Add meg a szám címét: ").title()
    mp = int(input("Add meg a hosszát: "))
    zene = {}
    zene['eloado'] = eloado
    zene['cim'] = cim
    zene['hossz'] = mp
    zeneLista.append(zene)

print(zeneLista)
    