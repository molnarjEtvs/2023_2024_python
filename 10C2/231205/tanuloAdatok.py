import os
os.system("cls")

tanulok = []

while True:
    vezetekNev = input("Add meg a vezeték nevet: ")
    if vezetekNev == "":
        break
    keresztNev = input("Add meg a keresztnevet: ")
    atlag = input("Add meg az átlag")
    atlag = float(atlag)
    tanulo = {}
    tanulo['vezetekNev'] = vezetekNev
    tanulo['keresztNev'] = keresztNev
    tanulo['atlag'] = atlag
    tanulok.append(tanulo)

print(tanulok)