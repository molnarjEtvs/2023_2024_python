f = open("fajl.txt","w",encoding="utf-8")
nev = input("Add meg a nevet: ")
szuletesiDatum = input("Add meg a születési dátumot: ")
osztaly = input("Add meg az osztályt: ")
f.write(f"{nev}\n")
f.write(f"{szuletesiDatum}\n")
f.write(f"{osztaly}\n")
f.close()

o = open("fajl.txt","r",encoding="utf-8")
elsoHarom = o.read(3)
o.close()