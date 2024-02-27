def konyvRogzites():
    konyvCimek = []
    while True:
        cim = input("Add meg a könyv címét: ")
        if cim == "":
            break
        cim=cim.title()
        konyvCimek.append(cim)
    return konyvCimek

def konyvElemezes(cimek):
    db = len(cimek)
    print(f"Darabszám: {db} db")
    bdb = 0
    azBet = []
    for egyCim in cimek:
        if egyCim.find("b")>=0:
            bdb+=1
        if egyCim.startswith("A") == True and egyCim.endswith("z") == True:
            azBet.append(egyCim)
    print(f"B betűsek száma: {bdb} db")
    utolsoElottiElem = cimek[-2]
    print(f"Utolsó előtti elem: {utolsoElottiElem}")
    sep = ", "
    szoveg = sep.join(azBet)
    print(f"A-z: {szoveg}")

f = konyvRogzites()
konyvElemezes(f)