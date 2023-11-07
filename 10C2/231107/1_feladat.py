import os
import random
os.system("cls")

db = input("Add meg hány számot szeretnél: ")
db = int(db)

szamok = []

for _ in range(db):
    szam = random.randint(1,10000)
    szamok.append(szam)
print(szamok)