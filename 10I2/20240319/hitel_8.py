import os
os.system("cls")

felvettOsszeg = input("Add meg a felvett összeget: ")
felvettOsszeg = int(felvettOsszeg)

futamido = input("Add meg a hónapok számát: ")
futamido = int(futamido)

thm = input("Add meg a THM-et: ")
thm = float(thm)

visszafizetendo = felvettOsszeg*(thm/100+1)
haviTorleszto =  round(visszafizetendo/futamido)

print(f"Visszafizetendő összeg: {visszafizetendo} Ft")
print(f"Havi törlesztő: {haviTorleszto} Ft")