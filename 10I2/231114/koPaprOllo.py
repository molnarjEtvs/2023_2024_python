import random
import os
os.system("cls")

lehetoseg = ['Kő','Papír','Olló']
while True:
    g = random.randint(1,3)
    f = input("1.Kő, 2. Papír, 3.Olló")
    if f == "":
        break
    f = int(f)

    if g == f:
        print("Döntetlen")
    elif (f==1 and g == 3) or (f==2 and g == 1) or (f==3 and g == 2):
        print("Nyertél")
    else:
        print("Vesztettél")
    print(f"Felhasználó:{lehetoseg[f-1]} Gép:{lehetoseg[g-1]}")