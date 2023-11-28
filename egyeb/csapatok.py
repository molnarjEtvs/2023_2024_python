import os
import random
os.system("cls")

while True:
    csapatokSzama = input("Add meg a csapatok számát: ")
    csapatokSzama = int(csapatokSzama)
    if csapatokSzama%2==0:
        break

csapatok = []

while len(csapatok)<csapatokSzama:
    csapat = input("Add meg a csapat nevét: ")
    if csapat not in csapatok:
        csapatok.append(csapat)

sorsoltak = []
for _ in range(int(csapatokSzama/2)):
    csapat1 = random.choice(csapatok)
    csapatok.remove(csapat1)
    csapat2 = random.choice(csapatok)
    csapatok.remove(csapat2)
    par = {}
    par['csapat1'] = csapat1
    par['csapat1Golok'] = random.randint(0,5)
    par['csapat2'] = csapat2
    par['csapat2Golok'] = random.randint(0,5)
    sorsoltak.append(par)

for eredmeny in sorsoltak:
    print(f"{eredmeny['csapat1']}-{eredmeny['csapat2']}: {eredmeny['csapat1Golok']}-{eredmeny['csapat2Golok']}")