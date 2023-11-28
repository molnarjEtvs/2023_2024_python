import os
os.system("cls")

kosar = []

while True:
    nev = input("Add meg a termék nevét: ")
    if nev == "":
        break
    ar = input("Add meg az árát: ")
    ar = int(ar)
    termek = {}
    termek['nev'] = nev
    termek['ar'] = ar
    kosar.append(termek)

vegosszeg = 0
for tetel in kosar:
    vegosszeg+=tetel['ar']
print(f"végösszeg: {vegosszeg}")