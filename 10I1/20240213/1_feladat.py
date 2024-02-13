import os
os.system("cls")

nev = input("Add meg a pokemon nevét: ")
ero = input("Add meg az erőt: ")
ero = int(ero)

utesiPsz = ero/2*0.43
rugasPsz = ero/3*0.90

print(f"A pokemon neve: {nev}")
print(f"Erő: {ero} pont")
print(f"Rugás->{rugasPsz} pont, Ütés->{utesiPsz} pont")