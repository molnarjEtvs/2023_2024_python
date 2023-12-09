import os
os.system("cls")

lejatszasiLista = []

while True:
    eloado = input("Add meg az előadot: ").title()
    if eloado == "":
        break
    szamCime = input("Add meg a szám címét: ").title()
    mp = input("Add meg a hosszt: ")
    zene = {}
    zene["cime"] = szamCime
    zene["eloado"] = eloado
    zene['hossz'] = mp
    lejatszasiLista.append(zene)

print(lejatszasiLista)