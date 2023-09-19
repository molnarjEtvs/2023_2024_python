import os
os.system('cls')

szam = input("Adj meg egy számot: ")
szam = int(szam)
hatvany = szam ** 5
if hatvany%2==0:
    print("Páros")
else:
    print("Páratlan")
    