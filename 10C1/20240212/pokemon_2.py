import os
os.system("cls")

def pokemonRogzites():
    pokemonok = []
    while True:
        pokemon = input("Add meg a pokemon nevét: ")
        if pokemon == "":
            break
        pokemonok.append(pokemon)
    return pokemonok

def kiErtekeles(pokok):
    db = len(pokok)
    bBetusek = []
    cBetuesk = []
    egyebBetusek = []
    for egyPokemon in pokok:
        if egyPokemon.startswith('b') == True:
            bBetusek.append(egyPokemon)
        elif egyPokemon.startswith('c') == True:
            cBetuesk.append(egyPokemon)
        else:
            egyebBetusek.append(egyPokemon)
    
    print(f"Rögzített adatok száma: {db}")
    separator = ","
    bSek = separator.join(bBetusek)
    cSek = separator.join(cBetuesk)
    egySek = separator.join(egyebBetusek)
    print(f"B betűsek: {bSek}")
    print(f"C betűsek: {cSek}")
    print(f"Minden más: {egySek}")

valasz = pokemonRogzites()
kiErtekeles(valasz)