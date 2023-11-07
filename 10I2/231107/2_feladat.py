import os
import random
os.system("cls")

db = input("Hány darab véletlen számot szeretnél: ")
db = int(db)

mettol = input("Add meg a kezdő értéket: ")
mettol = int(mettol)
meddig = input("Add meg a vég értéket: ")
meddig = int(meddig)

szamok = []

for _ in range(db):
    szam = random.randint(mettol,meddig)
    szamok.append(szam)

print(szamok)