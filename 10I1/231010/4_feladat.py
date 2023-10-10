import os 
os.system("cls")

szam1 = input("Add meg az 1 számot: ")
szam1 = float(szam1)

szam2 = input("Add meg az 2 számot: ")
szam2 = float(szam2)

szam3 = input("Add meg az 3 számot: ")
szam3 = float(szam3)

eredmeny = szam1**szam2//szam3

if eredmeny>100:
    print("Nagyobb mint 100")
elif eredmeny>50:
    print("NAgyobbb mint 50")
else:
    print("Legfeljebb 50")