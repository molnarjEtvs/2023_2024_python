import os
os.system("cls")

mondat = input("Adj meg egy mondatot: ")
szo = input("Adj meg egy szót: ")

if mondat.startswith(szo) == True:
    print("Kezdődik")
elif mondat.endswith(szo) == True:
    print("Végződik")
else:
    print("Egyik sem")