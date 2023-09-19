import os
os.system("cls")

szam = input("Add meg a számot:")
szam = int(szam)

if szam%2==0 and szam>0:
    print("Pozitív Páros szám")
elif szam%2>0 and szam>0:
    print("Pozitív Páratlan szám")
elif szam%2==0 and szam<0:
    print("Negatív Páros szám")
elif szam%2>0 and szam<0:
    print("Negatív Páratlan szám")
else:
    print("0")