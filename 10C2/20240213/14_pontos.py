import os
os.system("cls")

def pokemonRogzites():
    nevek = []
    while True:
        nev = input("Add meg a nevet: ")
        if nev == "":
            break
        nevek.append(nev)
    return nevek

def kiErtekeles(nevek):
    db = len(nevek)
    b = []
    c = []
    mm = []
    for egyNev in nevek:
        if egyNev.startswith("b") == True:
            b.append(egyNev)
        elif egyNev.startswith("c") == True:
            c.append(egyNev)
        else:
            mm.append(egyNev)
    print(f"Rögzített darabszám: {db}")
    sep = ","
    bBetusek = sep.join(b)
    cbetusek = sep.join(c)
    mmBetusek = sep.join(mm)
    print(f"B betűsek: {bBetusek}")
    print(f"C betűsek: {cbetusek}")
    print(f"Minden más: {mmBetusek}")

p = pokemonRogzites()
kiErtekeles(p)
#kiErtekeles(pokemonRogzites())