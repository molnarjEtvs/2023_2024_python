import os
os.system("cls")

evszamok = []

for _ in range(5):
    evszam = input("Add meg az évszámot: ")
    evszam = int(evszam)
    evszamok.append(evszam)

legkisebb = min(evszamok)
legnagyobb = max(evszamok)

print(evszamok)
print(f"Legkisebb: {legkisebb}")
print(f"Legnagyobb: {legnagyobb}")
