import os
os.system("cls")

szam = input("Adj meg egy számot: ")
szam = int(szam)
while szam!=23:
    szam = input("Adj meg egy számot: ")
    szam = int(szam)
print("A program véget ért")

#másik megoldás
while True:
    szam = input("Adj meg egy számot: ")
    szam = int(szam)
    if szam==23:
        break
print("A program véget ért")