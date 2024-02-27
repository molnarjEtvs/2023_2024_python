def konyvRogzites():
    konyvCimek = []
    while True:
        cim = input("Add meg a könyv címét: ")
        if cim == "":
            break
        cim = cim.title()
        konyvCimek.append(cim)
    return konyvCimek

def konyvElemzes(cimek):
    db = len(cimek)
    print(f"Darabszám: {db} db")
    dbB = 0
    az = []
    for egyCim in cimek:
        if egyCim.find("b")>=0:
            dbB += 1
        if egyCim.startswith("A") == True and egyCim.endswith("z") == True:
            az.append(egyCim)
    print(f"B betűsek darabszáma: {dbB} db")
    utolsoElotti = cimek[-2]
    print(f"Utolsó előtti elem: {utolsoElotti}")
    separator = ", "
    szovegAz = separator.join(az)
    print(f"A-val kezd, z-re végződik: {szovegAz}")

d = konyvRogzites()
konyvElemzes(d)