import random
class Pokemon:
    def __init__(self,dex,nev,ero):
        self.dex = dex
        self.nev = nev
        self.ero = ero

    def beallitas(self):
        self.ugarasiMagassag = self.ero*3*0.885

    def kepessegValasztas(self):
        kepessegek = ["párolgás","Tűzhányás","Lövés","Gurulás"]
        self.kepesseg = random.choice(kepessegek)
    
pokemonok = []

f = open("pokemonLista.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    pokemon1 = Pokemon(int(adatok[0]),adatok[1],int(adatok[2]))
    pokemon1.beallitas()
    pokemon1.kepessegValasztas()
    pokemonok.append(pokemon1)
    del pokemon1
f.close()

i = open("pokemonjaim.txt","w",encoding="utf-8")
for egyPokemon in pokemonok:
    i.write(f"Dex szám: #{egyPokemon.dex}\n")
    i.write(f"Név: {egyPokemon.nev}\n")
    i.write(f"Erő: {egyPokemon.ero} pont\n")
    i.write(f"Képesség: {egyPokemon.kepesseg}\n")
    i.write(f"Ugrási magasság: {egyPokemon.ugarasiMagassag}m\n")
    i.write("----------------------------\n")

i.close()