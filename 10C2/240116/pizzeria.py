import os
os.system("cls")

rendelesek = []
f = open("rendelesek.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adat = sor.split("\t")
    rendeles = {}
    rendeles['nev'] = adat[0]
    rendeles['ar'] = int(adat[1])
    rendeles['db'] = int(adat[2])
    rendeles['leadasiIdo'] = adat[3]
    rendeles['kiszallitasiIdo'] = adat[4]
    print(adat)
    rendelesek.append(rendeles)
f.close()

print(rendelesek)