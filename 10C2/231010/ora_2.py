import os
os.system("cls")

szam = input("Add meg a számot: ")
szam = int(szam)

for x in range(szam,0,-1):
    if x%3==0:
        print(x)