import os
os.system("cls")

nev = input("Adj meg egy pokemon nevet: ")
ero = input("Add meg az erőt: ")
ero = int(ero)

utes = ero/2*0.43
rugas = ero/3*0.9

print(f"A pokemon neve: {nev}")
print(f"Erő: {ero} pont")
print(f"Rugás->{rugas} pont, Ütés->{utes} pont")