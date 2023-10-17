import os
os.system("cls")

parosak = []
paratlanok = []
harommaloszhatok = []

for szam in range(1,101):
    if szam%2==0:
        parosak.append(szam)
    else:
        paratlanok.append(szam)
    
    if szam%3==0:
        harommaloszhatok.append(szam)

print(parosak)
print(paratlanok)
print(harommaloszhatok)