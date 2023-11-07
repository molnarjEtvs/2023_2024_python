import random

szam1 = input("Adj meg egy számot: ")
szam1 = int(szam1)

szam2 = random.randint(1,10000)

if szam1>szam2:
    print(f"A felhasználó száma nagyobb mert {szam1}>{szam2}")
elif szam1<szam2:
    print(f"A gép száma nagyobb mert: {szam1}<{szam2}")
else:
    print(f"A két szám egyenlő mert: {szam1} = {szam2}")
