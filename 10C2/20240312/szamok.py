f = open("szamok.txt","r",encoding="utf-8")
szamok = []
for sor in f:
    sor = sor.strip()
    szamok.append(int(sor))
f.close()
osszeg = sum(szamok)
print(f"{osszeg}")