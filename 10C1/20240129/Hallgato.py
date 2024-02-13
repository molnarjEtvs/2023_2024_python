class Hallgato:
    def __init__(self,azonosito,evfolyam,kreditszam):
        self.azonosito = azonosito
        self.evfolyam = evfolyam
        self.kreditszam = kreditszam

    def targyFelvetel(self,targyKreditErtek):
        self.kreditszam += targyKreditErtek

    def vizsgazik(self):
        if self.kreditszam>0:
            self.evfolyam += 1
            self.kreditszam = 0
            return True
        else:
            return False
        
kati = Hallgato("1",10,100)
ferike = Hallgato("2",9,0)
kati.targyFelvetel(50)
katiEredmeny = kati.vizsgazik()
feriEredmeny = ferike.vizsgazik()
if katiEredmeny == True:
    print(f"{kati.azonosito} számú tanuló sikeresen levizsgázott")
else:
    print(f"{kati.azonosito} számú tanuló SIKERTELEN vizsgát tett")
if feriEredmeny == True:
    print(f"{ferike.azonosito} számú tanuló sikeresen levizsgázott")
else:
    print(f"{ferike.azonosito} számú tanuló SIKERTELEN vizsgát tett")

