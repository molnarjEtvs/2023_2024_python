import os
import math
os.system("cls")

testSuly = input("Add meg a testsúlyod (kg): ")
testSuly = int(testSuly)
magassag = input("Add meg a magasságot (cm): ")
magassag = int(magassag)

tti = testSuly/math.pow((magassag/100),2)

if tti<18.5:
    print("sovány")
elif tti>=18.5 and tti<25:
    print("Normál")
elif tti>=25 and tti<30:
    print("Túlsúlyos")
elif tti>30:
    print("Elhízott")
else:
    print("Nem értelmezhető")