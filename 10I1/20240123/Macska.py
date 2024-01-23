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
            return True
        else:
            return False
        
    
    def futkos(self):
        self.suly -= 0.1
        if self.ehesE == False:
            self.ehesE = True

    def jelenlegiErtekek(self):
        print(f"Név: {self.nev}")
        print(f"Súly {self.suly} kg")
        if self.ehesE == True:
            print(f"Éhes-e: IGEN")
        else:
            print(f"Éhes-e: NEM")

macska1 = Macska("Garfield",9.3,True)
macska2 = Macska("Cirmi",4.2,False)
macska1.futkos()
for _ in range(10):
    macska2.futkos()
macska1.eszik(1.2)
macska2.eszik(0.4)
macska1.jelenlegiErtekek()
macska2.jelenlegiErtekek()