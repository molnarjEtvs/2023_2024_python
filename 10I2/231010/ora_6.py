

szelesseg = input("Add meg a szélességet: ")
szelesseg = int(szelesseg)

hosszusag = input("Add meg a hosszuságot: ")
hosszusag = int(hosszusag)

ar = input("Add me a m2 árat: ")
ar = int(ar)

terulet = szelesseg*hosszusag
koltseg = terulet*ar*1.1

print(f"A {terulet}m2 szoba burkolási ára: {koltseg} Ft")