import os
os.system("cls")

mondat = input("Adj meg egy mondatot: ")
szo = input("Adj meg egy szót: ")

if mondat.startswith(szo) == True:
    print("A szóval kezdődik")
elif mondat.endswith(szo) == True:
    print("A szóval végződik")
else:
    print("Sem nem kezd se nem végez.")