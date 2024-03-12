def oszt(szamok,oszto):
    o = []
    for szam in szamok:
        if szam%oszto==0:
            o.append(szam)
    return o

sz = [45,567,7,4,8]
k = 5
v = oszt(sz,k)
print(v)