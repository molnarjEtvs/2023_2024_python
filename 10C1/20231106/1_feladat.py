import random

szamok = []

db = input("Add meg hány darab számot szeretnél: ")
db = int(db)

for x in range(db):
    vszam = random.randint(1,10000)
    szamok.append(vszam)
    
print(szamok)