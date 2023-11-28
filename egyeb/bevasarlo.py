import os
os.system("cls")

kosar = []

while True:
    nev = input("Add meg a termék nevét: ")
    if nev == "":
        break
    ar = input("Ár: ")
    ar = int(ar)
    termek = {}
    termek['nev'] = nev
    termek['ar'] = ar
    kosar.append(termek)

vegosszeg = 0
for tetel in kosar:
    vegosszeg += tetel['ar']

print(f"Fizetendő összeg: {vegosszeg} Ft")
