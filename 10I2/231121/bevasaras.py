import os
os.system("cls")

kosar = []

while True:
    nev = input("Add meg a nevet: ")
    if nev == "":
        break
    ar = input("Add meg az árat: ")
    ar = int(ar)
    termek = {}
    termek['nev'] = nev
    termek['ar'] = ar
    kosar.append(termek)

print(kosar)

fizetendo = 0
for elem in kosar:
    fizetendo+=elem['ar']
print(f"Fizetendő: {fizetendo} Ft")