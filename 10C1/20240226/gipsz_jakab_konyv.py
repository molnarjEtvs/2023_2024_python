def konyvRogzites():
    konyvCimek = []
    while True:
        cim = input("Add meg a könyv címét: ")
        if cim == "":
            break
        cim = cim.title()
        konyvCimek.append(cim)
    return konyvCimek

def konyvElemezes(cimek):
    db = len(cimek)
    print(f"Darabszám: {db} db")
    bDb = 0
    azBetusek = []
    for egyCim in cimek:
        if egyCim.find("b")>=0:
            bDb+=1
        if egyCim.startswith('A') == True and egyCim.endswith("z") == True:
            azBetusek.append(egyCim)
    print(f"B található {bDb} -ban")
    utolsoElottiElem = cimek[-2]
    print(f"Utolsó előtti elem: {utolsoElottiElem}")
    separator = ", "
    azBetusekSzoveg = separator.join(azBetusek)
    print(f"A-val kezdődik és z-re végződik: {azBetusekSzoveg}")

a = konyvRogzites()
konyvElemezes(a)

    