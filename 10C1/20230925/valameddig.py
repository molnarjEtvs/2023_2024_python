
szam = input("Adj meg egy számot: ")
szam = int(szam)
osszeg = 0
for x in range(1,(szam+1)):
    osszeg += x
print(f"A számok összege: {osszeg}")