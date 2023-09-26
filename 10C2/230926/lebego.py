
szam = 0
osszeg = 0
while szam!=3.14:
    szam = input("Adj meg egy számot: ")
    szam = float(szam)
    osszeg += szam
print(f"A lebegők összege: {osszeg}")