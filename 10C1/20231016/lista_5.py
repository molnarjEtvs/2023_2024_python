
evszamok = []
for _ in range(5):
    evszam = input("Add meg az évszámot: ")
    evszam = int(evszam)
    evszamok.append(evszam)

legkissebb = min(evszamok)
legnagyobb = max(evszamok)

print(evszamok)
print(f"Legkissebb: {legkissebb}")
print(f"Legnagyobb: {legnagyobb}")