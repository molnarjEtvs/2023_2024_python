import os
import random
os.system("cls")

tanuloCsoport = ["Juci","Kati","Sanyi","Béla","Ferenc","Evelin"]
db = int(len(tanuloCsoport)/2)
for x in range(db):
    par1 = random.choice(tanuloCsoport)
    tanuloCsoport.remove(par1)
    par2 = random.choice(tanuloCsoport)
    tanuloCsoport.remove(par2)
    print(f"{par1}-{par2}")

    