#életerő|sebesség|képpeség
class Defender:
    def __init__(self,hp,speed,gadget):
        self.hp = hp
        self.speed = speed
        self.gadget = gadget

defenders = []
f = open("r6.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split("|")
    defender1 = Defender(int(adatok[0]),int(adatok[1]),adatok[2])
    defenders.append(defender1)
    del defender1
f.close()

print(f"{defenders[2].gadget}")
