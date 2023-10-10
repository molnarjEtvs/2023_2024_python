import os 
os.system("cls")

szelesseg = input("Add meg a szélességet: ")
szelesseg = int(szelesseg)

hosszusag = input("Add meg a hosszúságot: ")
hosszusag = int(hosszusag)

arm2 = input("Add meg a m2 árat: ")
arm2 = int(arm2)

terulet=szelesseg*hosszusag
dij=terulet*arm2*1.1

print(f"A {terulet}m2 burkolás ára: {dij} Ft")