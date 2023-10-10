import os
os.system("cls")

szam1 = input("Adj meg egy számot: ")
szam1 = int(szam1)
szam2 = input("Adj meg egy másik számot: ")
szam2 = int(szam2)

for x in range(szam1,szam2+1):
    if x%2==0:
        print(x)