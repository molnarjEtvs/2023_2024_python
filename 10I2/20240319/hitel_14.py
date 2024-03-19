import os
os.system("cls")

def torlesztoRogzites():
    torlesztok = []
    x = 1
    while True:
        osszeg = input(f"Add meg {x}. törlesztő részletet: ")
        x += 1
        osszeg = int(osszeg)
        if osszeg == 0:
            break
        osszeg = osszeg*0.9
        torlesztok.append(osszeg)
    return torlesztok

def torlesztoStatisztikak(t):
    db = len(t)
    print(f"Befizetések száma: {db} db")
    legalacsonyabb = min(t)
    print(f"Legalacsonyabb törlesztő: {legalacsonyabb} Ft")
    legmagasabb = max(t)
    print(f"Legmagasabb törlesztő: {legmagasabb} Ft")
    ossz = sum(t)
    print(f"Összbefizetés: {ossz} Ft")
    atlag = ossz/db
    print(f"Átlag befizetés: {atlag} Ft")
    otveAlatti = 0
    for egy in t:
        if egy<50000:
            otveAlatti+=1
    print(f"50 000 Ft alatti befizetések száma: {otveAlatti} db")

h = torlesztoRogzites()
torlesztoStatisztikak(h)