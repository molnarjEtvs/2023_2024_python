import os
os.system("cls")

km = input("Add meg mennyi km-t utaztál: ")
km = int(km)

dij = input("100km mennyibe kerül?")
dij = int(dij)

koltseg = 0

for x in range(1,(km+1)):
    if x%4==0 and x%6==0:
        koltseg += (dij/100)*(x*2)
    else:
        koltseg += (dij/100)*x

print(f"Költség: {koltseg} Ft")