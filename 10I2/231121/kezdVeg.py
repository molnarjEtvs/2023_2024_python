import os
os.system("cls")

mondat = input("Add meg a mondatot: ")
szo = input("Add meg a szót: ")

if mondat.startswith(szo) == True:
    print("Kezd")
elif mondat.endswith(szo) == True:
    print("Végződik")
else:
    print("Egyik sem")