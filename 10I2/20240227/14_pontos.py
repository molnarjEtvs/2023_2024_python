def konyvRogzites():
    konyvCimek = []
    while True:
        cim = input("Add meg a könyv címet: ")
        if cim == "":
            break
        cim = cim.title()
        konyvCimek.append(cim)
    return konyvCimek

def konyvElemzes(cimek):
    db = len(cimek)
    print(f"Darabszám: {db} db")
    dbb = 0
    azVeg = []
    for egyCim in cimek:
        if egyCim.find("b")>=0:
            dbb+=1
        if egyCim.startswith("A") == True and egyCim.endswidth("z") == True:
            azVeg.append(egyCim)

    separator = ", "
    azSzoveg = separator.join(azVeg)
    print(f"B található {dbb} db-ban")
    utolsoElotti = cimek[-2]
    print(f"Utolsó előtti: {utolsoElotti}")
    print(f"A-val kezdődik és z-re végződik: {azSzoveg}")


d = konyvRogzites()
konyvElemzes(d)