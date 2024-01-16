import os
os.system("cls")

szamok = []
f = open("szamok.sza","r",encoding="utf-8")
for sor in f:
    szam = int(sor.strip())
    szamok.append(szam)
f.close()

parosFajl = open("parosSzamok.txt","w",encoding='utf-8')
paratlanFajl = open("paratlanSzamok.txt","w",encoding='utf-8')
for egySzam in szamok:
    if egySzam %2==0:
        #páros fájlba írás
        parosFajl.write(f"{egySzam}\n")
    else:
        #páratlanba
        paratlanFajl.write(f"{egySzam}\n")
parosFajl.close()
paratlanFajl.close()