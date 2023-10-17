import os
os.system("cls")

db = input("Add meg hány db zöldséget szeretnél rögzíteni: ")
db = int(db)

zoldsegek = []

for x in range(db):
    zoldseg = input("Adj meg egy zöldséget: ")
    zoldsegek.append(zoldseg)
print(zoldsegek)
