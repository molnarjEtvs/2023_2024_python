class Macska:
    def __init__(self,nev,suly,ehseg):
        self.nev = nev
        self.suly = suly
        self.ehseg = ehseg

    def eszik(self,etelMennyiseg):
        if self.ehseg == True:
            self.suly += etelMennyiseg
            self.ehseg = False
            print(f"A {self.nev} macska evett")
            return True
        else:
            print(f"A {self.nev} macska NEM evett")
            return False
        
    def futkos(self):
        print(f"A {self.nev} macska futkosott")
        self.suly -= 0.1
        if self.ehseg == False:
            self.ehseg = True

    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly: {self.suly}")
        if self.ehseg == True:
            print("Éhes-e: Igen")
        else:
            print("Éhes-e: Nem")

macska1 = Macska("Garfield",10,True)
macska2 = Macska("Cirmi",4,False)
macska1.eszik(0.4)
macska2.eszik(0.6)
macska1.futkos()
macska2.futkos()
for x in range(10):
    macska1.futkos()

macska1.jelenlegiErtekek()
macska2.jelenlegiErtekek()