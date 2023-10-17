import os
os.system("cls")

zoldsegek = []
db = input("Mennyi zöldésget rögzítesz: ")
db = int(db)

for x in range(db):
    zoldseg = input("Add meg a zöldség nevét: ")
    zoldsegek.append(zoldseg)
print(zoldsegek)