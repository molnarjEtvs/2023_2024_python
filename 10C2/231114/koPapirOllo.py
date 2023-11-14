import os
import random
os.system("cls")

valaszok = ["KŐ","PAPÍR","OLLÓ"]

while True:
    
    f = input("1.Kő, 2.Papír, 3.Olló?: ")
    if f == "":
        break
    f = int(f)

    g = random.randint(1,3)

    if f == g:
        print("DÖNTETLEN")
    elif (f==1 and g == 3) or (f==2 and g == 1) or (f==3 and g == 2):
        print("NYERTÉL")
    else:
        print("VESZTETTÉL")
    print(f"Mert a felh: {valaszok[f-1]}, a gép: {valaszok[g-1]}")
    input("")
    os.system("cls")

print("Köszönöm a játékot!")