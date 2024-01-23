class Macska:
    def __init__(self,nev,suly,ehesE):
        self.nev = nev
        self.suly = suly
        self.ehesE = ehesE
        print(f"{self.nev} macska létrejött")

    def eszik(self,etelMennyiseg):    
        if self.ehesE == True:
            self.suly += etelMennyiseg
            self.ehesE = False
            print(f"{self.nev} macska evett")
            return True
        else:
            print(f"{self.nev} macska NEM evett")
            return False
        
    def futkos(self):
        self.suly -= 0.1
        print(f"{self.nev} macska futkos")
        if self.ehesE == False:
            self.ehesE = True

    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly: {self.suly}")
        if self.ehesE == True:
            print(f"Éhes-e: igen")
        else:
            print(f"Éhes-e: NEM")

macska1 = Macska("Garfield",8.9,True)
macska2 = Macska("Cirmi",3.2,False)
macska1.futkos()
for x in range(10):
    macska2.futkos()
macska1.eszik(0.5)
macska2.eszik(0.8)
macska1.jelenlegiErtekek()
macska2.jelenlegiErtekek()


