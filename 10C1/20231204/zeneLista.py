import os
os.system("cls")

lejatszasiLista = []

while True:
    eloado = input("Add meg az előadó nevét: ").title()
    if eloado == "":
        break
    cim = input("Szám címe:").title()
    mp = input("Szám hossza: ")
    mp = int(mp)
    zene = {}
    zene['eloado'] = eloado
    zene['hossza'] = mp
    zene['cim'] = cim
    lejatszasiLista.append(zene)
print(lejatszasiLista)