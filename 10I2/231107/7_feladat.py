import os
import random
os.system("cls")


csoport = ["Ferenc","Katika","Sanyika","Béla","Luca","Bertalan"]

parokSzama = int(len(csoport)/2)

for _ in range(parokSzama):
    par1 = random.choice(csoport)
    csoport.remove(par1)
    par2 = random.choice(csoport)
    csoport.remove(par2)
    print(f"{par1}-{par2}")
    