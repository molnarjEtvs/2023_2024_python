import os
import random
os.system("cls")

vszam = random.randint(1,3)
betuk = ['A','B','C']
vbetu = random.choice(betuk)
kombinacio = vbetu+str(vszam)

tippekSzama = 0
while True:
    ftipp = input("Add meg a tipped: ")
    ftipp = ftipp.capitalize()
    tippekSzama += 1
    if ftipp == "":
        break
    if kombinacio == ftipp:
        print("NYERTÉl!")
        break
    else:
        print("NEM TALÁLT! PRÓBÁLD ÚJRA!")
print(f"A játék vége! Tippek száma: {tippekSzama} db")