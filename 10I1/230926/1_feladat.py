szam = input("Add meg a számot: ")
szam = int(szam)

osszeg = 0
for y in range(1,(szam+1)):
    osszeg += y
print(f"Összeg: {osszeg}")