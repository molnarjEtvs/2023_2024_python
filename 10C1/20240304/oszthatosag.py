def kivalogat(szamok,oszto):
    kivSzamok = []
    for egySzam in szamok:
        if egySzam%oszto == 0:
            kivSzamok.append(egySzam)
    return kivSzamok


oszto = 4
szamok = [1,2,3,10,213,23453,465]
oszthatoak = kivalogat(szamok,oszto)
print(oszthatoak)