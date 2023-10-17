import os
os.system("cls")

evszamok = []

for _ in range(5):
    evszam = input("Adj meg egy évszámot: ")
    evszam = int(evszam)
    evszamok.append(evszam)

legkisseb = min(evszamok)
legnagyobb = max(evszamok)

print(evszamok)
print(f"Legkisebb: {legkisseb}")
print(f"Legnagyobb: {legnagyobb}")
