
szamok = []
f = open("szamok.sza","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    szam = int(sor)
    szamok.append(szam)
f.close()

i = open("szamokOsszege.sza","w",encoding="utf-8")
osszeg = sum(szamok)
i.write(str(osszeg))
i.close()