import os
import random
os.system("cls")

db = input("Add meg hány számot szeretnél: ")
db = int(db)

mettol = input("Mettől szeretnéd? ")
mettol = int(mettol)

meddig = input("Meddig szeretnéd? ")
meddig = int(meddig)

szamok = []

for _ in range(db):
    szam = random.randint(mettol,meddig)
    szamok.append(szam)
print(szamok)