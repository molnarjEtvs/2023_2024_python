import random

szamok = []

db = input("Add meg hány darab számot szeretnél: ")
db = int(db)

a = input("Add meg mettől generáljak: ")
a = int(a)

b = input("Add meg meddig generáljak: ")
b = int(b)


for x in range(db):
    vszam = random.randint(a,b)
    szamok.append(vszam)
    
print(szamok)