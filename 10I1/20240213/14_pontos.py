def pokemonRogzites():
    pokemonok = []
    while True:
        pnev = input("Add meg a pokemon nevet: ")
        if pnev == "":
            break
        pokemonok.append(pnev)
    return pokemonok

def kiErtekeles(p):
    db = len(p)
    b = []
    c = []
    mm = []
    for egy in p:
        if egy.startswith("b") == True:
            b.append(egy)
        elif egy.startswith("c") == True:
            c.append(egy)
        else:
            mm.append(egy)

    
    sep = ", "
    bBetusek =  sep.join(b)
    cBetusek = sep.join(c)
    mmBetusek = sep.join(mm)
    print(f"Rögzített adatok száma: {db} db")
    print(f"B betűsek {bBetusek}")
    print(f"C betűsek: {cBetusek}")
    print(f"Minden más: {mmBetusek}")


pokes = pokemonRogzites()
kiErtekeles(pokes)

#kiErtekeles(pokemonRogzites())