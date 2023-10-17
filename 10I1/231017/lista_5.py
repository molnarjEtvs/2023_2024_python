import os
os.system("cls")


evszamok = []

for x in range(5):
    szam = input("Add meg az évszámot: ")
    szam = int(szam)
    evszamok.append(szam)

legkisebb = min(evszamok)
legnagyobb = max(evszamok)
print(f"Legkisebb: {legkisebb}")
print(f"Legnagyobb: {legnagyobb}")
