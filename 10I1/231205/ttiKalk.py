import os
import math
os.system("cls")

testsuly = input("Add meg a testsúlyt (kg): ")
testsuly = int(testsuly)

magassag = input("Add meg a magasságot (cm): ")
magassag = int(magassag)

tti = testsuly/math.pow((magassag/100),2)

if tti<18.5:
    print("Sovány")
elif tti>=18.5 and tti<25:
    print("Normál")
elif tti>=25 and tti<30:
    print("Túlsúlyos")
elif tti>=30:
    print("Elhízott")
else:
    print("Nem értelmezhető")