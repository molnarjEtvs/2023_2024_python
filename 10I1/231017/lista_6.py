import os
os.system("cls")

paros = []
paratlanok = []
harommal = []

for szam in range(1,101):
    if szam%2==0:
        paros.append(szam)
    else:
        paratlanok.append(szam)

    if szam%3==0:
        harommal.append(szam)

print(paros)
print(paratlanok)
print(harommal)