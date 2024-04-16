def torlesztoRogzites():
    torelesztesek = []
    sorszam = 1
    while True:
        torleszto = input(f"Add meg a(z) {sorszam}. törlesztő részletet: ")
        sorszam+=1
        torleszto = int(torleszto)
        if torleszto == 0:
            break
        torleszto = torleszto*0.9
        torelesztesek.append(torleszto)
    return torelesztesek

def torlesztoStatisztikak(reszletek):
    db = len(reszletek)
    print(f"Befizetsések száma: {db} db")
    legAlacsonyabb = min(reszletek)
    print(f"Legalacsonyabb: {legAlacsonyabb} Ft")
    legMagasabb = max(reszletek)
    print(f"Legmagasabb: {legMagasabb} Ft")
    osszesen = sum(reszletek)
    print(f"Összbefizetés: {osszesen} Ft")
    atlag = osszesen/db
    print(f"Átlag: {atlag} Ft")
    db50=0
    for egy in reszletek:
        if egy<50000:
            db50+=1
    print(f"50.000 Ft alattiak száma: {db50} db")

torlesztoStatisztikak(torlesztoRogzites())
