import os
os.system("cls")

termekek = []

while True:
    nev = input("Add meg a tétel nevét: ")
    if nev == "":
        break
    ar = input("Add meg az árat: ")
    ar = int(ar)
    termek = {}
    termek['nev'] = nev
    termek['ar'] = ar
    termekek.append(termek)

vegosszeg = 0
for egyTermek in termekek:
    vegosszeg += egyTermek['ar']

print(f"Fizetendő: {vegosszeg}")