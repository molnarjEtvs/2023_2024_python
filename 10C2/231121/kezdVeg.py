import os
os.system("cls")

mondat = input("Add meg a mondatot: ")
szo = input("Add meg szót: ")

if mondat.startswith(szo) == True:
    print("A mondat a szóval kezdődik")
elif mondat.endswith(szo) == True:
    print("A mondat a szóra végződik")
else:
    print("Se nem kezd se nem végződik")


    