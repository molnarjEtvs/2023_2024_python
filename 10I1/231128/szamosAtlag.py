import os
os.system("cls")

szamok = input("Add meg a számokat : -al: ")
szamok2 = szamok.split(":")
szamok3 = []
for x in szamok2:
    szamok3.append(int(x))

legkisebb = min(szamok3)
legnagyobb = max(szamok3)
atalag = sum(szamok3)/len(szamok3)

print(f"Kisebb: {legkisebb}, Nagyobb: {legnagyobb}, Átlag: {atalag}")
