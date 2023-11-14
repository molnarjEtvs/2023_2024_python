import random
import os
os.system("cls")

lehetosegek = ["Kő","Papír","Olló"]

while True:
    g = random.randint(1,3)
    f = input("1.Kő,2.Papír,3.Olló: ")
    if f == "":
        break
    f = int(f)

    if g == f:
        print("DÖNTETELEN")
    elif (f==1 and g==3) or (f==2 and g==1) or (f==3 and g==2):
        print("NYERTÉL")
    else:
        print("VESZTETTÉL")


    print(f"F: {lehetosegek[f-1]} | G: {lehetosegek[g-1]}")