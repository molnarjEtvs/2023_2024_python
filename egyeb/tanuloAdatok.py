import os
os.system("cls")

tanulok = []
while True:
    vezetekNev = input("Add meg a vezetéknevet: ")
    if vezetekNev == "":
        break
    keresztNev = input("Add meg a keresztnevet: ")
    atlag = input("Add meg az átlagot: ")
    atlag = float(atlag)
    tanulo = {}
    tanulo['keresztNev'] = keresztNev
    tanulo['vezetekNev'] = vezetekNev
    tanulo['atlag'] = atlag
    tanulok.append(tanulo)

print(tanulok)
