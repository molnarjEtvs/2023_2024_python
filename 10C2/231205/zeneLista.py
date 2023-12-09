import os
os.system("cls")

zeneLista = []

while True:
    eloado = input("Add meg az előadót: ").title()
    if eloado == "":
        break
    cim = input("Add meg a szám címét: ").title()
    mp = input("Add meg a mp számát: ")
    mp = int(mp)
    zene = {}
    zene['cim'] = cim
    zene['eloado'] = eloado
    zene['hossz'] = mp
    zeneLista.append(zene)

print(zeneLista)