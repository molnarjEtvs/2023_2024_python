import os
os.system("cls")

db = input("Hány darab zöldésget rögzítesz? ")
db = int(db)

zoldsegek = []

for x in range(db):
    zoldseg = input("Adj meg egy zöldésget: ")
    zoldsegek.append(zoldseg)

print(zoldsegek)