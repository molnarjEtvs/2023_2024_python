macskak = []
#macska = {}
#macska['nev'] = ?
#macska['szin'] = ?

f = open("macskak.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(";")
    macska = {}
    macska['nev'] = adatok[0]
    macska['szin'] = adatok[1]
    macskak.append(macska)
f.close()

print(f"{macskak[1]['szin']}")