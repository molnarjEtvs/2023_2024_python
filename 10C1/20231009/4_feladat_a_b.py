import os
os.system("cls")

szam1 = input("Első szám: ")
szam1 = float(szam1)

szam2 = input("Első szám: ")
szam2 = float(szam2)

szam3 = input("Első szám: ")
szam3 = float(szam3)

eredmeny = szam1**szam2//szam3

if eredmeny>100:
    print("nagyobb mint 100")
elif eredmeny>50:
    print("nagyobb mint 50")
else:
    print("Legfeljebb 50")