def torlesztoRogzites():
    torlesztesek = []
    x = 1
    while True:
        torleszto = input(f"Add meg {x}. törlszetőt: ")
        x+=1
        torleszto = int(torleszto)
        if torleszto == 0:
            break
        torleszto = torleszto*0.9
        torlesztesek.append(torleszto)
    return torlesztesek

def torelsztoStatisztikak(tr):
    db = len(tr)
    print(f"Befizetések száma: {db} db")
    legAlcsanyoabb = min(tr)
    print(f"Legalacsonyabb: {legAlcsanyoabb} Ft")
    legMagasabb = max(tr)
    print(f"Legmagasabb törlesztő: {legMagasabb} Ft")
    osszbefizetes = sum(tr)
    print(f"Összbefizetés: {osszbefizetes} Ft")
    atlag = osszbefizetes/db
    print(f"Átlag befizetés: {atlag} Ft")
    dbOtven = 0
    for egyTorleszto in tr:
        if egyTorleszto<50000:
            dbOtven += 1
    print(f"50 000Ft alatti: {dbOtven} db")

h = torlesztoRogzites()
torelsztoStatisztikak(h)