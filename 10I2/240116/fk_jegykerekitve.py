import math
tanulok = []
f = open("jegyek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adat = sor.split(";")
    tanulo = {}
    tanulo['nev'] = adat[0]
    tanulo['jegy'] = float(adat[1])
    tanulok.append(tanulo)
f.close()

i=open("tanulokkerek.txt","w",encoding="utf-8")
for egyTanulo in tanulok:
    i.write(f"Név: {egyTanulo['nev']}\n")
    i.write(f"Jegy: {math.floor(egyTanulo['jegy'])}\n")
    i.write("---------------------------\n")
i.close()