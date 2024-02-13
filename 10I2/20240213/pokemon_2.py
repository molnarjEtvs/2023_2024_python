import os
os.system("cls")


def pokemonRogzites():
    pokemonok = []
    while True:
        pokemon = input("Add meg a pokemont: ")
        if pokemon == "":
            break
        pokemonok.append(pokemon)
    return pokemonok

def kiErtekeles(pokok):
    db = len(pokok)
    b = []
    c = []
    mm = []
    for egy in pokok:
        if egy.startswith("b") == True:
            b.append(egy)
        elif egy.startswith("c") == True:
            c.append(egy)
        else:
            mm.append(egy)

    sep = ","
    bBetusek = sep.join(b)
    cBetusek = sep.join(c)
    mmBetusek = sep.join(mm)
    print(f"Rögzített adatok száma: {db} db")
    print(f"C betűsek: {cBetusek}")
    print(f"B betűsek: {bBetusek}")
    print(f"Minden más: {mmBetusek}")

x = pokemonRogzites()
kiErtekeles(x)
#kiErtekeles(pokemonRogzites())