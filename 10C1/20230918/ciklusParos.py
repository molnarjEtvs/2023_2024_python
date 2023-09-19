import os
os.system("cls")

parosSzamok = ""
for y in range(11,201):
    if y%2==0:
        parosSzamok += str(y)+","
print(parosSzamok)
