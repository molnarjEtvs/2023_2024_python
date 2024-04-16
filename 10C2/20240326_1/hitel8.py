import os
os.system("cls")

felvettOsszeg = input("Add meg a felvett összeget: ")
felvettOsszeg = int(felvettOsszeg)

futamido = input("Add meg a futamidő: ")
futamido = int(futamido)

thm = input("Add meg a THM: ")
thm = float(thm)

visszafizetendo = felvettOsszeg*(thm/100+1)
haviTorleszto = visszafizetendo/futamido

print(f"Visszafizetendő: {visszafizetendo} Ft")
print(f"Havi törlesztő: {haviTorleszto} Ft")