import random
import os
os.system("cls")


nyeroSzamok = []

while len(nyeroSzamok) < 5:
    szam = random.randint(1,90)
    if szam not in nyeroSzamok:
        nyeroSzamok.append(szam)

nyeroSzamok.sort()

talalat = 0
for _ in range(5):
    szam = input("Add meg a tipped: ")
    szam = int(szam)
    if szam in nyeroSzamok:
        talalat+=1

print(f"Eltaláltál {talalat}db számot")
print(nyeroSzamok)