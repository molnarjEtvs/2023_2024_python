import os
import math
os.system("cls")

magassag = input("Add meg a magasságod (cm): ")
magassag = int(magassag)
suly = input("Add meg a súlyod (kg): ")
suly = int(suly)

tti = suly/math.pow((magassag/100),2)

if tti<18.5:
    print("Sovány")
elif tti>=18.5 and tti<25:
    print("Normál")
elif tti>=25 and tti<30:
    print("Túlsúlyos")
elif tti>30:
    print("Elhízott")
else:
    print("Nem értelmezhető")