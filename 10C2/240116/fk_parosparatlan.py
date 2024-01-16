import os
os.system("cls")

szamok = []
f = open("szamok.sza","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    szam = int(sor)
    szamok.append(szam)
f.close()

parosFajl = open("paros.sza","w",encoding="utf-8")
paratlanFajl = open("paratlan.sza","w",encoding="utf-8")
for s in szamok:
    if s%2==0:
        parosFajl.write(f"{s}\n")
    else:
        paratlanFajl.write(f"{s}\n")
paratlanFajl.close()
parosFajl.close()