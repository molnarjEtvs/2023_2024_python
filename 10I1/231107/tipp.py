import os
import random
os.system("cls")

kitalalandoSzam=random.randint(1,1000)
tipp = 0

while kitalalandoSzam != tipp:
    tipp = input("Add meg a tipped: ")
    tipp = int(tipp)
    if tipp>kitalalandoSzam:
        print("A gondolt szám kisebb")
    elif tipp<kitalalandoSzam:
        print("A gondolt szám nagyobb")
    else:
        print("Eltaláltad!")