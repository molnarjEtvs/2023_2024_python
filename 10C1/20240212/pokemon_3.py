import os,random
os.system("cls")

class Pokemon:
    def __init__(self,dex,nev,ero):
        self.dex = dex
        self.nev = nev
        self.ero = ero
    
    def beallitas(self):
        self.ugrasiMagassag = self.ero*3*0.885
    
    def kepessegValasztas(self):
        kepessegek = ["párolgás","tűzhányás","lövés","gurulás"]
        self.kepesseg = random.choice(kepessegek)

pokemonok = []
f = open("pokemonLista.txt","r",encoding="utf-8")
for sor in f:
    sor = sor.strip()
    adatok = sor.split(",")
    pokemon1 = Pokemon(int(adatok[0]), adatok[1], int(adatok[2]))
    pokemon1.beallitas()
    pokemon1.kepessegValasztas()
    pokemonok.append(pokemon1)
    del pokemon1
f.close()

i = open("pokemonjaim.txt","w",encoding="utf-8")
for egy in pokemonok:
    i.write(f"Dex szám #: {egy.dex}\n")
    i.write(f"Név: {egy.nev}\n")
    i.write(f"Erő: {egy.ero} pont\n")
    i.write(f"Képesség: {egy.kepesseg}\n")
    i.write(f"Ugáris magasság: {egy.ugrasiMagassag}m\n")
    i.write("--------------------------\n")
i.close()