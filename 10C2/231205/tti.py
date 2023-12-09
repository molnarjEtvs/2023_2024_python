import os
import math
os.system("cls")

testSuly = input("Add meg a testsúlyt (kg): ")
testSuly = int(testSuly)

magassag = input("Add meg a magasságod (cm): ")
magassag = int(magassag)

tti = testSuly/math.pow((magassag/100),2)

if tti<18.5:
    print("Sovány")
elif tti>=18.5 and tti<25:
    print("Normál")
elif tti>=25 and tti<30:
    print("Túlsúly")
elif tti>30:
    print("Elhízott")
else:
    print("Értelmezhetetlen")