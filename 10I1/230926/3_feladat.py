osszeg = 0
szam = 0
while szam != 3.14:
    szam = input("Adj meg egy lebegő számot: ")
    szam = float(szam)
    osszeg = osszeg+szam
    #osszeg += szam
print(f"Az összeg: {osszeg}")