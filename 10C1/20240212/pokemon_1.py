import os
os.system("cls")

nev = input("Add meg a pokemon nevét: ")
ero = input("Add meg az erőt: ")
ero = int(ero)

utesiPontszam = (ero/2)*0.43
rugasiPontszam = (ero/3)*0.9

print(f"A pokemon neve: {nev}")
print(f"Erő: {ero} pont")
print(f"Rúgás -> {rugasiPontszam} pont, Ütés: {utesiPontszam} pont")

