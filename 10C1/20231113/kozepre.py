import os
os.system("cls")

szo = input("Add meg a szót: ")
szeles = input("Milyen hosszan: ")
szeles = int(szeles)

kitoltoKarakter = input("Kitöltő karakter: ")

print(szo.center(szeles,kitoltoKarakter))