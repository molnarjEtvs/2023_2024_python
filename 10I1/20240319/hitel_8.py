import os
os.system("cls")

felvettOsszeg = input("Add meg az összeget: ")
felvettOsszeg = int(felvettOsszeg)

honapokSzama = input("Add meg a hónapok számát: ")
honapokSzama = int(honapokSzama)

thm = input("Add meg a THM-et: ")
thm = float(thm)

visszfizetendo = felvettOsszeg*(thm/100+1)
haviTorleszto = round(visszfizetendo/honapokSzama)

print(f"Visszafizetendő összeg: {visszfizetendo} Ft")
print(f"Havi törlesztő részlet: {haviTorleszto} Ft")