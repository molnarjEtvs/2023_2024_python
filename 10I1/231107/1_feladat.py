import os
import random
os.system("cls")

db = input("Hány db véletlen számot szeretnél: ")
db = int(db)

szamok = []
for _ in range(db):
    szam = random.randint(1,10000)
    szamok.append(szam)

print(szamok)