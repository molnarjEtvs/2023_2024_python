db = input("Add meg mennyi zöldséget rögzítesz: ")
db = int(db)

zoldsegek = []
for _ in range(db):
    zoldseg = input("Add meg a zöldség nevét: ")
    zoldsegek.append(zoldseg)

print(zoldsegek)