import os
import random
os.system("cls")

aiSzam = random.randint(1,3)
betuk = ['A','B','C']
aiBetu = random.choice(betuk)
ai = aiBetu+str(aiSzam)

tippekSzama = 0
while True:
    tippekSzama += 1
    userTipp = input("Add meg a tipped: ")
    userTipp = userTipp.upper()
    if ai == userTipp:
        print("NYERTÉL!")
        break

print(f"A tippjeid száma: {tippekSzama} db")