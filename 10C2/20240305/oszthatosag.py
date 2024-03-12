def oszthatosag(szamok,oszto):
    oszthatok = []
    for szam in szamok:
        if szam%oszto == 0:
            oszthatok.append(szam)
    return oszthatok

sz = [2,4,8,6,9,77,1654]
o = 3
v = oszthatosag(sz,o)
print(v)