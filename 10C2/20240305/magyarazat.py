def fuggveny(szamok):
    s = 0
    for szam in szamok:
        s+=szam
    return s

def eljaras(osszeg):
    print(osszeg)

z = [1,2,3]
h = fuggveny(z)
eljaras(h)

h = fuggveny([3,3,56])

h = fuggveny([45,8,987,456])
h = fuggveny([34,45,567])

