import os
os.system("cls")

szamsor = input("Add meg a számokat : -al elválasztva: ")
szamok = szamsor.split(":")
szamok2 = []
for x in szamok:
    szamok2.append(int(x))

legkissebb = min(szamok2)
legnagyobb = max(szamok2)
atlag = sum(szamok2)/len(szamok2)

print(f"legkisebb: {legkissebb}, legnagyobb: {legnagyobb}, átlag: {atlag}")